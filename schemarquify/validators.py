from typing import Dict, List, Any, Callable, Union
import logging

from schemarquify.exceptions import ValidationErrorException as ValidationError


logger = logging.getLogger(__name__)


ValidatorListType = List[Dict[str, Union[Callable, str]]]


class Validator:
    add_more_info: bool = False
    add_exception_name: bool = False
    sort_validators: bool = True
    fail_safe: bool = True
    __errors__: List[str] = []

    def formatted_error_list(self) -> List[Any]:
        return self.__errors__

    @property
    def errors(self) -> List[Any]:
        return self.formatted_error_list()

    def discovery_validators(self) -> ValidatorListType:
        validators = []
        validators_name_list = [m for m in dir(self) if m.startswith("validate_")]
        if self.sort_validators:
            validators_name_list = sorted(validators_name_list)
        for validator in validators_name_list:
            validator_fn = getattr(self, validator)
            if callable(validator_fn):
                validators.append(
                    {
                        "fn": validator_fn,
                        "name": validator.replace("resolve_", ""),
                        "description": validator_fn.__doc__ or "- ",
                    }
                )
        return validators

    def perform_validations(self):
        validators = self.discovery_validators()
        for validation in validators:
            fn = validation["fn"]
            name = validation["name"]
            desc = validation["description"]
            try:
                result = fn()
                if not result:
                    raise ValidationError(f'Result: "{result}".')
            except Exception as e:
                msg = ""
                if self.add_exception_name:
                    msg = f"{type(e).__name__}. "
                msg += f'Validation "{name}" fails. {e}'
                if self.add_more_info:
                    msg += f"\nMore info: {desc}."
                self.__errors__.append(msg)

    def is_valid(self) -> bool:
        try:
            self.perform_validations()
            if len(self.errors) > 0:
                raise ValidationError(", ".join([f"{error}" for error in self.errors]))
            return True
        except Exception as e:
            if self.fail_safe:
                return False
            raise e

    def __str__(self) -> str:
        return f"{type(self).__name__}. {self.__doc__}"


class SchemaValidator(Validator):
    ...
