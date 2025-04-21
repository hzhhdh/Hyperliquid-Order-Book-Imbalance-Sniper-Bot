from typing import Type
import importlib

class PluginLoaderStrategy:
    """
    Dynamically loads new strategy plugins
    from a plugins directory at runtime.
    """
    def load(self, module_name: str, class_name: str) -> Type:
        module = importlib.import_module(module_name)
        return getattr(module, class_name)
