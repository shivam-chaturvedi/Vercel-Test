from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog 



def home(request):
    # Fetch all blog posts from the database
    blogs = Blog.objects.all()
    
    # Pass the blogs to the template context
    return render(request, 'home.html', {'blogs': blogs})

def clear(req):
    Blog.objects.all().delete()
    return redirect("/")


def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        data = request.POST.get('data')
        
        # Create a new Blog object and save it
        new_blog = Blog(title=title, data=data)
        new_blog.save()
        
        # Optionally, you can redirect to a success page or another view
        return redirect("/")
        # return HttpResponse("Blog post created successfully!")
    else:
        # Handle GET request to render the form
        return render(request, 'blog_form.html')
