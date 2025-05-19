# Project Management

## Next Steps

Part 1

* Build test manuscript
* Make decisions on where/what project definition will/can exist
* Stub pre-processor
* Construct the pipeline

Part 2

* Get pandoc's typst template as a starting point
* Grab epub css from previous work
* Define where/how to find supplement front/back matter.
* overrides
    * Extra typst definitions/functions (dropdown, author-defined, etc)
    * Extra css definitions (dropdown, author-defined, etc)

## Sources

* https://gatekeeperpress.com/parts-of-a-book/
* https://blog.reedsy.com/guide/parts-of-a-book/
* https://kindlepreneur.com/design-beautiful-chapter-themes/


`pandoc <file> -t json -o <file.json>` produces the raw pandoc AST.

* It only contains one metadata section no matter how many sections are in the doucment.
* If there is a key that appears in multiple sections only the last one will be in the meta section.

See also `pypandoc` and `pypanflute`