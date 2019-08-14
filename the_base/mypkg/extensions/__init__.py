__path__ = __import__('pkgutil').extend_path(__path__, __name__)

#import importlib
#import pkgutil
#
#import mypkg.extensions
#
#def iter_namespace(ns_pkg):
#  return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")
#
#myapp_plugins = {
#  name: importlib.import_module(name) for finder, name, ispkg in iter_namespace(mypkg.extensions)
#}
