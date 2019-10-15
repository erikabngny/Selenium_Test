import unittest

class TestClass2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("**********************")
        print("Class 2 -> class level setUp")
        print("**********************")

    def setUp(self):
        print("Class 2 -> setUp")

    def test_class2_methodA(self):
        print("Running class 2 -> method A")

    def test_class2_methodB(self):
        print("Running class 2 -> method A")

    def tearDown(self):
        print("Class 2 -> tearDown")

    @classmethod
    def tearDownClass(cls):
        print("**********************")
        print("Class 2 -> class level tearDown")
        print("**********************")

if __name__ == '__main__':
    unittest.main(verbosity=2)
