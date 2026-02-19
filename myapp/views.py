from django.shortcuts import render

# Create your views here.

def index(request):
    context={"mensaje":"Bienvenidos a aplicacion Django"}
    return render(request,"myapp/index.html", context) #Se ubica desde templates, y luego se debe poner la ubicacion del archivo