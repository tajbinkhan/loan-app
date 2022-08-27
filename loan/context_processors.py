from .models import Loan, NotificationHistory

def notification(request):
	loan_request = None
	update_request = None
	notification_history = None
	if request.user.is_authenticated:
		loan_request = Loan.objects.filter(money_lender=request.user, status='Pending', editable='Not Applied')
		update_request = Loan.objects.filter(money_lender=request.user, status='Accepted', editable='Requested')
		notification_history = NotificationHistory.objects.filter(user=request.user, mark_as_read=False)
		count_notification = loan_request.count() + update_request.count() + notification_history.count()
		show_notification = True
		if count_notification == 0:
			show_notification = False
		if count_notification > 9:
			count_notification = '9+'
	else:
		count_notification = None
		show_notification = None
	context = {
		'count_notification': count_notification,
		'show_notification': show_notification,
		'notification_history': notification_history,
		'loan_request': loan_request,
		'update_request': update_request,
	}
	return context