import os
import sys
import importlib.machinery

from .ast_transform import fold


class PyfoldFileLoader(importlib.machinery.SourceFileLoader):
    """
    Hook to load a Pyfold module
    """

    @staticmethod
    def source_to_code(data, path='<string>'):
        """Compile 'data' into a code object.

        The 'data' argument can be anything that compile() can handle. The'path'
        argument should be where the data was retrieved (when applicable)."""
        return compile(fold(data.decode()), path, 'exec', dont_inherit=True)


class PyfoldPathFinder(importlib.machinery.PathFinder):
    """
    PathFinder to find PyfoldFileLoader for Pyfold modules in ``sys.path``
    """
    importer_cache = {}
    file_finder = importlib.machinery.FileFinder.path_hook((PyfoldFileLoader, [".pyf"]))

    @classmethod
    def invalidate_caches(cls):
        for finder in cls.importer_cache.values():
            if hasattr(finder, 'invalidate_caches'):
                finder.invalidate_caches()

    @classmethod
    def _path_hooks(cls, path):
        """Search try to create a finder for 'path'."""
        try:
            return cls.file_finder(path)
        except ImportError:
            return None

    @classmethod
    def _path_importer_cache(cls, path):
        if path == '':
            try:
                path = os.getcwd()
            except FileNotFoundError:
                return None
        try:
            finder = cls.importer_cache[path]
        except KeyError:
            finder = cls.importer_cache[path] = cls._path_hooks(path)
        return finder


sys.meta_path.append(PyfoldPathFinder)
