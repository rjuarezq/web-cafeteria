from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts })

def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    
    #Establecemos el id de la categoria
    category = get_object_or_404(Category, id=category_id)
    #Mostramos los posts que pertenecen a dicha categoria seleccionada
    #posts = Post.objects.filter(categories = category)
    
    #return render(request, 'blog/category.html', {'category':category, 'posts': posts } )
    return render(request, 'blog/category.html', {'category':category})
                                                    