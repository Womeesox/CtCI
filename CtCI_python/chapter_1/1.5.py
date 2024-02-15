import unittest

def is_one_away(string1, string2):
    one_away_permit = True

    if len(string1) < len(string2):
        string1 = string2
        string2 = string1

    #if this won't be present we get out of index error for string2[0]
    if len(string1) == 1 and len(string2) == 0:
        return True

    if abs(len(string1) - len(string2)) == 1:
        string1 = list(string1)
        string2 = list(string2)

        for counter, letter1 in enumerate(reversed(string1)):
            print(string1)
            try:
                letter2 = string2[-(counter + 1)]
            except IndexError:
                    if string1[0] == string2[0]: #if loop is at last iteration and didn't throw error it's good
                        return True
                    else: #we have to check for last element cuz it's not checked
                        return False

            if letter1 != letter2:
                if one_away_permit:
                    one_away_permit = False
                    del string1[-(counter+1)]
                else:
                    return False
        return True

    elif len(string1) - len(string2) == 0:            
        for letter1, letter2 in zip(string1, string2):
            if letter1 != letter2:
                if one_away_permit:
                    one_away_permit = False
                    continue
                return False
        return True
    else:
        return False
    

class Test(unittest.TestCase):
    functions_to_test = [is_one_away]

    test_cases = {
        ("ple", "pale"): True,
        ("bale", "pale"): True,
        ("dupa", "gupe"): False,
        ("abc", "abc"): True,
        ("xdfs dfa", "dfwaga"): False,
        ("", ""): True,
        (".", ""): True
    }
    
    def test_check_permutation(self):
        for function in self.functions_to_test:
            for test_case, expected in self.test_cases.items():
                result = function(*test_case)
                assert result == expected, f"For: {function.__name__} test case: {test_case} expected: {expected} and instead got: {result}"

if __name__ == "__main__":
        unittest.main()