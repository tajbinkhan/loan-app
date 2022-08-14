from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoanForm, LoanRequestAgainForm, LoanUpdateModelForm
from .models import Loan, PreviousUserList
from accounts_profile.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
	template_name = 'dashboard/dashboard.html'
	accepted_list = Loan.objects.filter(user=request.user, status='Accepted')
	requested_list = Loan.objects.filter(user=request.user, status='Pending')
	rejected_list = Loan.objects.filter(user=request.user, status='Rejected')
	form = LoanForm()
	if request.method == 'POST':
		form = LoanForm(request.POST or None)
		if form.is_valid():
			account_number = form.cleaned_data.get('account_number')
			account_name = form.cleaned_data.get('account_name')
			amount = form.cleaned_data.get('amount')
			return_date = form.cleaned_data.get('return_date')
			if request.user.username == account_name:
				messages.error(request, "You can't loan from yourself!!!")
			else:
				account_number_db = User.objects.filter(account_number=account_number)
				if account_number_db.exists():
					user = User.objects.get(username=account_name)
					Loan.objects.create(user=request.user, money_lender=user, return_date=return_date, amount=amount)
					return redirect('dashboard')
	context = {
		'form': form,
		'requested_list': requested_list,
		'rejected_list': rejected_list,
		'accepted_list': accepted_list,
	}
	return render(request, template_name, context)

@login_required
def loan_requested(request):
	template_name = 'loan/loan_requested.html'
	loan_requested = Loan.objects.filter(money_lender=request.user, status='Accepted')
	context = {
		'loan_requested': loan_requested
	}
	return render(request, template_name, context)

@login_required
def loan_form(request):
	template_name = 'loan/loan_request.html'
	form = LoanForm()
	if request.method == 'POST':
		form = LoanForm(request.POST or None)
		if form.is_valid():
			account_number = form.cleaned_data.get('account_number')
			account_name = form.cleaned_data.get('account_name')
			amount = form.cleaned_data.get('amount')
			return_date = form.cleaned_data.get('return_date')
			if request.user.username == account_name:
				messages.error(request, "You can't loan from yourself!!!")
			else:
				account_number_db = User.objects.filter(account_number=account_number)
				if account_number_db.exists():
					user = User.objects.get(username=account_name)
					Loan.objects.create(user=request.user, money_lender=user, return_date=return_date, amount=amount)
					return redirect('dashboard')
	context = {
		'form': form
	}
	return render(request, template_name, context)

@login_required
def previous_user_list(request):
	template_name = 'loan/previous_user_list.html'
	previous_user_list = PreviousUserList.objects.filter(user=request.user)
	if request.method == 'POST':
		form = LoanForm(request.POST or None)
		if form.is_valid():
			account_number = form.cleaned_data.get('account_number')
			account_name = form.cleaned_data.get('account_name')
			amount = form.cleaned_data.get('amount')
			return_date = form.cleaned_data.get('return_date')
			if request.user.username == account_name:
				messages.error(request, "You can't loan from yourself!!!")
			else:
				account_number_db = User.objects.filter(account_number=account_number)
				if account_number_db.exists():
					user = User.objects.get(username=account_name)
					Loan.objects.create(user=request.user, money_lender=user, return_date=return_date, amount=amount)
					return redirect('dashboard')
		else:
			messages.success(request, 'Something went wrong, try again!!!')
	else:
		form = LoanForm()
	context = {
		'form': form,
		'previous_user_list': previous_user_list
	}
	return render(request, template_name, context)

@login_required
def loan_request_again(request, account_number):
	template_name = 'loan/loan_request_again.html'
	user = get_object_or_404(User, account_number=account_number)
	previous_user_list = PreviousUserList.objects.filter(user=request.user, money_lender=user)
	if previous_user_list.exists():
		if request.method == 'POST':
			form = LoanRequestAgainForm(request.POST)
			if form.is_valid():
				amount = form.cleaned_data.get('amount')
				return_date = form.cleaned_data.get('return_date')
				Loan.objects.create(user=request.user, money_lender=user, amount=amount, return_date=return_date)
				messages.success(request, 'Loan Request Successfully Sent!')
				return redirect('dashboard')
			else:
				messages.success(request, 'Something went wrong, try again!!!')
		else:
			form = LoanRequestAgainForm()
	else:
		form = None
	context = {
		'form': form,
		'previous_user_list': previous_user_list
	}
	return render(request, template_name, context)

@login_required
def update_loan(request, form_id):
	template_name = 'loan/loan_request_again.html'
	loan = get_object_or_404(Loan, form_id=form_id)
	if request.method == 'POST':
		form = LoanUpdateModelForm(request.POST, instance=loan)
		if form.is_valid():
			form.save()
			loan.editable = 'Updated'
			loan.save()
			messages.info(request, 'Requested Loan Successfully Updated!')
			return redirect('dashboard')
		else:
			messages.error(request, 'Something went wrong. Please try again!!!')
	else:
		form = LoanUpdateModelForm(instance=loan)
	context = {
		'form': form
	}
	return render(request, template_name, context)

def notification(request):
	template_name = 'loan/notification.html'
	loan_requested = Loan.objects.filter(money_lender=request.user, status='Pending', editable='Not Applied')
	update_request = Loan.objects.filter(money_lender=request.user, status='Accepted', editable='Requested')
	context = {
		'loan_requested': loan_requested,
		'update_request': update_request
	}
	return render(request, template_name, context)

@login_required
def notification_approve(request, form_id):
	loan = get_object_or_404(Loan, form_id=form_id, status='Pending')
	loan.status = 'Accepted'
	loan.save()
	return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def notification_deny(request, form_id):
	loan = get_object_or_404(Loan, form_id=form_id, status='Pending')
	loan.status = 'Rejected'
	loan.save()
	return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def request_for_update(request, form_id):
	loan = get_object_or_404(Loan, form_id=form_id)
	if loan.status == 'Pending':
		messages.info(request, 'Loan needs to be accepted!')
	else:
		loan.editable = 'Requested'
		loan.save()
	return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def request_for_update_approve(request, form_id):
	loan = get_object_or_404(Loan, form_id=form_id)
	loan.editable = 'Approved'
	loan.save()
	return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def request_for_update_deny(request, form_id):
	loan = get_object_or_404(Loan, form_id=form_id)
	loan.editable = 'Not Approved'
	loan.save()
	return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

@login_required
def loan_delete(request, form_id):
	loan = get_object_or_404(Loan, form_id=form_id)
	if loan.status == 'Pending':
		loan.delete()
		messages.success(request, 'Successfully deleted.')
	else:
		messages.warning(request, 'You have no premission to delete it.')
	return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))