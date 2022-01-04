from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Training

'''def home(request):
	return HttpResponse("<h1>Ushur Homepage</h1>")'''

def home(request):
	return render(request,'index.html')

def train(request):
	train = Training.objects.all()
	return render(request,'train.html',{'train':train})
