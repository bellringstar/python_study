from django.shortcuts import render

# Create your views here.

def index(request):

    context ={
                                                            
    }
    return render(request, "articles/index.html", context)
     
def page(req):

    return render(req, "articles/page.html")