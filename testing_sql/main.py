from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from . import crud,structure_of_schema,schema
from .c_engine import sessionlocal,engine
from sqlalchemy.orm import Session

app=FastAPI()

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/',response_model=List[schema.user_details])
def inforamtion(db:Session=Depends(get_db)):
    return crud.get_employee(db)

@app.get('/{employee_id}',response_model=schema.user_details)
def informayion_of_id(employee_id:int,db:Session=Depends(get_db)):
    return crud.get_employee_by_id(db,employee_id)

@app.post('/upload',response_model=schema.user_details)
def upload_new_info(emp:schema.userinput,db:Session=Depends(get_db)):
    return crud.connect_database(db,emp)

@app.put("/employees/{emp_id}", response_model=schema.user_details)
def update(emp_id: int, emp: schema.empupdate, db: Session = Depends(get_db)):
    return crud.update_employee(db, emp_id, emp)


@app.delete("/employees/{emp_id}")
def delete(emp_id: int, db: Session = Depends(get_db)):
    crud.delete_employee(db, emp_id)
    return {"detail": "Employee deleted"}

