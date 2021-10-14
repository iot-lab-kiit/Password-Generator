from django.shortcuts import redirect, render
import random
import string

MAXLENGTH = 20
MAXPASSWORDS = 15
MAX_INCLUDE_LENGTH = MAXLENGTH//2     # 10 in this case


def home(request):
	context = {
		'length_numbers': [x for x in range(6, MAXLENGTH+1)],
		'password_count_numbers': [x for x in range(1, MAXPASSWORDS+1)],
		'max_include_length': MAX_INCLUDE_LENGTH,
	}
	return render(request, 'generator/home.html', context=context)

def generate_password(passlenth, characters, include):
	password = ''
	for i in range(passlenth):
		password += random.choice(characters)
	if(include != ''):
		start = random.randrange(len(include))
		password = password[:start] + include + password[start+len(include):]
	return password



def password(request):
	alphabets = string.ascii_lowercase
	length = int(request.GET.get('length', 13))
	passcount = int(request.GET.get('passcount', 1))
	include = request.GET.get('include', "")
	

	if request.GET.get('uppercase'):
		alphabets += string.ascii_uppercase

	if request.GET.get('special'):
		alphabets += string.punctuation

	if request.GET.get('number'):
		alphabets += string.digits

	payload = []
	for i in range(passcount):
		password = generate_password(passlenth=length, characters=alphabets, include=include)
		payload.append(password)
	
	return render(request, 'generator/password.html', {'passwords': payload})
