from django.shortcuts import render
from django.db.models import Sum


def dashboard(request):
   

    context = {
       
    }
    return render(request, 'dashboard.html', context)
