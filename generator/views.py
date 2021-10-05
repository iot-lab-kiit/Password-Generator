from django.shortcuts import render
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	
	alphabets = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length', 13))
	finalpass = ''

	if request.GET.get('uppercase'):
		alphabets.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		alphabets.extend(list('~!@#$%^&*()_+=-./?<>:|\[];'))

	if request.GET.get('number'):
		alphabets.extend(list('0123456789'))

	for i in range(length):
		finalpass += random.choice(alphabets)
	
	return render(request, 'generator/password.html', {'password': finalpass})
