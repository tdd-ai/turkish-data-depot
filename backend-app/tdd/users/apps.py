from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class UsersConfig(AppConfig):
	name = "users"
	verbose_name = _("Users")
