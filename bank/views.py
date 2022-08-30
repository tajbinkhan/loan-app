from django.shortcuts import render, redirect, get_object_or_404
from .forms import StatementModelForm, InterestStatementModelForm
from .models import Statement, InterestStatement
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from crispy_forms.templatetags.crispy_forms_filters import as_crispy_field
from accounts_profile.models import User

# Create your views here.
@login_required
def statement_list(request):
	template_name = 'bank/statement_list.html'
	credit_total = 0
	debit_total = 0
	interest_total = 0
	statement_list = Statement.objects.filter(user=request.user)
	statement_credit_list = Statement.objects.filter(user=request.user, status='Credit')
	statement_debit_list = Statement.objects.filter(user=request.user, status='Debit')
	interest_statement_list = InterestStatement.objects.filter(user=request.user)

	for i in statement_credit_list:
		credit_total = credit_total + int(i.amount)

	for i in statement_debit_list:
		debit_total = debit_total + int(i.amount)

	for i in interest_statement_list:
		interest_total = interest_total + (int(i.amount) - int(i.tax))

	try:
		user_balance = User.objects.get(username=request.user.username)
		initaial_balance = user_balance.initial_bank_balance
	except:
		initaial_balance = 0

	sub_total = credit_total - debit_total
	total = initaial_balance + sub_total

	form = StatementModelForm()
	if request.method == 'POST':
		form = StatementModelForm(request.POST)
		if form.is_valid():
			initial_save = form.save(commit=False)
			initial_save.user = request.user
			initial_save.save()
			messages.success(request, 'Statement Added.')
			return redirect('statement_list')
		else:
			messages.error(request, 'Something went wrong, try again.')
	context = {
		'form': form,
		'total': total,
		'interest_total': interest_total,
		'statement_list': statement_list,
		'interest_statement_list': interest_statement_list,
	}
	return render(request, template_name, context)

@login_required
def statement_create(request):
	template_name = 'bank/statement_form.html'
	form = StatementModelForm()
	if request.method == 'POST':
		form = StatementModelForm(request.POST)
		if form.is_valid():
			initial_save = form.save(commit=False)
			initial_save.user = request.user
			initial_save.save()
			messages.success(request, 'Statement Added.')
			return redirect('statement_list')
		else:
			messages.error(request, 'Something went wrong, try again.')
	context = {
		'form': form,
	}
	return render(request, template_name, context)

@login_required
def statement_update(request, form_id):
	template_name = 'bank/statement_form.html'
	statement = get_object_or_404(Statement, form_id=form_id)
	form = StatementModelForm(instance=statement)
	if request.method == 'POST':
		form = StatementModelForm(request.POST, instance=statement)
		if form.is_valid():
			initial_save = form.save(commit=False)
			initial_save.user = request.user
			initial_save.save()
			messages.success(request, 'Statement Updated.')
			return redirect('statement_list')
		else:
			messages.error(request, 'Something went wrong, try again.')
	context = {
		'form': form,
	}
	return render(request, template_name, context)

@login_required
def statement_delete(request, form_id):
	statement = get_object_or_404(Statement, form_id=form_id)
	statement.delete()
	return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def interest_statement_create(request):
	template_name = 'bank/interest_form.html'
	form = InterestStatementModelForm()
	if request.method == 'POST':
		form = InterestStatementModelForm(request.POST)
		if form.is_valid():
			initial_save = form.save(commit=False)
			initial_save.user = request.user
			initial_save.save()
			messages.success(request, 'Interest Statement Added.')
			return redirect('statement_list')
		else:
			messages.error(request, 'Something went wrong, try again.')
	context = {
		'form': form,
	}
	return render(request, template_name, context)

@login_required
def interest_statement_update(request, form_id):
	template_name = 'bank/interest_form.html'
	interest_statement = get_object_or_404(InterestStatement, form_id=form_id)
	form = InterestStatementModelForm(instance=interest_statement)
	if request.method == 'POST':
		form = InterestStatementModelForm(request.POST, instance=interest_statement)
		if form.is_valid():
			initial_save = form.save(commit=False)
			initial_save.user = request.user
			initial_save.save()
			messages.success(request, 'Interest Statement Updated.')
			return redirect('statement_list')
		else:
			messages.error(request, 'Something went wrong, try again.')
	context = {
		'form': form,
	}
	return render(request, template_name, context)

@login_required
def interest_statement_delete(request, form_id):
	interest_statement = get_object_or_404(InterestStatement, form_id=form_id)
	interest_statement.delete()
	return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

# HTMX validation
def check_amount(request):
	template_name = 'bank/partial/button.html'
	form = StatementModelForm(request.GET)
	context = {
		'field': as_crispy_field(form['amount']),
		'valid': not form['amount'].errors
	}
	return render(request, template_name, context)

def check_entry_date(request):
	template_name = 'bank/partial/button.html'
	form = StatementModelForm(request.GET)
	context = {
		'field': as_crispy_field(form['entry_date']),
		'valid': not form['entry_date'].errors
	}
	return render(request, template_name, context)

def check_interest_amount(request):
	template_name = 'bank/partial/button.html'
	form = InterestStatementModelForm(request.GET)
	context = {
		'field': as_crispy_field(form['amount']),
		'valid': not form['amount'].errors
	}
	return render(request, template_name, context)

def check_interest_tax(request):
	template_name = 'bank/partial/button.html'
	form = InterestStatementModelForm(request.GET)
	context = {
		'field': as_crispy_field(form['tax']),
		'valid': not form['tax'].errors
	}
	return render(request, template_name, context)

def check_interest_entry_date(request):
	template_name = 'bank/partial/button.html'
	form = InterestStatementModelForm(request.GET)
	context = {
		'field': as_crispy_field(form['entry_date']),
		'valid': not form['entry_date'].errors
	}
	return render(request, template_name, context)

