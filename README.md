# sphinx-matlabdoc-builder

[![Build Status](https://travis-ci.org/ilent2/sphinx-matlabdoc-builder.svg?branch=master)](https://travis-ci.org/ilent2/sphinx-matlabdoc-builder)

A Sphinx extension for generating Matlab HTML docs.
This extension builds the Sphinx project into a set of HTML
documents and additionally generates the TOC `helptoc.xml` file
required for the
[Matlab toolbox documentation](https://au.mathworks.com/help/matlab/matlab_prog/display-custom-documentation.html)

For generating documentation for Matlab code, check out the
[matlabdomain](https://github.com/sphinx-contrib/matlabdomain) Sphinx extension.

## Installation

The package can be installed using [Pip](https://pypi.org/project/sphinx-matlabdoc-builder/)

```bash
pip install sphinx-matlabdoc-builder
```

Alternatively you can download the `sphinx_matlabdoc_builder` package into your
sphinx directory and add the local directory to the sphinx path.

## Requirements
This package is an extension to Sphinx.
Requires Python 3.

## Usage

To use sphinx-matlabdoc-builder, you must first install the package and add
the extension to your sphinx `conf.py` file.  For example, add the
`sphinx_matlabdoc_builder` extension to the end of your extension list:

```python
extensions = [
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
    'sphinx_matlabdoc_builder',
]
```

Then compile the source with

```bash
make matlabdoc
```

or if using `sphinx-build`

```
sphinx-build -M matlabdoc ./ build
```

this should generate the normal HTML output and add the `helptoc.xml`
file to the output directory.

To use the `helptoc.xml` file in your toolbox, create a new matlab
package and click add documentation and specify the documentation
output directory.
If you have an existing `info.xml` file, simply change the documentation
directory to point to the output directory containing the `helptoc.xml` file.
