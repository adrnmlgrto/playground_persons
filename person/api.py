from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from person.models import Person
from pydantic import Field

router = Router()


# Defining Schemas (Models for Django-Ninja)
class PersonIn(Schema):
    # Schema for post() method
    f_name: str = Field(..., description="First Name")
    m_name: str = Field(None, description="Middle Name")
    l_name: str = Field(..., description="Last Name")
    is_male: bool = Field(None, description="Is Male")
    is_female: bool = Field(None, description="Is Female")
    other: bool = Field(None, description="Prefer not to say")


class PersonOut(Schema):
    # Schema for get(), ... methods
    id: int
    f_name: str = Field(None, description="First Name")
    m_name: str = Field(None, description="Middle Name")
    l_name: str = Field(None, description="Last Name")
    is_male: bool = Field(None, description="Is Male")
    is_female: bool = Field(None, description="Is Female")
    other: bool = Field(None, description="Prefer not to say")

# Defining API Endpoints as Route (POST, GET, PUT, PATCH, DELETE)


# Create an instance of Person
@router.post("/new")
def create_person(request, payload: PersonIn):
    person = Person.objects.create(**payload.dict(exclude_none=True))
    return {
        "message": f'User <{person.f_name} {person.l_name}> has been created.'
        }


# Get single instance of Person
@router.get("/get/{person_id}", response=PersonOut)
def get_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    return person


# @router.get("/filter", response=list[PersonOut])
# def get_persons(request, **kwargs):
#     person_list = Person.objects.filter(**kwargs)
#     return person_list


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


@router.delete("/delete-all")
def delete_all(request):
    if Person.objects.all().exists():
        Person.objects.all().delete()
        return {
            "message": "Deleted all persons in the Database"
        }
    else:
        return {
            "message": "No persons found in the database"
        }
