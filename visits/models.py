from django.db import models
from links.models import Link
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Visit(models.Model):
    link = models.ForeignKey(Link, verbose_name=_("Tracker link for this visit"), on_delete=models.CASCADE)
    headers = models.CharField(_("Request Headers"), max_length=400)
    timestamp = models.DateTimeField(_("Datetime of the visit"), auto_now=True)
