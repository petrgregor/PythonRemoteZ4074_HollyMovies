from django.test import TestCase


class ExampleTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Spustí se jednou na začátku testování a "
              "slouží k nastavení dat/databáze.")

    def setUp(self):
        pass
        #print("setUp: Spustí se před každým testem.")

    def test_false(self):
        result = False
        self.assertFalse(result)

    def test_add(self):
        result = 1 + 3
        self.assertEqual(result, 4)
