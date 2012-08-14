Django Fixture
==============

A Django Decorator to be able to load a fixture on a test-by-test basis.  This can also be used with the global <code>fixtures</code> 

    class ClassToTest(TestCase):
		fixtures = ['globalone.json', 'globaltwo']

        @Fixture('firstfixture.yaml','secondfixture.yaml')
        def setUp(self):
		   pass
