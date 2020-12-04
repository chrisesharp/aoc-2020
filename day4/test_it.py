import unittest
from pass_check import valid, total_valid

class GameTest(unittest.TestCase):
    def test_check_fields(self):
        passport1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm
"""     
        passport2 = """iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929"""
        self.assertTrue(valid(passport1))
        print("===========")
        self.assertFalse(valid(passport2))
    
    def test_batch_check(self):
        passports = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""
        total_valid = 0
        for passport in passports.split("\n\n"):
            total_valid += valid(passport)
        self.assertEqual(2, total_valid)

    def test_file_load(self):
        data = open("test.txt","r").read()
        self.assertEqual(2, total_valid(data))


if __name__ == '__main__':
    unittest.main()
