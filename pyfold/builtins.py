import builtins
from .ast_transform import fold


def exec(source: str, *globals_locals) -> None:
    """
    Dynamically execute the Pyfold code in `source`
    """
    assert (
        len(globals_locals) <= 2
    ), f"expected [globals [, locals]], got {len(globals_locals)}"
    code = compile(
        fold(source), filename="<exec string>", mode="exec"
    )
    builtins.exec(code, *globals_locals)
