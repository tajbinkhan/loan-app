from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from bank.models import Statement, InterestStatement
from .forms import UserUpdateModelForm
from .models import User
from django.contrib import messages
from loan.models import Loan
from django.db.models import Count

# Create your views here.
@login_required
def profile(request):
	template_name = 'account/profile.html'
	show = True
	credit_total = 0
	debit_total = 0
	requested_amount_total = 0
	given_amount_total = 0
	sub_total = 0
	current_bank_balance = 0
	interest_balance = 0

	user = User.objects.get(username=request.user.username)
	accepted = Loan.objects.filter(user=request.user, status='Accepted').count()
	requested = Loan.objects.filter(user=request.user, status='Pending').count()
	rejected = Loan.objects.filter(user=request.user, status='Rejected').count()
	given = Loan.objects.filter(money_lender=request.user, status='Accepted').count()

	requested_amount = Loan.objects.filter(user=request.user, status='Accepted')
	given_amount = Loan.objects.filter(money_lender=request.user, status='Accepted')
	interest_balance_qs = InterestStatement.objects.filter(user=request.user)
	statement_credit_list = Statement.objects.filter(user=request.user, status='Credit')
	statement_debit_list = Statement.objects.filter(user=request.user, status='Debit')

	for i in statement_credit_list:
		credit_total = credit_total + int(i.amount)

	for i in statement_debit_list:
		debit_total = debit_total + int(i.amount)

	for i in requested_amount:
		requested_amount_total = requested_amount_total + i.amount

	for i in given_amount:
		given_amount_total = given_amount_total + i.amount

	for i in interest_balance_qs:
		interest_balance = interest_balance + (i.amount - i.tax)

	sub_total = credit_total - debit_total

	current_bank_balance = interest_balance + sub_total + user.initial_bank_balance

	# dupes = Loan.objects.values('user', 'money_lender').annotate(Count('id')).filter(user=request.user, status='Accepted')
	# print(dupes)

	# filter_accepted = Loan.objects.filter(user__in=[item['user'] for item in dupes])
	# for i in filter_accepted:
	# 	print(i)


	context = {
		'user': user,
		'show': show,
		'accepted': accepted,
		'requested': requested,
		'rejected': rejected,
		'given': given,
		'requested_amount_total': requested_amount_total,
		'given_amount_total': given_amount_total,
		'current_bank_balance': current_bank_balance,
		'interest_balance': interest_balance,
	}
	return render(request, template_name, context)

@login_required
def update_profile(request):
	template_name = 'account/profile_update.html'
	if request.method == 'POST':
		form = UserUpdateModelForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			user = form.save(commit=False)
			user = request.user
			user.save()
			messages.success(request, 'Profile Updated Successfully.')
			return redirect('profile')
		else:
			messages.error(request, "Profile couldn't updated.")
	else:
		form = UserUpdateModelForm(instance=request.user)
	context = {
		'form': form
	}
	return render(request, template_name, context)

@login_required
def show_profile(request, account_number):
	template_name = 'account/profile.html'
	show = True
	user = get_object_or_404(User, account_number=account_number)
	if not request.user.account_number == user.account_number:
		show = False
	context = {
		'user': user,
		'show': show
	}
	return render(request, template_name, context)