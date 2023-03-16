from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='person_list_view'),
    path('create/', views.new_person, name='person_create'),
    path('<int:pk>/update/', views.person_update, name='person_update'),
    path('<int:pk>/delete/', views.person_delete, name='person_delete'),
]
