from dataclasses import dataclass, fields
from typing import Any, Dict, List, Type

from schemarquify.exceptions import (
    MissingMetaException as MissingMeta,
    MissingSerializerException as MissingSerializer,
    MissingSchemaException as MissingSchema,
)
from schemarquify.serializers import Serializer


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
            raise MissingMeta()
        return _Meta

    def __validate_meta__(self):
        if not hasattr(self._meta, "schema"):
            raise MissingSchema()

    def __populate__meta_fields__(self):
        setattr(self._meta, "fields", fields(self.schema))

    def __init__(self, **inputs):
        _meta = self.__get_meta_class__()
        if not self.serializer_class:
            raise MissingSerializer()
        self._meta = _meta()
        self.__validate_meta__()
        self.inputs = inputs
        self.schema = dataclass(self._meta.schema)(**inputs)
        self.__populate__meta_fields__()

    @property
    def cleaned_data(self) -> dict:
        if self.schema.is_valid():
            serializer = self.serializer_class
            return serializer(self).serialize()

    def how_to_store(self):
        ...

    def save(self):
        if self.schema.is_valid():
            self.how_to_store()

    def fields(self) -> List[Any]:
        return list(self._meta.fields)
