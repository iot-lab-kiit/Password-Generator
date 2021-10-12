from django.http import request
from django.shortcuts import redirect, render
from .forms import UserCreationForm, LoginForm
from .models import UserProfile
from django.views import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


class AccoutView(View):
    template_name = 'account/form.html'
    def get(self, request):
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if(form.is_valid()):
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                password = make_password(password)
            )
            user.save()
            profile = UserProfile.objects.create(
                user=user
            )
            profile.save()
            print(form.cleaned_data)
        #     user = form.save(commit=False)
        #     user.password = make_password(form.cleaned_data['password'])
        #     user.save()
        else:
            print(form.errors)

        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def profile_login(request):
    template_name = 'account/login.html'
    if request.method == "GET":         # GET METHOD
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)
    else:           # POST METHOD
        form = LoginForm(request.POST)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print('user: ', user)
                return redirect('/account/profile/')
            else:
                form = LoginForm()
                message = 'Invalid Credentials'
                context = {
                    'form': form,
                    'message': message,
                } 
                return render(request, template_name, context)  
        else:
            print(form.errors)
        
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, template_name, context)  


@login_required(login_url='/account/login/')
def profile(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    template_name = 'account/profile.html'
    context = {
        'user': profile.user.first_name,
        'previous_passwords': profile.previous_passwords
    }
    return render(request, template_name, context)

@login_required()
def profile_logout(request):
    logout(request)
    return redirect('/account/login/')