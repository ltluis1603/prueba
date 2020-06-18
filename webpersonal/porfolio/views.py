from django.shortcuts import render
from porfolio.models import Project

# Create your views here.
def portfolio(request):
     projects= Project.objects.all()
     return render(request, "porfolio/portfolio.html", {'projects':projects})