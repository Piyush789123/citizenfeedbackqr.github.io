from django import forms
from captcha.fields import CaptchaField

class MyLoginForm(forms.Form):
   captcha=CaptchaField()