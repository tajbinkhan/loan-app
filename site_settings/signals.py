from loan.models import Loan
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.utils import add_context_to_string
from .models import DomainSetting, EmailContent
from django.core.mail import EmailMessage

@receiver(post_save, sender=Loan)
def send_email_on_new_loan(sender, instance, created, *args, **kwargs):
	if created:
		try:
			domain_settings = DomainSetting.objects.last()
			email_content = EmailContent.objects.filter(notification_name='New Loan Request').last()
			context = {
				'domain': domain_settings.domain_name,
				'site_name': domain_settings.site_name,
				'protocol': domain_settings.protocol,
				'account_number': instance.user.account_number,
				'user': instance.user.username,
				'amount': instance.amount,
				'requested_date': instance.created,
				'returned_date': instance.return_date,
			}
			subject = email_content.subject
			from_ = f"{domain_settings.site_name} <{domain_settings.email_from}>"
			to = [instance.money_lender.email]
			if email_content.plain_text_html_enable == True:
				plain_html_content = add_context_to_string(email_content.plain_text_html, context)
				msg = EmailMessage(subject, plain_html_content, from_, to)
			else:
				html_content = add_context_to_string(email_content.message, context)
				msg = EmailMessage(subject, html_content, from_, to)
			msg.content_subtype = "html"
			msg.send()
			print(html_content)
		except:
			pass

@receiver(post_save, sender=Loan)
def send_email_on_approved_loan(sender, instance, *args, **kwargs):
	try:
		loan_user = Loan.objects.get(id=instance.id)
		if loan_user.status == 'Accepted':
			domain_settings = DomainSetting.objects.last()
			email_content = EmailContent.objects.filter(notification_name='New Loan Request Approved').last()
			context = {
				'domain': domain_settings.domain_name,
				'site_name': domain_settings.site_name,
				'protocol': domain_settings.protocol,
				'account_number': instance.user.account_number,
				'user': instance.user.username,
				'amount': instance.amount,
				'requested_date': instance.created,
				'returned_date': instance.return_date,
				'status': instance.status
			}
			subject = email_content.subject
			from_ = f"{domain_settings.site_name} <{domain_settings.email_from}>"
			to = [instance.money_lender.email]
			if email_content.plain_text_html_enable == True:
				plain_html_content = add_context_to_string(email_content.plain_text_html, context)
				msg = EmailMessage(subject, plain_html_content, from_, to)
			else:
				html_content = add_context_to_string(email_content.message, context)
				msg = EmailMessage(subject, html_content, from_, to)
			msg.content_subtype = "html"
			msg.send()
	except:
		pass

@receiver(post_save, sender=Loan)
def send_email_on_rejected_loan(sender, instance, *args, **kwargs):
	try:
		loan_user = Loan.objects.get(id=instance.id)
		if loan_user.status == 'Rejected':
			domain_settings = DomainSetting.objects.last()
			email_content = EmailContent.objects.filter(notification_name='New Loan Request Rejected').last()
			context = {
				'domain': domain_settings.domain_name,
				'site_name': domain_settings.site_name,
				'protocol': domain_settings.protocol,
				'account_number': instance.user.account_number,
				'user': instance.user.username,
				'amount': instance.amount,
				'requested_date': instance.created,
				'returned_date': instance.return_date,
				'status': instance.status
			}
			subject = email_content.subject
			from_ = f"{domain_settings.site_name} <{domain_settings.email_from}>"
			to = [instance.money_lender.email]
			if email_content.plain_text_html_enable == True:
				plain_html_content = add_context_to_string(email_content.plain_text_html, context)
				msg = EmailMessage(subject, plain_html_content, from_, to)
			else:
				html_content = add_context_to_string(email_content.message, context)
				msg = EmailMessage(subject, html_content, from_, to)
			msg.content_subtype = "html"
			msg.send()
	except:
		pass

@receiver(post_save, sender=Loan)
def send_email_on_edit_request(sender, instance, *args, **kwargs):
	try:
		loan_user = Loan.objects.get(id=instance.id)
		if loan_user.editable == 'Requested':
			domain_settings = DomainSetting.objects.last()
			email_content = EmailContent.objects.filter(notification_name='Loan Edit Request').last()
			context = {
				'domain': domain_settings.domain_name,
				'site_name': domain_settings.site_name,
				'protocol': domain_settings.protocol,
				'account_number': instance.user.account_number,
				'user': instance.user.username,
				'amount': instance.amount,
				'requested_date': instance.created,
				'returned_date': instance.return_date,
				'status': instance.status
			}
			subject = email_content.subject
			from_ = f"{domain_settings.site_name} <{domain_settings.email_from}>"
			to = [instance.money_lender.email]
			if email_content.plain_text_html_enable == True:
				plain_html_content = add_context_to_string(email_content.plain_text_html, context)
				msg = EmailMessage(subject, plain_html_content, from_, to)
			else:
				html_content = add_context_to_string(email_content.message, context)
				msg = EmailMessage(subject, html_content, from_, to)
			msg.content_subtype = "html"
			msg.send()
	except:
		pass

@receiver(post_save, sender=Loan)
def send_email_on_edit_request_approved(sender, instance, *args, **kwargs):
	try:
		loan_user = Loan.objects.get(id=instance.id)
		if loan_user.editable == 'Approved':
			domain_settings = DomainSetting.objects.last()
			email_content = EmailContent.objects.filter(notification_name='Loan Edit Request Approved').last()
			context = {
				'domain': domain_settings.domain_name,
				'site_name': domain_settings.site_name,
				'protocol': domain_settings.protocol,
				'account_number': instance.user.account_number,
				'user': instance.user.username,
				'amount': instance.amount,
				'requested_date': instance.created,
				'returned_date': instance.return_date,
				'status': instance.status
			}
			subject = email_content.subject
			from_ = f"{domain_settings.site_name} <{domain_settings.email_from}>"
			to = [instance.money_lender.email]
			if email_content.plain_text_html_enable == True:
				plain_html_content = add_context_to_string(email_content.plain_text_html, context)
				msg = EmailMessage(subject, plain_html_content, from_, to)
			else:
				html_content = add_context_to_string(email_content.message, context)
				msg = EmailMessage(subject, html_content, from_, to)
			msg.content_subtype = "html"
			msg.send()
	except:
		pass

@receiver(post_save, sender=Loan)
def send_email_on_edit_request_rejected(sender, instance, *args, **kwargs):
	try:
		loan_user = Loan.objects.get(id=instance.id)
		if loan_user.editable == 'Not Approved':
			domain_settings = DomainSetting.objects.last()
			email_content = EmailContent.objects.filter(notification_name='Loan Edit Request Rejected').last()
			context = {
				'domain': domain_settings.domain_name,
				'site_name': domain_settings.site_name,
				'protocol': domain_settings.protocol,
				'account_number': instance.user.account_number,
				'user': instance.user.username,
				'amount': instance.amount,
				'requested_date': instance.created,
				'returned_date': instance.return_date,
				'status': instance.status
			}
			subject = email_content.subject
			from_ = f"{domain_settings.site_name} <{domain_settings.email_from}>"
			to = [instance.money_lender.email]
			if email_content.plain_text_html_enable == True:
				plain_html_content = add_context_to_string(email_content.plain_text_html, context)
				msg = EmailMessage(subject, plain_html_content, from_, to)
			else:
				html_content = add_context_to_string(email_content.message, context)
				msg = EmailMessage(subject, html_content, from_, to)
			msg.content_subtype = "html"
			msg.send()
	except:
		pass