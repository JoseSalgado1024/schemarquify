from typing import Any, List, Type, Dict


class Serializer:
    __data__: Any

    acceptable_json_fields: List[Type] = [str, float, int, dict, list]

    def __init__(self, data_instance: Any, **extra):
        self.__omitted_fields__ = extra.get("omitted_fields", [])
        self.__data__ = data_instance

    def serialize(self) -> Dict[str, Any]:
        serialized_data = {}
        for field in self.__data__.fields():
            _f_name = field.name
            value = getattr(self.__data__.schema, _f_name)
            serialized_data.update({_f_name: value})
        return serialized_data
