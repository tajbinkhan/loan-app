from django.shortcuts import render

def privacy_policy(request):
	template_name = 'policies/privacy_policy.html'
	context = {}
	return render(request, template_name, context)

def terms_of_services(request):
	template_name = 'policies/terms_of_services.html'
	context = {}
	return render(request, template_name, context)