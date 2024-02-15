"""
Assumptions:
- every character acept for whitespace is taken into calculations
- 
"""
import unittest

#I know it's not working. The solution is Trivial
def is_palindrome_permutation(word):
    assert isinstance(word, str), "Word has to be string"

    word = word.replace(" ", "")
    permit_for_single = False if len(word)%2 == 0 else True
    duplicates_table = dict()

    for letter in word:
        if letter in duplicates_table:
            if duplicates_table[letter]:
                duplicates_table[letter] = False
            else:
                duplicates_table[letter] = True
        else:
            duplicates_table[letter] = True
    
    for key, value in duplicates_table.items():
        if not value:
            if permit_for_single:
                permit_for_single = False
            else:
                return False
    return True #ended there ----------------------

class Test(unittest.TestCase):
    functions_to_test = [is_palindrome_permutation]

    test_cases = {
        "taco cat": True,
        "dfwd": False,
        "dd": True,
        "ddwfw p": False 
    }
    
    def test_check_permutation(self):
        for function in self.functions_to_test:
            for test_case, expected in self.test_cases.items():
                result = function(test_case)
                assert result == expected, f"For: {function.__name__} test case: {test_case} expected: {expected} and instead got: {result}"

if __name__ == "__main__":
        unittest.main()
