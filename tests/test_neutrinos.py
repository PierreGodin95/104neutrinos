import unittest
# import sys
# import os
#os.path.append("..")
import neutrinos

class TestNeutrinos(unittest.TestCase):
    #def name_test(function_to_be_tested(), expected_ouput)

# ########################################################################################
    def test_harmomean(self):
        self.assertAlmostEqual(neutrinos.harmomean(6, 2, 3), 2.1)

# ########################################################################################
    def test_rootmean(self):
        self.assertAlmostEqual(neutrinos.rootmean(2, 3, 5), 3.696845502136472)

########################################################################################
    def test_aritmean(self):
        self.assertAlmostEqual(neutrinos.aritmeticmean(2, 3, 3), 3)

########################################################################################
    def test_sd(self):
        self.assertAlmostEqual(neutrinos.stand_deviation(2, 3, 3, 4), 1.7888543819998317)

########################################################################################
    def test_create_rootmean(self):
        self.assertAlmostEqual(neutrinos.create_rootmean(3, 2), 3.605551275463989)

########################################################################################

if __name__ == '__main__':
    unittest.main()
