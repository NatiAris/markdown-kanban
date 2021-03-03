# markdown-kanban
Render a collection of markdown notes as a board

## Outline

Parsing
1. Recursively go through all `.md` files under the provided directory
2. Split them on `"\n\n---\n\n"`, discard the parts before the first and after the last line rules
3. Make items from notes that match `\s\.\.\.\s` pattern (ellipsis)
4. Extract tags, if any, from the line with ellipsis

An item should retail the following info
- the relative path to the note
- the line number of the line that contained ellipsis
- all lines of the note
- tags, if any

Rendering
1. Order items by status
2. Show status as a header, then the list of notes


## Tags

Status tags
`.backlog` (the default status)
`.upnext`
`.inprogress`
`.blocked`
`.done`

Parsing tags
`.above` — consider everything above the item to be items as well
`.below` — same, but for items below

## Definitions

Note
A piece of text preceded and followed by line rules

Item
A card that goes on the board
