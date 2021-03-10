from django import forms
from django.contrib.auth import password_validation
from django.utils.translation import ugettext as _
from .models import User


class UserForm(forms.ModelForm):
	email = forms.EmailField(required=True)
	password1 = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput, required=False)
	password2 = forms.CharField(label=_("Password confirmation"), widget=forms.PasswordInput, strip=False, help_text=_("Enter the same password as before, for verification."), required=False)
	error_messages = {"password_mismatch": _("The two password fields didn't match.")}

	class Meta:
		model = User
		fields = ("email", )

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError(
				self.error_messages["password_mismatch"],
				code="password_mismatch",
		)

		if password1 and password2:
			password_validation.validate_password(self.cleaned_data.get("password2"), self.instance)
		return password2

	def save(self, commit=True):
		# Save the provided password in hashed format
		user = super(UserForm, self).save(commit=False)
		if self.cleaned_data["password1"]:
			user.set_password(self.cleaned_data["password1"])
		if commit:
			user.save()
		return user
