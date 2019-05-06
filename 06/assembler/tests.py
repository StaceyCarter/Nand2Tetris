import unittest

class TestStringMethods(unittest.TestCase):

    def test_compare_add(self):
        with open("Add.hack") as myFile:
            myFile = myFile.read()
        with open("AddReference.hack") as comparisonFile:
            comparisonFile = comparisonFile.read()
        self.assertEqual(myFile, comparisonFile)

    def test_compare_max(self):
        with open("Max.hack") as myFile:
            myFile = myFile.read()
        with open("MaxReference.hack") as comparisonFile:
            comparisonFile = comparisonFile.read()
        self.assertEqual(myFile, comparisonFile)

    def test_compare_rect(self):
        with open("Rect.hack") as myFile:
            myFile = myFile.read()
        with open("RectReference.hack") as comparisonFile:
            comparisonFile = comparisonFile.read()
        self.assertEqual(myFile, comparisonFile)      
        

if __name__ == '__main__':
    unittest.main()