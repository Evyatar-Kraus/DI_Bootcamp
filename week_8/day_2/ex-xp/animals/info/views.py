from django.http.response import HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from info.models import Animal, Family

# Create your views here.
def homepage(request):
    return HttpResponse("Hello world")

def animal(request,animal_id):
    # animal = Animal.objects.filter(id=animal_id).first()
    animal = get_object_or_404(Animal,pk=animal_id)
    return render(request,"pages/animal.html",context={"animal":animal})

def animals(request):
    animals = get_list_or_404(Animal)
    return render(request,"pages/animals.html",context={"animals":animals})

def family(request,family_id):
    family = get_object_or_404(Family,pk=family_id)
    family_animals = get_list_or_404(Animal, family=family)

    return render(request,"pages/family.html",context={"family":{
        'name':family,
        'animals':family_animals
    }})
