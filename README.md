Schemarquify
===

Work in progress!

```python
from source.data import DataType
from source.schemas import Schema


class ContactSchema(Schema):
    # Required String field
    first_name: str
    # Optional String field. Default = ""
    last_name: str = ""


class Contact(DataType):
    class Meta:
        schema = ContactSchema


input_data = {"first_name": "Tony", "last_name": "Stark"}
contact = Contact(**input_data)
assert contact.cleaned_data, input_data
```