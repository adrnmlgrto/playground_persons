from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from person.models import Person

router = Router()


# Defining Schemas (Models for Django-Ninja)
class PersonIn(Schema):
    # Schema for post() method
    f_name: str
    m_name: str
    l_name: str


class PersonOut(Schema):
    # Schema for get(), ... methods
    id: int
    f_name: str
    m_name: str
    l_name: str

# Defining API Endpoints as Route (POST, GET, PUT, PATCH, DELETE)


# Create an instance of Person
@router.post("/new")
def create_person(request, payload: PersonIn):
    person = Person.objects.create(**payload.dict())
    return {
        "id": person.id,
        "f_name": person.f_name,
        "m_name": person.m_name,
        "l_name": person.l_name
        }


# Get single instance of Person
@router.get("/get/{person_id}", response=PersonOut)
def get_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    return person


# Get all Person Objects as List
@router.get("/all", response=list[PersonOut])
def get_all_person(request):
    person_list = Person.objects.all()
    return person_list


# Update Person Object
@router.put("/update/{person_id}")
def update_person(request, person_id: int, payload: PersonIn):
    person = get_object_or_404(Person, id=person_id)
    for attr, value in payload.dict().items():
        setattr(person, attr, value)
    person.save()
    return {"success": True}


# Delete single instance of Person
@router.delete("/delete/{person_id}")
def delete_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    person.delete()
    return {"success": True}
