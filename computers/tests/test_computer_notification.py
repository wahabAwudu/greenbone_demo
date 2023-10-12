from django.test import TestCase
from computers.factories import ComputerFactory
from unittest import mock
from django.db.models.signals import post_save


class NotificationTestCase(TestCase):
    @mock.patch("computers.models.notify_admins_signal")
    def test_admin_notification_not_called(self, notify_mock):
        ComputerFactory(
            ip_address="192.168.0.1",
            mac_address="00-B0-D0-63-C2-29",
            description=None,
            employee_abbrev="mum"
        )
        ComputerFactory(
            ip_address="192.168.0.3",
            mac_address="00-B0-D0-63-C2-27",
            description=None,
            employee_abbrev="mum"
        )
        ComputerFactory(
            ip_address="192.168.0.3",
            mac_address="00-B0-D0-63-C2-27",
            description=None,
            employee_abbrev="mon" # different employee
        )
        notify_mock.assert_not_called()
