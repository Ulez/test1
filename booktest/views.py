from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *
# Create your views here.
def index(request):
    context={'list':BookInfo.objects.all()}
    return render(request,'booktest/index.html',context)
def show(request,id):
    date=BookInfo.objects.get(pk=id).bpub_date
    title = BookInfo.objects.get(pk=id).btitle
    context={"title":title,'date':date}
    return render(request,'booktest/show.html',context)
