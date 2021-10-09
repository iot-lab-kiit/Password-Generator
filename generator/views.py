from django.shortcuts import render
import random

# Create your views here.
def home(request):
	return render(request, 'generator/home.html')

def password(request):
	
	alphabets = list('abcdefghijklmnopqrstuvwxyz')
	length = int(request.GET.get('length', 13))
	number = int(request.GET.get('number', 1))
    
	passwords = []

	if request.GET.get('uppercase'):
		alphabets.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

	if request.GET.get('special'):
		alphabets.extend(list('~!@#$%^&*()_+=-./?<>:|\[];'))

	if request.GET.get('number'):
		alphabets.extend(list('0123456789'))
    

	for j in range(number):
         finalpass = ''
         for i in range(length):
	         finalpass += random.choice(alphabets)
         passwords.append(finalpass)
        
	print(passwords)	
	return render(request, 'generator/password.html',{'passwords': passwords})
