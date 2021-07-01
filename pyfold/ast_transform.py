from typing import Union
import sys
import ast

assert sys.version_info[:2] == (3, 9), f"In {sys.version_info}, AST folds you!"


class NameFolder(ast.NodeTransformer):
    """
    AST Transformer that case-folds names
    """

    def visit_Name(self, node: ast.Name) -> ast.Name:
        node.id = node.id.casefold()
        return node

    def visit_Attribute(self, node: ast.Attribute) -> ast.Attribute:
        node.attr = node.attr.casefold()
        return node


def fold(source: Union[str, ast.AST]) -> ast.AST:
    """Convenience helper to fold an AST or source code"""
    source_ast = ast.parse(source) if isinstance(source, str) else source
    return NameFolder().visit(source_ast)
