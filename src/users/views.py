from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from users.forms import RegistrationForm

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
  if request.user.is_authenticated():
    return HttpResponseRedirect('profile/')

  # Handler for form submission and user creation
  if request.method == 'POST':
    if form.is_valid():
      user = User.objects.create_user(
        username = form.cleaned_data['username'], 
        email = form.cleaned_data['email'],
        password = form.cleaned_data['password'],
        )
      user.save()
      return HttpResponseRedirect('profile/')
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


def login(request):
  context = {}
  context.update(csrf(request))
  return render_to_response('users_login.html', context)



def logout(request):
  return render(request, 'users_logout.html')


def profile(request):
  return render(request, 'users_profile.html')

