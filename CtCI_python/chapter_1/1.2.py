import unittest

def check_permutation(str1, str2):
    if not len(str1) == len(str2):
        return False
    elif sorted(str1) == sorted(str2):
        return True

    return False

class Test(unittest.TestCase):
    test_cases = {
        ("tzdse", "zdset"): True,
        ("abddfw", "dsads"): True,
        ("frgaadf", "dsabjik"): False
    }
    
    def test_check_permutation(self):
        for args, expected in self.test_cases.items():
            assert check_permutation(*args) == expected, f"Failed {check_permutation.__name__} for: {[*args]}"

if __name__ == "__main__":
        unittest.main()

