type-hinting
============

Python 3 type-hinting introduces a way to annotate code in a way that retains
Python's dynamic typing while helping you to write more implicit documentation
and avoid type-related bugs. This becomes particularly important within larger
projects and teams, as well as refactoring, debugging, and understanding the
flow of object types through an application.

Type hinting is provided by the "typing" module, and is ignored by the
interpreter, while allowing debugging using IDEs and tools such as mypy
and pycharm.

Defined by PEP [3107](https://www.python.org/dev/peps/pep-3107/) and [484](https://www.python.org/dev/peps/pep-0484/).


example usage
-------------
Check hinting:
`mypy ./bank.py`


related tools
-------------
- [mypy](http://mypy-lang.org/)
- [mypy-tools](https://github.com/nylas/mypy-tools), mypy as a server
- [pyannotate](https://github.com/dropbox/pyannotate), runtime inspection, auto-generation and insertion of PEP-484 annotations
- [flake8-mypy](https://pypi.org/project/flake8-mypy/), An extension for flake8 linter to integrate mypy, such as in VS Code
- [pydantic](https://pydantic-docs.helpmanual.io/), data validation library