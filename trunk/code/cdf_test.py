import unittest
import Cdf

class Test(unittest.TestCase):

    def setUp(self):
        t = [2, 1, 3, 2, 5]
        self.cdf = Cdf.MakeCdfFromList(t, 'bob')

    def testMakeCdf(self):
        cdf = self.cdf
        self.assertEqual(cdf.vs, [1, 2, 3, 5])
        self.assertEqual(cdf.ps, [0.2, 0.6, 0.8, 1.0])
        self.assertEqual(cdf.name, 'bob')

    def testProb(self):
        cdf = self.cdf
        self.assertEqual(cdf.Prob(-1), 0.0)
        self.assertEqual(cdf.Prob(1), 0.2)
        self.assertEqual(cdf.Prob(2), 0.6)
        self.assertEqual(cdf.Prob(2.5), 0.6)
        self.assertEqual(cdf.Prob(4), 0.8)
        self.assertEqual(cdf.Prob(5), 1.0)
        self.assertEqual(cdf.Prob(7), 1.0)

    def testValue(self):
        cdf = self.cdf
        self.assertEqual(cdf.Value(0.0), 1)
        self.assertEqual(cdf.Value(0.1), 1)
        self.assertEqual(cdf.Value(0.2), 1)
        self.assertEqual(cdf.Value(0.3), 2)
        self.assertEqual(cdf.Value(0.4), 2)
        self.assertEqual(cdf.Value(0.5), 2)
        self.assertEqual(cdf.Value(0.6), 2)
        self.assertEqual(cdf.Value(0.7), 3)
        self.assertEqual(cdf.Value(0.8), 3)
        self.assertEqual(cdf.Value(0.9), 5)
        self.assertEqual(cdf.Value(1.0), 5)
        self.assertRaises(ValueError, cdf.Value, -0.1)
        self.assertRaises(ValueError, cdf.Value, 1.1)

    def testMean(self):
        cdf = self.cdf
        self.assertAlmostEqual(cdf.Mean(), 13.0/5.0)
        
    def testRender(self):
        cdf = self.cdf
        data = cdf.Render()
        print data

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testCdf']
    unittest.main()