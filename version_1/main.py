from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    RollNo: Union[int, str]
    Depart: str
    uni: str


students = []


# get all students
@app.get("/students")
async def all_students():
    if students:
        return {"all students": students}
    else:
        return {"Empty List"}


# get single students
@app.get("/students/{students_id}")
async def get_students(students_id: int):
    for student in students:
        if student.id == students_id:
            return {"student": student}
    return {"Message": "students is not found"}


# create student id
@app.post("/students")
async def create_students(student: Item):
    students.append(student)
    return {"Message": "student has been added"}


# delete student id
@app.delete("/students/{students_id}")
async def delete_students(students_id: int):
    for student in students:
        if student.id == students_id:
            students.remove(student)
            return {"Message": "Student has been deleted"}
    return {"Message": "students is not found"}


@app.put("/students/{students_id}")
async def update_student(students_id: int, student_obj: Item):
    for student in students:
        if students_id == student.id:
            student.name = student_obj.name
            student.RollNo = student_obj.RollNo
            student.Depart = student_obj.Depart
            student.uni = student_obj.uni
            return {"Message": "Record has been updated"}
    return {"Message": "No record found"}


# wildlife tracking
# v1: wildlife tracking using fastapi and for data storage , we will use dictionary
# v2: wildlife tracking using fastapi and postgresql database for data storage
# v3: wildlife tracking using fastapi for backend and postgresql for database and streamlit for frontend
