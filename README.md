# codex-build

> Build System for Books

I've been a software engineer for 20 years and in my spare time I write novels.

The workflow for a software engineer is:

* Make changes to source code.
* Compile and test via automated systems.
* Iterate making additional changes to the source code.

For a novel writer the assumed workflow is:

* Write the whole novel.
* Format/construct the book by hand.
* publish it.

This project will be a success if it can produce a professional looking novel via automated systems instead of by hand formatting.

## Goals

See [GOALS.md](GOALS.md).

## Architecture

Likely use python/[invoke](https://www.pyinvoke.org/) to layout the and invoke the pipeline.

* Pre-processors written in python

* [Pandoc](pandoc.org) - Conversion from Markdown to AST.
  * custom python filters via [panflute](https://github.com/sergiocorreia/panflute?tab=readme-ov-file)
  * Custom python to adjust the AST if filters aren't enough (hopefully we don't have to do this)

* [Pandoc](pandoc.org) - Conversion AST to epub and typst/pdf
  * custom pandoc filters via [panflute](https://github.com/sergiocorreia/panflute?tab=readme-ov-file) again.
  * [Typst](https://github.com/typst/typst) - A layout tool hoping to supplant LaTeX built on more modern principles.
    * Whether they succeed or not is hard to say, but for a simple novel, not much is needed from the layout engine and typst seemed simpler.
    * For our purposes we should just need a custom template fed into pandoc and selecting typst as the pdf engine.

* Post processors
  * I hope this is not required.  If it is, we would need to have pandoc generate the typst and then make changes, before having typst do the compile.

## Pandoc

The pandoc in even the most recent version of ubuntu is very old.  My understanding is this has to do with maintaining compatible sets of packages written in Haskell.  My understanding is limited, because after I got to the point where I realized as of now (May 2025) I would have to (or at least want to) install my own pandoc, I moved on.

* As of May 2025 the most recent version of pandoc is 3.7
* Pandoc typst support was added in 3.1.2
* Ubuntu 24.04 LTS Includes 3.1.3
  * Technically this should be able to work, but there have been a lot of changes to the typst writer in pandoc since then, so I would recommend something more modern.
* pandoc releases/download: 
  * https://github.com/jgm/pandoc/releases


Download the deb from the above url

```
# install
DEB="/path/to/deb/pandoc-version-arch.deb
sudo dpkg -i $DEB

# verify
pandoc -v  # should show the just installed version
pandoc -D typst  # Should print out the default typst template.
```

## Typst

Typst is installable via snap.

```
sudo snap install typst
typst -V # verify
```

## UV

Python virtualenv and dependencies will be handled by [UV](https://github.com/astral-sh/uv), so a user will need to have that installed:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```


### UV Notes to Self

* [Using UV to run Self contained scripts](https://blog.dusktreader.dev/2025/03/29/self-contained-python-scripts-with-uv/)