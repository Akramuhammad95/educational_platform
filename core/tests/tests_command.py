# core/tests/test_commands.py

from unittest.mock import patch
from django.core.management import call_command
from django.test import SimpleTestCase
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

class CommandTests(SimpleTestCase):
    """Test custom Django management commands."""

    @patch('time.sleep', return_value=None)
    @patch('core.management.commands.wait_for_db.Command.check')
    def test_wait_for_db_delay(self, patched_check, patched_sleep):
        """Test waiting for database when getting operational errors."""
        # محاكاة استثناءات DB قبل أن تكون جاهزة
        patched_check.side_effect = [Psycopg2Error]*2 + [OperationalError]*3 + [True]
        call_command('wait_for_db')
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])

    @patch('core.management.commands.wait_for_db.Command.check')
    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database when it's ready immediately."""
        patched_check.return_value = True
        call_command('wait_for_db')
        patched_check.assert_called_with(databases=['default'])
        self.assertEqual(patched_check.call_count, 1)
