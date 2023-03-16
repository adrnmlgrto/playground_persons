import json
from django.http import JsonResponse
from .api import PersonIn
from django.shortcuts import render, redirect
from .api import (
    create_person,
    get_person,
    get_all_person,
    update_person,
    delete_person)


def homepage(request):
    # Use API that gets all persons in the DB using endpoint "/api/persons/all"
    persons = get_all_person(request)

    # Render the "view" template with the persons variable
    return render(request, 'person/view.html', {'persons': persons})


def new_person(request):
    # Use API that creates a person in the DB using endpoint "/api/persons/new"
    if request.method == 'POST':

        if request.POST['s_input'] == 'male':
            data = {
                "f_name": request.POST['f_name'],
                "m_name": request.POST['m_name'],
                "l_name": request.POST['l_name'],
                "is_male": "true",
            }
        elif request.POST['s_input'] == 'female':
            data = {
                "f_name": request.POST['f_name'],
                "m_name": request.POST['m_name'],
                "l_name": request.POST['l_name'],
                "is_female": "true",
            }
        elif request.POST['s_input'] == 'other':
            data = {
                "f_name": request.POST['f_name'],
                "m_name": request.POST['m_name'],
                "l_name": request.POST['l_name'],
                "other": "true",
            }

        create_person(request, PersonIn(**data))
        return redirect('person_list_view')

    else:
        return render(request, 'person/create.html')


def person_update(request, person_id):
    # Use API that creates a person in the DB using endpoint "/api/persons/update"
    update_person(request, person_id)
    pass


def person_delete(request, pk: int):
    delete_person(request, pk)
    return render(request, 'person/delete_success.html')
    # return redirect('person_list_view')
