from django.urls import path
from . import views

urlpatterns = [
    path('gif/<int:gif_id>', views.gif, name="gif_page"),
    path('category/<int:category_id>', views.category, name="category_page"),
    path('categories', views.categories, name="categories_page"),
    path('add_gif', views.new_gif, name="new_gif_page"),
    path('add_category',views.new_category, name="new_category_page"),
    path('', views.homepage, name="homepage"),
    path('gif/<int:gif_id>/<str:like>', views.like_gif, name='like_gif'),
    path('gifs_popular/', views.gifs_popular, name='gifs_popular'),
]
