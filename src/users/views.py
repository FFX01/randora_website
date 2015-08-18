from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from users.forms import RegistrationForm, LoginForm

# Define view for registration form
def register(request):
  page_title = "Randora User Registration"
  user = request.user
  form = RegistrationForm(request.POST or None)
  errors = []

  context = {
    "page_title": page_title,
    "user": user,
    "form": form,
    "errors": errors,
  }

  # If user is already logged in, redirect them to their profile
  if user.is_authenticated():
    return HttpResponseRedirect(reverse('profile', kwargs={'username': request.user.username}))

  # Handler for form submission and user creation
  if request.method == 'POST':
    if form.is_valid():
      user = User.objects.create_user(
        username = form.cleaned_data['username'], 
        email = form.cleaned_data['email'],
        password = form.cleaned_data['password'],
        )
      user.save()
      return HttpResponseRedirect(reverse('login'))
    else:
      errors.append("Form not valid.")
      return render_to_response(
        'users_register.html', 
        context, 
        context_instance=RequestContext(request)
      )
  else:
    return render_to_response(
      'users_register.html', 
      context, 
      context_instance=RequestContext(request)
    )


def users_login(request):
  page_title = "Randora Login"
  form = LoginForm(request.POST or None)
  errors = []

  context = {
    "page_title": page_title,
    "form": form,
    "errors": errors,
  }

  if request.user.is_authenticated():
    return HttpResponseRedirect(reverse('profile', kwargs={'username': request.user.username}))

  if request.method == 'POST':
    if form.is_valid():
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)
      if user:
        if user.is_active:
          login(request,  user)
          return HttpResponseRedirect(reverse('profile', kwargs={'username': request.user.username}))
        else:
          errors.append("Your account has been disabled.")
          return render(request, 'users_login.html', context)
      else:
        errors.append("Invalid login.")
        return render(request, 'users_login.html', context)
  else:
    return render(request, 'users_login.html', context)


def users_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('login'))


def profile(request, username):
  user = User.objects.get(username=username)
  page_title = "%s Profile" % username
  errors =[]

  context = {
    "user": user,
    "page_title": page_title,
    "errors": errors,
  }
  
  return render(request, 'users_profile.html', context)

