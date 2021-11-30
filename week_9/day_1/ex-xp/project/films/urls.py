from django.urls import path
from .views import FilmListView, FilmCreateView, DirectorCreateView, CountryCreateView, CategoryCreateView

app_name = "films"

urlpatterns = [
    path('homepage', FilmListView.as_view(), name="homepage"),
    path('addDirector', DirectorCreateView.as_view(), name="add_director"),
    path('addFilm', FilmCreateView.as_view(), name="add_film"),
    path('addCountry', CountryCreateView.as_view(), name="add_country"),
    path('addCategory', CategoryCreateView.as_view(), name="add_category"),

]
