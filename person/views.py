from django.shortcuts import render, redirect
from .api import (
    create_person,
    get_person,
    get_all_person,
    update_person,
    delete_person)


def homepage(request):
    # Use API that gets all persons in the DB using endpoint "/api/persons/all"
    persons = get_all_person()

    # Render the "view" template with the persons variable
    return render(request, 'view.html', {'persons': persons})


def new_person(request):
    # Use API that creates a person in the DB using endpoint "/api/persons/new"
    if request.method == 'POST':
        create_person(request)
        return redirect('view')
    else:
        return render(request, 'create.html')


def person_update(request, person_id):
    # Use API that creates a person in the DB using endpoint "/api/persons/update"
    update_person(request, person_id)
    pass


def person_delete(request):
    pass
