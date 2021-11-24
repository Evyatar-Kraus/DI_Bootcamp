from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
import re
from .models import Person
# Create your views here.


def person_by_name_or_phone(request,input_param):
    #check if input is name or phone number
    phone_regex = re.compile('((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))')
    name_regex = re.compile('^[a-zA-Z]{4,}(?: [a-zA-Z]+){0,2}$')
    print(input_param)
    if bool(re.search(phone_regex,input_param)):
        print('phone')
        person = Person.objects.filter(phone_num = input_param).first()
        return render(request,'person.html',context= {'person':person,'found':'phone'})
    elif bool(re.search(name_regex,input_param)):
        print('name')
        person = Person.objects.filter(name = input_param).first()
        return render(request,'person.html',context= {'person':person,'found':'name'})
    else:
        return HttpResponseNotFound("404 - not found - no such person")
