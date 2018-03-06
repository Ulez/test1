from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
# Create your views here.
def index(request):
    context={'title':'hello5646456'}
    return render(request,'booktest/index.html',context)
