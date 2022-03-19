from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm
# Create your views here.
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('accessPage')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				
				return redirect('login')
			
		context = {'form':form}
		return render(request, 'register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('accessPage')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('accessPage')
			else:
				messages.info(request, 'Username or Password is incorrect!')
			
		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def accessPage(request):
	#customer = Customer.objects.get(id=pk)
	context = {}
	return render(request, 'accesspage.html', {})

def home(request):
	import requests
	import json

	#grab crypto price data
	price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,ADA,BNB,USDT,DOGE,XLM,LTC,POT&tsyms=USD")
	price = json.loads(price_request.content)

	#grab crypto news
	api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
	api = json.loads(api_request.content)
	return render(request, 'home.html', {'api': api, 'price': price})
	

def prices(request):
	if request.method == 'POST':
		import requests
		import json
		quote = request.POST['quote']
		quote = quote.upper()
		crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
		crypto = json.loads(crypto_request.content)
		return render(request, 'prices.html', {'quote':quote, 'crypto':crypto})

	else:
		notfound = "404 Not Found"
		return render(request, 'prices.html', {'notfound': notfound})
	
def blogs(request):
	return render(request, 'blogs.html', {})

def about(request):
	return render(request, 'about.html', {})

