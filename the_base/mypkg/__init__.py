__all__ = []

from . import core
__all__ += core.__all__
from . import extensions


def __update_plugins():
    import importlib
    import pkgutil
    import mypkg.extensions
    plugins = {
        name: importlib.import_module(name) for finder, name, ispkg in pkgutil.iter_modules(mypkg.extensions.__path__, mypkg.extensions.__name__+'.')
    }
    for finder, name, ispkg in pkgutil.iter_modules(mypkg.extensions.__path__, mypkg.extensions.__name__+'.'):
        setattr(extensions, name.split('mypkg.extensions.')[1], importlib.import_module(name))
    #return plugins

__update_plugins()
