import ast
from decouple import config

from typing import List, Union
from pydantic import AnyHttpUrl, BaseSettings, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = config("PROJECT_NAME", "")
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = config("BACKEND_CORS_ORIGINS", [])
    
    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            # Return converted str representation of list to list
            return ast.literal_eval(v)
        
        raise ValueError(v)

    class Config:
        case_sensitive = True


settings = Settings()
