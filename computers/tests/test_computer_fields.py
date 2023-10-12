from django.test import TestCase
from computers.factories import ComputerFactory
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError, DataError


class ComputerTestCase(TestCase):
    def test_optional_fields_succeed(self):
        comp = ComputerFactory(
            ip_address="192.168.0.1",
            mac_address="00-B0-D0-63-C2-29",
            description=None,
            employee_abbrev=None
        )
        self.assertEqual(comp.description, None)
        self.assertEqual(comp.employee_abbrev, None)
    
    def test_employee_abbreviation_length(self):
        with self.assertRaises(DataError):
            ComputerFactory(
                ip_address="192.168.0.1",
                mac_address="00-B0-D0-63-C2-29",
                description=None,
                employee_abbrev="mmum"
            )

    def test_null_mac_address_fails(self):
        with self.assertRaises(IntegrityError):
            ComputerFactory(
            ip_address="192.168.0.1",
            mac_address=None,
            )
    
    def test_null_ip_address_fails(self):
        with self.assertRaises(IntegrityError):
            ComputerFactory(
            ip_address=None,
            mac_address="00-B0-D0-63-C2-29",
            )

    def test_invalid_mac_address(self):
        with self.assertRaises(ValidationError) as cm:
            ComputerFactory(
            ip_address="192.168.0.1",
            mac_address="00-B0-D0-63-C2",
            )
        
        self.assertEqual(cm.exception.message, 'This value must be a valid MAC address.')
    
    def test_invalid_ip_address(self):
        with self.assertRaises(DataError):
            ComputerFactory(
            ip_address="192.168.0.d",
            mac_address="00-B0-D0-63-C2-29",
            )
