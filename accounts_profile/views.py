from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateModelForm
from .models import User
from django.contrib import messages
from loan.models import Loan

# Create your views here.
@login_required
def profile(request):
	template_name = 'account/profile.html'
	show = True
	user = User.objects.get(username=request.user.username)
	accepted = Loan.objects.filter(user=request.user, status='Accepted').count()
	requested = Loan.objects.filter(user=request.user, status='Pending').count()
	rejected = Loan.objects.filter(user=request.user, status='Rejected').count()
	given = Loan.objects.filter(money_lender=request.user, status='Accepted').count()
	context = {
		'user': user,
		'show': show,
		'accepted': accepted,
		'requested': requested,
		'rejected': rejected,
		'given': given,
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