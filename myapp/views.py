from django.shortcuts import render
from . models import *

# Create your views here.
def index(request):
	return render(request,'index.html')

def single(request):
	return render(request,'single.html')

def contact(request):
	if request.method=="POST":
		Contact.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				subject=request.POST['subject'],
				message=request.POST['message']
			)
		return render(request,'index.html')
	else:
		return render(request,'index.html')