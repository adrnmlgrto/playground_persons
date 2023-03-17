from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.homepage, name='person_list_view'),
    path('create/', views.new_person, name='person_create'),
    path('p/<int:pk>/update/', views.person_update, name='person_update'),
    path('p/<int:pk>/delete/', views.person_delete, name='person_delete'),
    path('delete-all/', views.person_delete_all, name='person_delete_all'),
    path(
      'delete-all/confirm/',
      views.person_delete_all_confirm,
      name='person_delete_all_confirm'),
    path('filter/', views.search_results, name='person_filter')
]
