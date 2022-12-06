from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Category, Image # (important) get the class of Category & Image
from .forms import CategoryForm, ImageForm
import os

def index(request):
    categories = Category.objects.all() # get all the categories
    images = Image.objects.all()        # get all the images
    ctx = {
        'categories': categories,
        'images': images,
        'title' : 'app1',
    }
    return render(request, 'index.html', ctx)

def add_category(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            cat = Category(name=name)
            cat.save()
            return redirect('index')
    ctx = {
        'form': form,
        'title' : 'Add Category',
    }
    return render(request, 'add_category.html', ctx)

def add_image(request):
    form = ImageForm() # create an empty form object
    
    if request.method == 'POST':                        
        form = ImageForm(request.POST, request.FILES)   
        if form.is_valid():                             # 
            title = form.cleaned_data['title']          # 
            category = form.cleaned_data['category']    #
            image = form.cleaned_data['image']          #
            img = Image(title=title, category=category, image=image) #
            img.save()                                  # 
            return redirect('index')                              
    ctx = {
        'form': form,
        'title' : 'Add/Upload Image',
    }
    return render(request, 'add_image.html', ctx)

def view_image(request, image_id):
    try:
        item = Image.objects.get(id=image_id)   
        ctx = {
            'img': item,
            'title' : item.title,
        }
        return render(request, 'image_view.html', ctx)
    except:
        return redirect('index')

def delete_image(request, image_id):
    try:
        item = Image.objects.get(id=image_id)   
        os.remove(item.image.path)             
        item.delete()                           
    except:
        print('Error deleting image')
    return redirect('index')