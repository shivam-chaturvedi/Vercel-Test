from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def blog_post(request):
    # Dummy data for demonstration
    post = {
        'title': 'How the IT Sector is Growing',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ...'
    }
    return render(request, 'blog_post.html', {'post': post})

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

from django.shortcuts import render
from .models import Blog

def create_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        data = request.POST.get('data')
        author = request.user  # Assuming the user is authenticated
        # Handle success or redirect to another page
        return HttpResponse("Thanks")
    else:
        # Handle GET request to render form
        return render(request, 'blog_form.html')

