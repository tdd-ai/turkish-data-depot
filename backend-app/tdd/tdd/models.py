from django.utils.translation import ugettext_lazy as _
from django.db import models

class BaseModel(models.Model):
	create_date = models.DateTimeField(auto_now_add=True, verbose_name=_("create date"), null=True)
	update_date = models.DateTimeField(auto_now=True, verbose_name=_("update date"), null=True)

	class Meta:
		abstract = True