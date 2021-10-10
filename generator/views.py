from django.shortcuts import render
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	
	alphabets = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length', 13))
	passcount = int(request.GET.get('passcount', 1))

	if request.GET.get('uppercase'):
		alphabets.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		alphabets.extend(list('~!@#$%^&*()_+=-./?<>:|\[];'))

	if request.GET.get('number'):
		alphabets.extend(list('0123456789'))
	
	def generate(chars,length):
		finalpass = ''
		for i in range(length):
			finalpass += random.choice(chars)
		return finalpass

	payload = [generate(alphabets,length) for i in range(passcount)]	
		
	return render(request, 'generator/password.html', {'passwords': payload})