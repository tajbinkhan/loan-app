from datetime import datetime
from django import forms
from accounts_profile.models import User
from .models import Loan

class LoanForm(forms.Form):
	account_number = forms.CharField(
		label='Account Number',
		max_length=200,
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Account Number'
			}
		)
	)
	account_name = forms.CharField(
		label='Account Name',
		max_length=200,
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Account Name'
			}
		)
	)
	amount = forms.CharField(
		label='Loan Amount',
		max_length=100,
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'Enter loan amount (Minimum 50 BDT)'
			}
		)
	)
	return_date = forms.DateField(
		label='Return Date',
		input_formats=['%Y-%m-%d'],
		widget=forms.DateInput(
			attrs={
				'type': 'date',
			}
		)
	)

	def clean_account_number(self):
		data = self.cleaned_data
		account_number = data.get('account_number')
		user = User.objects.filter(account_number=account_number)
		if len(account_number) < 16 or len(account_number) > 16:
			self.add_error('account_number', 'Account number requires 16 digits.')
		elif not user.exists():
			self.add_error('account_number', 'Enter correct account number.')
		return account_number

	def clean_account_name(self):
		data = self.cleaned_data
		account_name = data.get('account_name')
		user = User.objects.filter(username=account_name)
		if not user.exists():
			self.add_error('account_name', 'Enter correct account name.')
		return account_name

	def clean_return_date(self):
		data = self.cleaned_data
		date = data.get('return_date')
		print(date)
		if date < datetime.now().date():
			self.add_error('return_date', 'Past date can not be choosen.')
		elif date == datetime.now().date():
			self.add_error('return_date', 'Today can not be returned date.')
		return date

class LoanUpdateModelForm(forms.ModelForm):
	class Meta:
		model = Loan
		fields = ['amount', 'return_date']
		widgets = {
			'return_date': forms.DateInput(
				format=('%Y-%m-%d'),
				attrs={
					'type':'date'
				}
			),
		}

class LoanRequestAgainForm(forms.Form):
	amount = forms.CharField(
		label='Loan Amount',
		max_length=100,
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'Enter loan amount (Minimum 50 BDT)'
			}
		)
	)
	return_date = forms.DateField(
		label='Return Date',
		input_formats=['%Y-%m-%d'],
		widget=forms.DateInput(
			attrs={
				'type': 'date',
			}
		)
	)

	def clean_date(self):
		data = self.cleaned_data
		date = data.get('return_date')
		if date < datetime.now().date():
			self.add_error('return_date', 'Past date can not be choosen.')
		elif date == datetime.now().date():
			self.add_error('return_date', 'Today can not be returned date.')
		return date