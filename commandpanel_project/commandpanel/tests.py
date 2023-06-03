from django.test import TestCase

from .models import Script, Parameter

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
        
class ParameterModelTest(TestCase):
    
    def setUp(self):
        self.script = Script.objects.create(
            name='Test Script',
            description='This is a test script',
            code='print("Hello, {}!")'
        )
        
        self.parameter = Parameter.objects.create(
            script=self.script,
            name='name',
            value='world'
        )

    def test_parameter_creation(self):
        self.assertEqual(f'{self.parameter.name}', 'name')
        self.assertEqual(f'{self.parameter.value}', 'world')
        self.assertEqual(self.parameter.script, self.script)

