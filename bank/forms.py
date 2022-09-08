from django import forms
from datetime import datetime
from .models import Statement, InterestStatement
from django.urls import reverse_lazy

class StatementModelForm(forms.ModelForm):
	class Meta:
		model = Statement
		fields = ['amount', 'status', 'description', 'entry_date']
		widgets = {
			'amount': forms.NumberInput(
				attrs={
					'placeholder': 'Enter amount',
				}
			),
			'description': forms.TextInput(
				attrs={
					'placeholder': 'Enter description',
				}
			),
			'entry_date': forms.DateInput(
				format=('%Y-%m-%d'),
				attrs={
					'type':'date',
					'hx-get': reverse_lazy('check_entry_date'),
					'hx-trigger': 'change',
					'hx-target': '#div_id_entry_date'
				}
			),
		}

	def clean_amount(self):
		data = self.cleaned_data
		amount = data.get('amount')
		if amount < 1 and amount == 0:
			self.add_error('amount', 'Value have to be greater than zero.')
		return amount

	def clean_entry_date(self):
		data = self.cleaned_data
		date = data.get('entry_date')
		if date > datetime.now().date():
			self.add_error('entry_date', "Entry date can't be future.")
		return date

class InterestStatementModelForm(forms.ModelForm):
	class Meta:
		model = InterestStatement
		fields = ['amount', 'tax', 'entry_date']
		widgets = {
			'amount': forms.NumberInput(
				attrs={
					'placeholder': 'Enter amount',
				}
			),
			'tax': forms.TextInput(
				attrs={
					'placeholder': 'Enter tax',
					'hx-get': reverse_lazy('check_interest_tax'),
					'hx-trigger': 'keyup changed',
					'hx-target': '#div_id_tax'
				}
			),
			'entry_date': forms.DateInput(
				format=('%Y-%m-%d'),
				attrs={
					'type':'date',
					'hx-get': reverse_lazy('check_interest_entry_date'),
					'hx-trigger': 'change',
					'hx-target': '#div_id_entry_date'
				}
			),
		}

	def clean_amount(self):
		data = self.cleaned_data
		amount = data.get('amount')
		if amount < 1 and amount == 0:
			self.add_error('amount', 'Value have to be greater than zero.')
		return amount

	def clean_entry_date(self):
		data = self.cleaned_data
		date = data.get('entry_date')
		if date > datetime.now().date():
			self.add_error('entry_date', "Entry date can't be future.")
		return date