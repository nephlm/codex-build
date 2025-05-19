# Config

Each novel is defined by a config file.  This is where the contents and customizations are laid out.  

Each config file is a JSON, YAML of Markdown (with metadata block) file.

The root config file, the one passed to the command, may contain a `metadata-files` key which may have a value of a path to another config file or a list of paths to other config files.  These files are read and incorporated into the metadata used by the build system.

Having a `metadata-files` key in non-root config files is an undefined behavior, and may change at any time without warning.  Don't do it.  

## Basic Config

```
title: Working Title
author: Nephlm
content:
    - ~/path/to/manuscript
output-dir: ~/path/to/output
```

At its simplest all the build systems really needs to build a book is a path to where the content files are, and where to put the compiled book.  Almost everyone is also going to want a `title` and `author` as well.

`content` is a list of files or directories containing Markdown files that are concatenated together to produce the raw manuscript in Markdown format.  Any directories are recursively scanned for Markdown files and the directory is replaced with that list sorted in lexicographic order (including full path).

`output-dir` is where the produced `epub` and `pdf` are placed.

`title` and `author` should be self-explanatory.  They are not used by the build system, but by the underlying Pandoc templates to produce title pages and such.  

## Sections / Acts / Books

If your book is broken up into larger sections that contain multiple chapters then you'll want to add: 

```
chapter-heading-level: 2
```

By default, this set to 1, and all top level headings are assumed to be chapters.  This will make second level headings chapters and first level headings will section dividers, that are usually presented on a page of their own.

```
# Act I

## Chapter 1

...

## Chapter 2

...

Act II

## Chapter 24

...
```

## Front Matter

Front matter are things like title page, copyright page, introduction, acknowledgement, forward, etc.

```
front-matter: 
    - title-page
    - copyright-page
    - introduction.md
    - acknowledgements.md
    - half-title
```

By default, a title page and copyright page is appended to th front if they are not added manually by the user.  The values `title-page`, `copyright-page` and `half-title` are special values that will insert those things at the appropriate places using values from the metadata. 

`epigraphs`, `accolades` and `also-by` are not yet supported, but may likely be added later.

Anything other than one of the special values needs to be a path to a Markdown file that will be rendered as expected for a introduction or acknowledgement.  A header followed by the text.  The heading should be in the chapter level.

## Back Matter

Exactly the same as `front-matter`, but appears after the content.

```
back-matter:
    - author-note.md
```

The same special values also apply, though some of them make less sense in back matter.