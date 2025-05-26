class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # iterate over s and add each 10 letter substring to a dict: {substring: count}
        # as we iterate: new substring is s[r - 9:r + 1]
        # check the dict if the substring we just created has already been seen then it is a repeated sequence
        # return all keys in dict with val > 1 in a list
        res = []
        substrings = defaultdict(int)

        for i in range(len(s) - 9):
            substring = s[i:i+10]
            substrings[substring] += 1
            if substrings[substring] == 2:
                res.append(substring)


        return res
