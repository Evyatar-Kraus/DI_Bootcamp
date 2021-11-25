from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Category, Gif
from .forms import CategoryForm, GifForm

# Create your views here.
def gif(request,gif_id):
    gif = get_object_or_404(Gif,pk = gif_id)
    return render(request,'gif.html',context= {'gif':gif})

def category(request, category_id):
    category = get_object_or_404(Category,pk = category_id)
    return render(request,'category.html',context= {'category':category})

def categories(request):
    categories = get_list_or_404(Category)
    return render(request,'categories.html',context= {'categories':categories})

def new_gif(request):
    if request.method == 'POST':
        form = GifForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            categories = form.cleaned_data.pop('categories')
            gif = Gif.objects.create(**form.cleaned_data)
            gif.categories.set(categories)
            return redirect('gif_page',gif.id)
    if request.method == 'GET':
        form = GifForm()
    return render(request,'gifnew.html',{'form':form})

def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            category = Category.objects.create(category_name=form.cleaned_data.get('category_name'))
            gifs = form.cleaned_data.get('gifs')
            category.gifs.set(gifs)
            return redirect('category_page',category.id)
    if request.method == 'GET':
        form = CategoryForm()
    return render(request,'categorynew.html',{'form':form})


def like_gif(request,gif_id,like):
    liked_gif = Gif.objects.get(id=gif_id)
    liked_gif.likes += int(like)
    liked_gif.save()
    return redirect('gif_page', liked_gif.id)

def homepage(request):
    gifs = Gif.objects.all()
    return render(request,'homepage.html',context={'gifs':gifs})

def gifs_popular(request):
    print(Gif().get_liked_gifs())
    return render(request,'gifs_by_likes.html',context={'gifs':Gif.get_liked_gifs})