import unittest
from coureur import Coureur

class CoureurTest(unittest.TestCase):

    def setUp(self):
        self.coureur1 = Coureur('Kim',45)
        self.coureur2 = Coureur('Charles',50)
        self.coureur3 = Coureur('Siegfried',35)

    def test_age(self):
        self.assertEqual(self.coureur1.age(),45)
        self.assertEqual(self.coureur2.age(),50)
        self.assertEqual(self.coureur3.age(),35)
        self.assertNotEqual(self.coureur3.age(),'35') # string instead of int for age
        self.assertNotEqual(self.coureur3.age(),50)

    def test_nom(self):
        self.assertEqual(self.coureur1.nom(),'Kim')
        self.assertEqual(self.coureur2.nom(),'Charles')
        self.assertEqual(self.coureur3.nom(),'Siegfried')
        self.assertNotEqual(self.coureur3.nom(),'Kim')

    def test_different(self):
        self.assertNotEqual(self.coureur1, self.coureur2)
        self.assertNotEqual(self.coureur2, self.coureur3)
        self.assertNotEqual(self.coureur1, 2)
        self.assertNotEqual(self.coureur1, 'Kim')
        self.assertNotEqual(self.coureur1, Coureur('Kim','45')) # string instead of int for age
        self.assertNotEqual(self.coureur1, Coureur('Kim',50))
        self.assertNotEqual(self.coureur1, Coureur('Charles',45))

    def test_equal(self):
        self.assertEqual(self.coureur1, self.coureur1)
        self.assertEqual(self.coureur1, Coureur('Kim',45))
        self.assertEqual(Coureur('Kim',45),self.coureur1)
        self.assertEqual(Coureur('Kim',45), Coureur('Kim',45))
        self.assertNotEqual(Coureur('Kim',45), Coureur('Kim','45')) # string instead of int for age

# To automatically launch this test when executing this file
if __name__ == '__main__':
    unittest.main()

# To run this test from the command prompt:
#   python -m unittest test_coureur.py
#   python -m unittest test_coureur.CoureurTest
#   python -m unittest test_coureur.CoureurTest.test_equal
# or with more detail (higher verbosity) by passing in the -v flag:
#   python -m unittest -v test_coureur.py
