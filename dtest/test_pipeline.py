import unittest
from .pipeline import isDigit,clean,check_diabetes,average

class testIsDigit(unittest.TestCase):
    def testIsNumber(self):
        self.assertTrue(isDigit('-1'))
        self.assertTrue(isDigit('123.34'))
        self.assertTrue(isDigit('10'))
    def testIsNotNumber(self):
        self.assertFalse(isDigit(''))
        self.assertFalse(isDigit('Apple'))
        self.assertFalse(isDigit('1a0'))


class testClean(unittest.TestCase):
    def testInvalidNumber(self):
        self.assertEqual(clean('-1'),'Test Results Invalid')
        self.assertEqual(clean('10000'),'Test Results Invalid')
    def testInvalidString(self):
        self.assertEqual(clean('Apple'),'Test Results Invalid')
    def testEmptyString(self):
        self.assertEqual(clean(''),'Test Results Invalid')


class testAverage(unittest.TestCase):
    def test_AllZeroInputs(self):
        self.assertEqual(average('0','0','0'),0)
    def test_NonNumberInputs(self):
        self.assertEqual(average('n/a','2','4'),3)
        self.assertEqual(average('2','n/a','4'),3)
        self.assertEqual(average('2','4','n/a'),3)
    def test_NullInputs(self):
        self.assertEqual(average(None,'2','4'),3)
        self.assertEqual(average('2',None,'4'),3)
        self.assertEqual(average('2','4',None),3)
    def test_EmptyStringInputs(self):
        self.assertEqual(average('','2','4'),3)
        self.assertEqual(average('2','','4'),3)
        self.assertEqual(average('2','4',''),3)
    def test_OutOfRangeInputs(self):
        self.assertEqual(average('2597','2','4'),3)
        self.assertEqual(average('2','-1','4'),3)
        self.assertEqual(average('2','4','0'),3)


class testDiagnostics(unittest.TestCase):
    def test_Diabetic(self):
        self.assertEqual(check_diabetes(200),'Diabetes')

    def test_Prediabetic(self):
        self.assertEqual(check_diabetes(199),'Prediabetes')

    def test_Normal(self):
        self.assertEqual(check_diabetes(139),'Normal')
    def test_Invalid(self):
        self.assertEqual(check_diabetes(-1),'Invalid Result')
        self.assertEqual(check_diabetes(2600),'Invalid Result')
