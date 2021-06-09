from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # context = locals()
    context = {}
    template = 'home.html'
    return render(request, template, context)

def about(request):
    # context = locals()
    context = {}
    template = 'about.html'
    return render(request, template, context)

# Pagina protegida con login
@login_required
def userProfile(request):
    user = request.user
    context = {'user':user}
    template = 'profile.html'
    return render(request, template, context)
