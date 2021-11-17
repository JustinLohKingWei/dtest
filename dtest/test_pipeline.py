import unittest
from pipeline import check_diabetes,average


class testAverage(unittest.TestCase):
    def test_AllZeroInputs(self):
        self.assertEquals(average('0','0','0'),0)
    def test_NonNumberInputs(self):
        self.assertEquals(average('n/a','2','4'),3)
        self.assertEquals(average('2','n/a','4'),3)
        self.assertEquals(average('2','4','n/a'),3)
    def test_NullInputs(self):
        self.assertEquals(average(None,'2','4'),3)
        self.assertEquals(average('2',None,'4'),3)
        self.assertEquals(average('2','4',None),3)
    def test_EmptyStringInputs(self):
        self.assertEquals(average('','2','4'),3)
        self.assertEquals(average('2','','4'),3)
        self.assertEquals(average('2','4',''),3)
    def test_OutOfRangeInputs(self):
        self.assertEquals(average('2597','2','4'),3)
        self.assertEquals(average('2','-1','4'),3)
        self.assertEquals(average('2','4','0'),3)


class testDiagnostics(unittest.TestCase):
    def test_Diabetic(self):
        self.assertEquals(check_diabetes(201),'Diabetes')

    def test_Prediabetic(self):
        self.assertEquals(check_diabetes(200),'Prediabetes')

    def test_Normal(self):
        self.assertEquals(check_diabetes(140),'Normal')
