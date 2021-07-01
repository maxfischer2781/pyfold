from typing import Union
import sys
import ast

assert sys.version_info[:2] == (3, 9), f"In {sys.version_info}, AST folds you!"


def fold(source: Union[str, ast.AST]) -> ast.AST:
    """Convenience helper to fold an AST or source code"""
    source_ast = ast.parse(source) if isinstance(source, str) else source
    for node in ast.walk(source_ast):
        if isinstance(node, ast.Name):
            node.id = node.id.casefold()
        elif isinstance(node, ast.Attribute):
            node.attr = node.attr.casefold()
        elif isinstance(node, (ast.ClassDef, ast.FunctionDef)):
            node.name = node.name.casefold()
    return source_ast
