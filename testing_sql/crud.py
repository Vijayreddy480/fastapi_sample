from fastapi import FastAPI,HTTPException
from sqlalchemy.orm import Session
from .c_engine import sessionlocal
from .structure_of_schema import structure
from .schema import userinput,user_details,empupdate
from pydantic import BaseModel




def connect_database(db:Session,connection:userinput):
    db_user=structure(name=connection.name,mobile_no=connection.mobile_no,email_id=connection.email_id,Linkiden_url=connection.Linkiden_url)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
#crud operations
def get_employee(db:Session):
    employee_data=db.query(structure).all()
    if employee_data:
        return employee_data
    else:
        raise HTTPException(status_code=404, detail="employee not found")
def get_employee_by_id(db:Session,emp_id:int):
    employee=db.query(structure).filter(structure.id==emp_id).first()
    if employee:
        return employee
    else:
        raise HTTPException(status_code=404, detail="employee not found")

def update_employee(db:Session,emp_id:int,emp:empupdate):
    emp_details=get_employee_by_id(db,emp_id)
    if emp.name is not None:
        emp_details.name = emp.name
    if emp.mobile_no is not None:
        emp_details.mobile_no = emp.mobile_no
    if emp.email_id is not None:
        emp_details.email_id = emp.email_id
    if emp.Linkiden_url is not None:
        emp_details.Linkiden_url = emp.Linkiden_url
    db.commit()
    db.refresh(emp_details)
    return emp_details
def delete_employee(db: Session, emp_id: int):
    emp = get_employee_by_id(db, emp_id)
    if emp:
        db.delete(emp)
        db.commit()
    return emp

    