from django.test import TestCase

from .models import Script

class ScriptModelTest(TestCase):
    
    def setUp(self):
        self.script = Script.objects.create(
            name='Test Script',
            description='This is a test script',
            code='print("Hello, world!")'
        )

    def test_script_creation(self):
        self.assertEqual(f'{self.script.name}', 'Test Script')
        self.assertEqual(f'{self.script.description}', 'This is a test script')
        self.assertEqual(f'{self.script.code}', 'print("Hello, world!")')

