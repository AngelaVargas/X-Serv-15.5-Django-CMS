from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages

# Create your views here.

def index(request, peticion):
	print(peticion)
	try:
		Request = Pages.objects.get(name=peticion)
	except Pages.DoesNotExist:
		return HttpResponse('Page Not Found')

	Response = "Hello, I'm " + Request.name + " : " + str(Request.page)

	return HttpResponse(Response)
