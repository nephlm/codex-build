## Goals

* A command line that can be run to build professional looking basic novels in pdf and ebook formats given a one or more Markdown documents.
* Should contain the interior book design expected in a professional novel.
* pdf
  * headers
    * some combination of: author, title, chapter title
  * footers
    * Just a number (center or outside)
  * Optional higher level "books" or "parts" that contain chapters.
  * chapter headings
    * Start on odd pages  
    * Number, title, epigraph, POV/time/other note
  * drop caps
  * front matter
    * title page
    * copyright page
    * epigraph
    * Acknowledgements/introductions/etc
      * These are all the same as far as layout is concerned
    * Table of contents (maybe, optional)
    * half-title page
  * back matter
    * Afterwords/Author notes/etc 
      * Basically the same as acknowledgement/introduction as far layout is concerned.
* ebook
  * chapter headings
    * optional books/parts/acts higher level organizations
  * drop caps
  * front matter
  * back matter


The following would be nice, but are not goals:

* Run on anything besides linux.
* The goal is good enough, not super customizable in the first few iterations.
* Produce any other kind of book besides a modern commercial novel.