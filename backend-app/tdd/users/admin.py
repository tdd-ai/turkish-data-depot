from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group as DGroup
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib import admin

from rest_framework.authtoken.models import Token
from .models import User, DjangoGroup
from .forms import UserForm


class CustomUserAdmin(admin.ModelAdmin):
	list_display = ("email", "first_name", "last_name", "create_date")
	fields = ("email", "first_name", "last_name", "password1", "password2")
	search_fields = ("email", "first_name", "last_name")
	readonly_fields = ("create_date", "update_date")
	form = UserForm

	def save_model(self, request, obj, form, change):

		if self.user_type == 1:
			obj.is_staff = True
			obj.is_superuser = True

		obj.user_type = self.user_type
		obj.save()


@admin.register(User)
class UserAdmin(CustomUserAdmin):
	user_type = 2


admin.site.unregister(DGroup)
# admin.site.unregister(Token)