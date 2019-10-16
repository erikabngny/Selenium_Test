import unittest


class TestCAseDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("**********************")
        print("I will run only once before all tests")
        print("**********************")

    def setUp(self):
        print("I will run once before every test")

    def test_methodA(self):
        print("Running method A")

    def test_methodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(cls):
        print("**********************")
        print("I will run only once after all tests")
        print("**********************")


if __name__ == '__main__':
    unittest.main(verbosity=2)
