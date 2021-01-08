from django import forms
from django.core import validators

class FormName(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	verify_email = forms.EmailField(label="Enter Email Again")
	bio = forms.CharField(widget=forms.Textarea)
	botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) 

	def clean(self):
		all_cleane_data= super().clean()
		email = all_cleane_data['email']
		v_email = all_cleane_data['verify_email']

		if email != v_email:
			raise forms.ValidationError("Make sure emails match!")


