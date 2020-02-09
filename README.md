Schemarquify
===

_Work in progress!_

> Here is my idea, what if we could write all our business strategy in python classes just for one time, and share it between frameworks?
 


**ToC**
+ [How to Install Schemarquify](#install)
+ [Usage](#usage)
    - [Create your DataSchema](#create-a-data-schema)
    - [Create your DataType](#create-a-data-type)
    - [Use it!](#validate-data)
    
# install 
```bash
(pyenv) pip install schemarquify
```

# Usage

## Create a Data Schema

```python
from source.schemas import Schema

CONTACTS = [
    {
        "first_name": "Tony",
        "last_name": "Stark",
        "surname": "IronMan"
    },
    {
        "first_name": "Bruce",
        "last_name": "Wayne",
        "surname": "Batman"},
]


class ContactSchema(Schema):
    """My Contact schema"""
    # FirstName is an Required Field
    first_name: str
    # LastName is an Required Field
    last_name: str
    # Surname is and Optional Field
    surname: str = ""

    def validate_is_marvel_superhero(self):
        super_heroes = \
            [
                "IronMan",
                "Thor",
                "Captain America",
                "SpiderMan",
                "Wolverine"
            ]
        return self.surname in super_heroes

    def validate_is_iron_man(self):
        """last_name, first_name should be Stark, Tony"""
        return f"{self.last_name}, {self.first_name}" == "Stark, Tony"
```

## Create a Data Type

```python
from source.data import DataType

class Contact(DataType):
    class Meta:
        schema = ContactSchema

    # Override this method to perform data save
    def how_to_store(self):
        with open(f"{type(self).__name__}.json".lower(), "w") as contact_file:
            contact_file.write(json.dumps(self.cleaned_data, indent=4))

```

## Validate Data
```python
for contact in CONTACTS:
    contact = Contact(**contact)
    contact.save()
```

## File `contact.json` content

```json
{
    "first_name": "Tony",
    "last_name": "Stark",
    "surname": "IronMan"
}
```