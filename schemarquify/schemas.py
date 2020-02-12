from schemarquify.validators import SchemaValidator
from dataclasses import is_dataclass
from typing import List


class Schema(SchemaValidator):
    """Tokko data schema"""

    __invalid_fields__: List[str] = []

    def enforce_types(self):
        if not is_dataclass(self):
            raise TypeError("Incompatible instance")
        for field_name, field_def in self.__dataclass_fields__.items():
            actual_type = type(getattr(self, field_name))
            if actual_type != field_def.type:
                atn = actual_type.__name__.capitalize()
                rt = field_def.type.__name__.capitalize()
                err_message = f"+ {field_name} argument should be an {rt} instance, got {atn}."
                self.__invalid_fields__.append(err_message)
        return len(self.__invalid_fields__) == 0

    def __post_init__(self):
        if not self.enforce_types():
            err_list_as_str = "\n".join(self.__invalid_fields__)
            err_message = f"Types Validation Error.\n{err_list_as_str}"
            raise ValueError(err_message)
