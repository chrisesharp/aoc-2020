import unittest
from allergens import Allergens

class GameTest(unittest.TestCase):
    def test_sum(self):
        data = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
        allergens = Allergens(data.splitlines())
        self.assertEqual(5, allergens.sum())
    
    def test_result(self):
        data = """\
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)"""
        allergens = Allergens(data.splitlines())
        self.assertEqual("mxmxvkd,sqjhc,fvjkl", allergens.pt2())

if __name__ == '__main__':
    unittest.main()