from dataclasses import dataclass, fields
from typing import Any, Dict, List, Type

from source.exceptions import (
    MissingMetaException,
    MissingSerializerException,
    MissingSchemaException,
)
from source.serializers import Serializer


class DataType:
    """DataType Base"""

    inputs: Dict[str, Any]
    serializer_class: Type[Serializer] = Serializer

    class Meta:
        schema: Any
        fields: List[Any]

    def __get_meta_class__(self) -> Type:
        _Meta = getattr(self, "Meta", None)
        if not _Meta:
            raise MissingMetaException()
        return _Meta

    def __validate_meta__(self):
        if not hasattr(self._meta, "schema"):
            raise MissingSchemaException()

    def __populate__meta_fields__(self):
        setattr(self._meta, "fields", fields(self.schema))

    def __init__(self, **inputs):
        _meta = self.__get_meta_class__()
        if not self.serializer_class:
            raise MissingSerializerException
        self._meta = _meta()
        self.__validate_meta__()
        self.inputs = inputs
        self.schema = dataclass(self._meta.schema)(**inputs)
        self.__populate__meta_fields__()

    @property
    def cleaned_data(self) -> dict:
        serializer = self.serializer_class
        return serializer(self).serialize()

    def fields(self) -> List[Any]:
        return list(self._meta.fields)
