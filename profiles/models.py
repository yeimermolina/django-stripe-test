from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from allauth.account.signals import user_logged_in, user_signed_up

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your models here.
class Profile(models.Model):
	name = models.CharField(max_length=120)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
	description = models.TextField(default="description default text")

	def __unicode__(self):
		return self.name


class UserStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		if self.stripe_id:
			return str(self.stripe_id)
		else:
			return self.user.username


def stripe_callback(sender, request, user, **kwargs):
	user_stripe_account, created = UserStripe.objects.get_or_create(user=user)
	if created:
		print "created for %s" %(user.username)
	if user_stripe_account.stripe_id is None or user_stripe_account.stripe_id == '':
		new_stripe_id = stripe.Customer.create(email=user.email)
		user_stripe_account.stripe_id = new_stripe_id['id']
		user_stripe_account.save()


def profile_callback(sender, request, user, **kwargs):
	user_profile, is_created = Profile.objects.get_or_create(user=user)
	if is_created:
		user_profile.name = user.username
		user_profile.save()

user_logged_in.connect(stripe_callback)
user_signed_up.connect(stripe_callback)
user_signed_up.connect(profile_callback)