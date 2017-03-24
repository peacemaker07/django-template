from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
	class Meta:
		model = CustomUser
		fields = (
			"username", "email", "password1", "password2",
			"last_name", "first_name", "section", "position",
		)
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'ユーザ名'
		
		self.fields['email'].widget.attrs['class'] = 'form-control'
		self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'
		
		self.fields['last_name'].widget.attrs['class'] = 'form-control'
		self.fields['last_name'].widget.attrs['placeholder'] = '姓'
		
		self.fields['first_name'].widget.attrs['class'] = 'form-control'
		self.fields['first_name'].widget.attrs['placeholder'] = '名'
		
		self.fields['section'].widget.attrs['class'] = 'form-control'
		self.fields['section'].widget.attrs['placeholder'] = 'セクション'
		
		self.fields['position'].widget.attrs['class'] = 'form-control'
		self.fields['position'].widget.attrs['placeholder'] = '役職'
		
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'
		
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'パスワード（確認）'
