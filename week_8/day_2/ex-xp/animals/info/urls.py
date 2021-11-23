from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('animal/<int:animal_id>',views.animal, name="animal"),
    path('family/<int:family_id>',views.family),
    path('animals/',views.animals)
]