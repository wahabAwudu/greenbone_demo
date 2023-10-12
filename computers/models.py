from django.db import models
from uuid import uuid4
from django.utils.translation import gettext_lazy as _
from macaddress.fields import MACAddressField
from django.db.models.signals import post_save
from django.dispatch import receiver
from .utils import send_admin_notification


class Computer(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=250, help_text=_("Name of this computer"))
    description = models.TextField(null=True, blank=True, help_text=_("Description of the computer"),)
    mac_address = MACAddressField(integer=False, help_text=_("Mac Address of this computer"))
    ip_address = models.GenericIPAddressField(help_text=_("IP Address of this computer"))
    employee_abbrev = models.CharField(max_length=3, null=True, blank=True, help_text=_("Employee's name abbreviation"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.employee_abbrev} - {self.ip_address}"


@receiver(post_save, sender=Computer)
def notify_admins_signal(sender, instance, created, **kwargs):
    computers = Computer.objects.filter(employee_abbrev=instance.employee_abbrev)
    if created and computers.count() >= 3:
        send_admin_notification(
            employee=instance.employee_abbrev,
            computer_count=computers.count()
        )
