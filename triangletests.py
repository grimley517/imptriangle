import unittest
import triangle as t

class testFunctions(unittest.TestCase):
    def testCos1(self):
        '''Check that the cos function works'''
        self.assertAlmostEqual(t.cos(90), 0, places = 14)# Cos(90) should be 0 by definition
        self.assertAlmostEqual(t.cos(0), 1, places = 14) # cos 0 should be 1 by definition

    def testSin1(self):
        '''Check that the sin function works'''
        self.assertAlmostEqual(t.sin(90), 1, places = 14)#sin(90) should be 1 by definition
        self.assertAlmostEqual(t.sin(0), 0, places = 14) #sin(0) should be 0 by definition
        self.assertAlmostEqual(t.sin(45),t.cos(45), places = 14) #the Sins and cosine of 45 degress should be equal.

    def testTriangle1(self):
        '''Check for consistency with trig identities'''
        for x in range(360):
            a = t.sin(x)
            b = t.cos(x)
            self.assertAlmostEqual((a*a + b*b),1, places = 14) #trig identity used to check values of cos(x) and sin(x) over full circle

    def testIntCheck(self):
        ''' check for integer checking accuracy behaviour'''
        for i in range(1,20):
            answer = i > 14
            testVar = 2 + 10**(0-i)
            self.assertEqual(t.checkInt(testVar), answer) #should be true when i is greater than 14

if __name__ == '__main__':
    unittest.main(verbosity = 2)
