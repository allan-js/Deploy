from django.contrib import messages
from django.http import HttpResponse
from django.db.models.query_utils import Q
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.shortcuts import  render, redirect
from django.contrib.auth.views import LoginView
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.tokens import default_token_generator

from .forms import NewUserForm


def sign_up(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information. Please try again!")
	form = NewUserForm()
	return render (request=request, template_name="users/auth/signup.html", context={"form":form})

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("homepage")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="users/auth/login.html", context={"login_form":form})

class LogInView(LoginView):
    template_name = 'users/auth/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or '/'


def logout_request(request):
	logout(request)
	messages.info(request, "You have been logged out successfuly!") 
	return redirect("homepage")

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "users/auth/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Kelodes Hospitality Masters',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("password_reset_done")
			else:
				messages.error(request, f"User with this Email '{data}' does not exist!")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="users/auth/password_reset.html", context={"password_reset_form":password_reset_form})