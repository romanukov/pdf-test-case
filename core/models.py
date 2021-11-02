from pydantic import BaseModel


class CustomerData(BaseModel):
    name: str
    surname: str
    company_name: str
