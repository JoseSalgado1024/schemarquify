from typing import List, Any, Callable
import logging


logger = logging.getLogger(__name__)


class Validator:

    add_exception_name: bool = True
    sort_validators: bool = True
    fail_safe: bool = True
    __errors__: List[str] = []

    def formatted_error_list(self) -> List[Any]:
        return self.__errors__

    @property
    def errors(self) -> List[Any]:
        return self.formatted_error_list()

    def discovery_validators(self) -> List[Callable]:
        validators = []
        validators_name_list = [m for m in dir(self) if m.startswith("validate_")]
        if self.sort_validators:
            validators_name_list = sorted(validators_name_list)
        for validator in validators_name_list:
            validator_fn = getattr(self, validator)
            if callable(validator_fn):
                validators.append(validator_fn)
        return validators

    def validate(self):
        validators = self.discovery_validators()
        for validation in validators:
            try:
                validation()
            except Exception as e:
                msg = ""
                if self.add_exception_name:
                    msg = f"{type(e).__name__}. "
                msg += f"{e}"
                self.__errors__.append(msg)

    def is_valid(self) -> bool:
        try:
            self.validate()
            return True
        except Exception as e:
            if self.fail_safe:
                logger.exception(e)
                return False
            raise e

    def __str__(self) -> str:
        return f"{type(self).__name__}. {self.__doc__}"


class SchemaValidator(Validator):
    ...
