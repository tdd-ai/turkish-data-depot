from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group as DGroup
from django.db import models
from django.utils import timezone

from rest_framework.authtoken.models import Token

from .managers import UserManager
from tdd.models import BaseModel


# Django Group
class DjangoGroup(DGroup):

	class Meta:
		proxy=True
		verbose_name = _("Django Group")
		verbose_name_plural = _("Django Group")


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
	# Personal Info
	email = models.EmailField(verbose_name=_("email address"), max_length=60, unique=True)
	first_name = models.CharField(_("first name"), max_length=50)
	last_name = models.CharField(_("last name"), max_length=50)

	# Permissions
	is_staff = models.BooleanField(_("staff status"), default=False, help_text=_("Designates whether the user can log into this admin site."))
	is_active = models.BooleanField(_("active"), default=True, help_text=_("is active"))
	user_type = models.PositiveIntegerField(
		choices = (
			(1, _("admin")),
			(2, _("application user")),
		),
		default = 2,
		verbose_name = _("user type")
	)

	USERNAME_FIELD = "email"
	RQUIRED_FIELDS = []
	objects = UserManager()

	class Meta:
		verbose_name = _("User")
		verbose_name_plural = _("Users")

	def __str__(self):
		if not self.first_name or not self.last_name:
			return self.email
		else:
			return self.first_name + " " + self.last_name

	def clean(self):
		super(User, self).clean()
		self.email = self.__class__.objects.normalize_email(self.email)

	def get_full_name(self):
		full_name = "%s %s" % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		send_mail(subject, message, from_email, [self.email], **kwargs)
