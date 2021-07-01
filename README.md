# pyfold

Demonstrator for case-insensitive execution of Python source code.

* [x] Dynamically "fold-execute" code via ``exec``
* [ ] Import "fold-modules" via ``.pyf``

-------------------------

```python3
from pyfold.builtins import exec as fexec
pyf_code = """
a = "Hello World!"
print(A)
"""
fexec(pyf_code)
```
