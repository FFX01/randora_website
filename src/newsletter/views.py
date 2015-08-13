from django.shortcuts import render, redirect
from .models import SignUp
from .forms import SignUpForm

# Create your views here.
def home(request):
  page_title = 'Randora Newsletter Home'
  form = SignUpForm(request.POST or None)
  user = request.user

  context = {
    "form": form,
    "user": user,
    "page_title": page_title,
  }
  
  if form.is_valid():
    form.save()
    return redirect('signed_up')
  
  return render(request, 'newsletter_home.html', context)

def signed_up(request):
  user = request.user
  page_title = 'Signed Up!'
  
  context = {
    "user": user,
    "page_title": page_title,
  } 

  return render(request, 'newsletter_signed_up.html', context)
