from django.urls.base import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.messages.views import SuccessMessageMixin

from .models import Category, Film ,Director  ,Country,Category
from .forms import AddDirectorForm, AddFilmForm, AddCategoryForm , AddCountryForm

# Create your views here.


class FilmListView(ListView):
    queryset = Film.objects.all().order_by('-release_date')
    # model = Film
    context_object_name = 'movies'
    paginate_by = 12
    template_name = 'homepage.html'



class DirectorCreateView(CreateView):
    model = Director
    fields = '__all__'
    form_class = AddDirectorForm
    template_name = 'director/addDirector.html'
    success_url = reverse_lazy('films:add_director')
    success_message = "%(title)s was created successfully"



class FilmCreateView(CreateView):
    model = Film
    fields = '__all__'
    form_class = AddFilmForm
    template_name = 'film/addFilm.html'
    success_url = reverse_lazy('films:add_film')
    success_message = "%(first_name)s %(last_name)s was created successfully"

class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'category/addCategory.html'
    success_url = reverse_lazy('films:add_category')
    success_message = "%(name)s was created successfully"
    fields = '__all__'

class CountryCreateView( SuccessMessageMixin, CreateView):
    model = Country
    form_class = AddCountryForm
    template_name = 'country/addCountry.html'
    success_url = reverse_lazy('films:add_country')
    success_message = "%(name)s was created successfully"
    fields = '__all__'
