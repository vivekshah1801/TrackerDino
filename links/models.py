from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4

# Create your models here.
class Link(models.Model):
    name = models.CharField(_("Tracker Name"), max_length=50, unique=True)
    uuid = models.CharField(_("Tracker link uuid"), max_length=100, primary_key=True, default=uuid4())
    is_enabled = models.BooleanField(_("Is the link enable?"), default=True)
    visit_count = models.PositiveIntegerField(_("Total visit count for this link"), default=0)
    created_at = models.DateTimeField(_("Datetime at the creation time"), auto_now_add=True)
    last_opened = models.DateTimeField(_("Datetime at last opened"), null=True, blank=True)
    first_opened = models.DateTimeField(_("Datetime of first opened"), null=True, blank=True)
    notifications_enabled = models.BooleanField(_("Are notifications enabled for this link?"), default=False)
    creator = models.CharField(_("Creator"), max_length=100) 

    def __str__(self):
        return f"Link: <{self.uuid}> [{self.creator}]"