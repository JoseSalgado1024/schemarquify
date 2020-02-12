from schemarquify.validators import SchemaValidator
from typing import List


class Schema(SchemaValidator):
    """Tokko data schema"""

    __invalid_fields__: List[str] = []

    def validate(self):
        ret = True
        for field_name, field_def in self.__dataclass_fields__.items():
            actual_type = type(getattr(self, field_name))
            if actual_type != field_def.type:
                err_message = f"{field_name}: '{actual_type}' instead of '{field_def.type}'"
                self.__invalid_fields__.append(err_message)
            ret = False
        return ret

    def __post_init__(self):
        if not self.validate():
            raise ValueError(", ".join(self.__invalid_fields__))
