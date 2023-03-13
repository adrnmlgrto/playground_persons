from django.contrib import admin
from django.urls import path, include

from ninja import NinjaAPI

from person.api import router as person_router

api = NinjaAPI()
api.add_router("/persons/", person_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('', include('person.urls')),
]
