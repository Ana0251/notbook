from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout


def register(request):
	if request.method == 'POST':
		print(request.POST)
		form = SignUpForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			login(request, new_user)
			return redirect('memories:home')

	return render(request, 'users/register.html')

def loginview(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		print(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('memories:home')
		else:
			return redirect('users:register')
	else:
		form = AuthenticationForm()
	return render(request, 'users/login.html', {'form': form})

def logoutview(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('users:logout')
	return redirect('users:login')