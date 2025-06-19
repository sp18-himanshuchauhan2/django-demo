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
    context = {
        "variable": "HIMANSHU CHAUHAN"
    }
    return render(request, "first.html", context)

def about(request):
    # return HttpResponse("This is the about page of myApp!")
    return render(request, "about.html")

def service(request):
    return HttpResponse("This is the service page of myApp!")

def contact(request):
    # return HttpResponse("This is my contact details...")
    return render(request, "contact.html")
