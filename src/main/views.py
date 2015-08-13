from django.shortcuts import render, redirect

def home(request):
  page_title = 'Randora Home'
  user = request.user

  context = {
    "page_title": page_title,
    "user": user,
  }

  return render(request, 'main_home.html', context)

def about(request):
  page_title = 'About Randora'
  user = request.user

  context = {
    "page_title": page_title,
    "user": user,
  }

  return render(request, 'main_about.html', context)