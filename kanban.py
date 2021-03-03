import os
import re
import argparse
import sys
from typing import List, Optional


ELLIPSIS_PATTERN = r'\s\.\.\.\s'
TAG_PATTEN = r'\s\.\w+\s'


class Item:
    def __init__(self,
                 path: str,
                 line_number: int,
                 contents: str,
                 tags: List[str]):
        self.path = path
        self.line_number = line_number
        self.contents = contents
        self.tags = tags

    def __repr__(self):
        return f"\nItem({self.path}, {self.line_number},\n{self.contents[:100]}, {self.tags})\n"""


def traverse_dir(basepath: str) -> List[str]:
    """Return the list of all markdown files below the given directory."""
    acc = []
    for root, dirs, files in os.walk(basepath):
        path = os.path.relpath(root, basepath)
        for file in files:
            if file.endswith('.md'):
                acc.append(path + os.sep + file)
    return acc


def parse_note_into_item(note: str, path: str) -> Optional[Item]:
    if re.search(ELLIPSIS_PATTERN, note) is None:
        return None
    tag_lines = [line
                 for line in note.split('\n')
                 if re.search(ELLIPSIS_PATTERN, line) is not None]
    tags = [tag
            for line in tag_lines
            for tag in re.findall(TAG_PATTEN, line)]
    return Item(
        path=path,
        line_number=None,  # TODO
        contents=note,
        tags=tags
    )


def parse_file_into_items(filepath: str) -> List[Item]:
    """Parse the file, get a list of items."""
    acc = []
    with open(filepath, encoding='utf-8', newline='\n') as f:
        # We discard the parts before the first and after the last line rules
        notes = f.read().split('\n\n---\n\n')[1:-1]
    for note in notes:
        result = parse_note_into_item(note, filepath)
        if result is not None:
            acc.append(result)
    return acc


if __name__ == '__main__':
    basepath = sys.argv[1]
    for filepath in traverse_dir(basepath):
        print("\n---\n".join(map(str, parse_file_into_items(os.path.join(basepath, filepath)))))
