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
            for cat in categories:
                cat.gifs.add(gif)
                print(cat.gifs.all())
            return redirect('gif_page',gif.id)
    if request.method == 'GET':
        form = GifForm()
    return render(request,'gifnew.html',{'form':form})

def new_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            print(form.cleaned_data)
            category = Category.objects.create(category_name=form.cleaned_data.get('category_name'))
            # category.gifs = (form.cleaned_data.get('gifs'))
            gifs = form.cleaned_data.get('gifs')
            for gif in gifs:
                gif.categories.add(category)
                print(gif.categories.all())
            return redirect('category_page',category.id)
    if request.method == 'GET':
        form = CategoryForm()
    return render(request,'categorynew.html',{'form':form})


def homepage(request):
    gifs = Gif.objects.all()
    return render(request,'homepage.html',context={'gifs':gifs})