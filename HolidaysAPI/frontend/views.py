from django.shortcuts import render

def index(request):
    """
    View function for the home page of the site.
    """
    return render(request, 'index.html')