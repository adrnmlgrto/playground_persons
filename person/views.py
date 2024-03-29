from django.shortcuts import redirect, render

from .api import (PersonIn, create_person, delete_all, delete_person,
                  get_all_person, get_person, get_persons, update_person)


def homepage(request):
    # Use API that gets all persons in the DB using endpoint "/api/persons/all"
    persons = get_all_person(request)

    # Render the "view" template with the persons variable
    return render(request, 'person/view.html', {'persons': persons})


def redirect_view(request):
    # Redirect to Homepage if no URL body
    return redirect('person_list_view')


def search_results(request):
    if request.GET.get('search_field'):
        persons_found = get_persons(request, request.GET.get('search_field'))
        print(persons_found)
        return render(request,
                      'person/filtered_list.html',
                      {'persons': persons_found})
    else:
        return redirect('person_list_view')


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


def person_update(request, pk: int):
    # Use API that creates a person in the
    # DB using endpoint "/api/persons/update"

    if request.method == 'POST':

        if request.POST['s_input'] == 'male':
            data = {
                "f_name": request.POST['f_name'],
                "m_name": request.POST['m_name'],
                "l_name": request.POST['l_name'],
                "is_male": "true",
                "is_female": "false",
                "other": "false"
            }
        elif request.POST['s_input'] == 'female':
            data = {
                "f_name": request.POST['f_name'],
                "m_name": request.POST['m_name'],
                "l_name": request.POST['l_name'],
                "is_female": "true",
                "is_male": "false",
                "other": "false"
            }
        elif request.POST['s_input'] == 'other':
            data = {
                "f_name": request.POST['f_name'],
                "m_name": request.POST['m_name'],
                "l_name": request.POST['l_name'],
                "other": "true",
                "is_male": "false",
                "is_female": "false"
            }

        update_person(request, pk, PersonIn(**data))
        return redirect('person_list_view')

    else:
        person = get_person(request, pk)
        return render(request, 'person/update.html', {'person': person})


def person_delete(request, pk: int):
    delete_person(request, pk)
    return render(request, 'person/delete_success.html')


def person_delete_all(request):
    return render(request, 'person/delete_confirmation.html')


def person_delete_all_confirm(request):
    delete_all(request)
    return redirect('person_list_view')
