from pydantic import BaseModel
from typing import Optional
class userinput(BaseModel):
    name: str
    mobile_no:int
    email_id: str
    Linkiden_url: str

class empupdate(BaseModel):
    name: Optional[str] = None
    mobile_no: Optional[int] = None
    email_id: Optional[str] = None
    Linkiden_url: Optional[str] = None

class user_details(userinput):
    id:int

    class Config:
        orm_mode=True



