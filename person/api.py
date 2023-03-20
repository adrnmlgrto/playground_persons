from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router, Schema
from person.models import Person
from pydantic import Field, validator

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

    @validator('f_name')
    def validate_fname(cls, value):
        # Check if the first name field contains any digits.
        # Automatically handle to remove digit in the first name.
        if any(char.isdigit() for char in value):
            value = ''.join(char for char in value if not char.isdigit())
        return value

    @validator('m_name')
    def validate_mname(cls, value):
        # Check if the middle name field contains any digits.
        # Automatically handle to remove digit in the middle name.
        if any(char.isdigit() for char in value):
            value = ''.join(char for char in value if not char.isdigit())
        return value

    @validator('l_name')
    def validate_lname(cls, value):
        # Check if the last name field contains any digits.
        # Automatically handle to remove digit in the last name.
        if any(char.isdigit() for char in value):
            value = ''.join(char for char in value if not char.isdigit())
        return value


class PersonOut(Schema):
    # Schema for get(), ... methods
    id: int
    f_name: str = Field(None, description="First Name")
    m_name: str = Field(None, description="Middle Name")
    l_name: str = Field(None, description="Last Name")
    is_male: bool = Field(None, description="Is Male")
    is_female: bool = Field(None, description="Is Female")
    other: bool = Field(None, description="Prefer not to say")


class Message(Schema):
    message: str


# Defining API Endpoints as Route (POST, GET, PUT, PATCH, DELETE)


# Create an instance of Person
@router.post("/new", response={200: PersonOut, 422: Message})
def create_person(request, payload: PersonIn):

    try:
        converted_payload = payload.dict(exclude_none=True)
        response = Person.objects.create(**converted_payload)
        person = response
    except ValidationError:
        return 422, {'message': 'Missing one or two fields. Please try again.'}

    return 200, PersonOut(
        id=person.id,
        f_name=person.f_name,
        m_name=person.m_name,
        l_name=person.l_name,
        is_male=person.is_male,
        is_female=person.is_female,
        other=person.other
    )


# Get single instance of Person
@router.get("/get/{person_id}", response=PersonOut)
def get_person(request, person_id: int):
    person = get_object_or_404(Person, id=person_id)
    return person


@router.get("/filter/{search_field}", response=list[PersonOut])
def get_persons(request, search_field: str):
    person_list = Person.objects.filter(
                Q(f_name__icontains=search_field) |
                Q(m_name__icontains=search_field) |
                Q(l_name__icontains=search_field)
            )
    return person_list


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
