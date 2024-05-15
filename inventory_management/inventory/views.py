from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from django import forms
from .forms import UserRegisterForm
from .models import InventoryItem

class Index(TemplateView):
	template_name = 'inventory/index.html'

class Dashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            items = InventoryItem.objects.filter(user=self.request.user.id).order_by('id')
            return render(request, 'inventory/dashboard.html', {'items': items})
        else:
            return redirect('two_factor:login')


class SignUpView(View):
	def get(self, request):
		form = UserRegisterForm()
		return render(request, 'inventory/signup.html', {'form': form})

	def post(self, request):
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			form.save()
			user = authenticate(
				username=form.cleaned_data['username'],
				password=form.cleaned_data['password1']
			)

			login(request, user)
			return redirect('index')

		return render(request, 'inventory/signup.html', {'form': form})


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':"Your username",
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':"Your password",
        'class':'w-full py-4 px-6 rounded-xl'
    }))
    
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())