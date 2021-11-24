from django.urls import path
from . import views

urlpatterns = [
    path('persons/<str:input_param>',views.person_by_name_or_phone, name='person_by_name_or_phone_page'),
]