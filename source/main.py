import json

from source.data import DataType
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
        super_heroes = ["IronMan", "Thor", "Captain America", "SpiderMan", "Wolverine"]
        return self.surname in super_heroes

    def validate_is_iron_man(self):
        """last_name, first_name should be Stark, Tony"""
        return f"{self.last_name}, {self.first_name}" == "Stark, Tony"


class Contact(DataType):
    class Meta:
        schema = ContactSchema

    # Override this method to perform data save
    def how_to_store(self):
        with open(f"{type(self).__name__}.json".lower(), "w") as contact_file:
            contact_file.write(json.dumps(self.cleaned_data, indent=4))


for contact in CONTACTS:
    contact = Contact(**contact)
    contact.save()
