from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Link(models.Model):
    tracker = models.CharField(_("Tracker link"), max_length=100)
    is_enabled = models.BooleanField(_("Is the link enable?"))
    visit_count = models.PositiveIntegerField(_("Total visit count for this link"))
    created_at = models.DateTimeField(_("Datetime at the creation time"), auto_now_add=True)
    last_opened = models.DateTimeField(_("Datetime at last opened"))
    notifications_enabled = models.BooleanField(_("Are notifications enabled for this link?"))
    creator = models.ForeignKey(get_user_model(), verbose_name=_("Creator of this link"), on_delete=models.CASCADE)
