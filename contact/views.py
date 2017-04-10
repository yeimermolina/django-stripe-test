from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm
# Create your views here.
def contact(request):
	title = "Contact"
	form= ContactForm(request.POST or None)

	context = {
		"form": form,
		"title": title
	}

	if form.is_valid():
		print form.cleaned_data['email']
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = " Message from %s" %(name)
		message = "%s %s"%(comment, name)
		email_from = form.cleaned_data['email']
		email_to = [settings.EMAIL_HOST_USER]

		send_mail(
				subject, message, email_from, email_to, fail_silently= True
			)

		context['title'] = "Thanks" 

	template = "contact.html"
	return render(request, template, context) 