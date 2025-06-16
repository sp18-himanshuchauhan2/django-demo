from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    """
    Render the index page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: Rendered index page.
    """
    # return HttpResponse("Hello, this is the index page of myApp!")
    return render(request, "index.html")

def about(request):
    return HttpResponse("This is the about page of myApp!")
