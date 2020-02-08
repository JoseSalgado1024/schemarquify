class CustomBaseException(Exception):
    """Custom Base Exception"""

    def __init__(self, *args, **kwargs):
        mgs = self.__doc__
        spacer = ". "
        if args:
            mgs += spacer + ", ".join([f"{arg}" for arg in args])
        if kwargs:
            mgs += spacer + ", ".join([f"{k}={v}" for k, v in kwargs.items()])
        super().__init__(mgs)


class MissingMetaException(CustomBaseException):
    """Missing DataType Meta-class."""


class MissingSerializerException(CustomBaseException):
    """Missing DataTypeSerializer class."""


class MissingSchemaException(CustomBaseException):
    """Missing DataTypeSchema class."""

