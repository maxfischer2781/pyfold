# pyfold

Demonstrator for case-insensitive execution of Python source code.

* [x] Dynamically "fold-execute" code via ``exec``

    ```python3
    from pyfold.builtins import exec as fexec
    pyf_code = """
    a = "Hello World!"
    print(A)
    """
    fexec(pyf_code)
    ```

* [x] Import "fold-modules" via ``.pyf``

    ```bash
    cat sample.pyf
    python3 -c "
    import pyfold.imports
    import sample
    "
    ```
