from sqlalchemy import Column,Integer,String
from .c_engine import Base

class structure(Base):
    __tablename__ = "Siam_computing_interns_data"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,index=True)
    mobile_no=Column(Integer,index=True)
    email_id = Column(String,index=True, unique=True)
    Linkiden_url= Column(String,index=True)

