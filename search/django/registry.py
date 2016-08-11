class RegisterError(Exception):
    pass


class __Registry(dict):
    """Registry for model -> document class mappings. Raises an error if a model
    tries to be registered twice.
    """
    def __setitem__(self, model_class, document_class):
        cls = self.setdefault(model_class, document_class)
        if cls != document_class:
            raise RegisterError(
                u'Cannot register {} for model {} already registered to'
                u' {}'.format(document_class, model_class, cls)
            )


registry = __Registry()