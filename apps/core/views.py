from django.shortcuts import render

def home(request):
    template_name ='core/home.html'
    context = {}
    return render(request, template_name, context)

