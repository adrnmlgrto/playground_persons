from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.homepage, name='person_list_view'),
    # path('create/', views.)
]
