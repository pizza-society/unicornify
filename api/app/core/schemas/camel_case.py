from humps import camelize
from pydantic import BaseModel


def to_camel_case(string):
    """ convert snake_case to camelCase """

    return camelize(string)


class CamelModel(BaseModel):
    """ Base model with snake_case to camelCase conversion """

    class Config:
        alias_generator = to_camel_case
        allow_population_by_field_name = True
