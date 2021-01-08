from django.shortcuts import render
from test1_app import forms
# Create your views here.
def index(request):
	return render(request, 'index.html')

def about_us(request):
	return render(request, 'about_us.html')

def contact_us(request):
	form = forms.FormName()
	if request.method == 'POST':
		form = forms.FormName(request.POST)

		if form.is_valid():
			print("Success!")
			print("Name:"+form.cleaned_data['name'])
			print("Email:"+form.cleaned_data['email'])
			print("Bio:"+form.cleaned_data['bio'])
	return render(request, 'contact_us.html',{'form':form})