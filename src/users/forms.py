from django import forms
from django.contrib.auth.models import User

# form for user registration
class RegistrationForm(forms.ModelForm):
  username = forms.CharField(label='User Name')
  email = forms.EmailField(label='Email Address')
  password = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
  password1  = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(render_value=False))
  
  class Meta:  
    model = User
    fields = [
      'username',
      'email',
      'password',
      'password1',
    ]

  # checks to ensure entered username is not already in db
  def clean_username(self):
    username = self.cleaned_data['username']
    try:
      User.objects.get(username=username)
    except User.DoesNotExist:
      return  username
    raise forms.ValidationError("That username is already taken.")

  # checks to ensure password and password1 fields are the same
  def clean_passwords(self):
    password = self.cleaned_data['password']
    password1 = self.cleaned_data['password1']
    if password != password1:
      raise forms.ValidationError("The passwords did not match.")
    else:
      return password


class LoginForm(forms.Form):
  username = forms.CharField(label='Username')
  password = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
  