class Solution:
    def intToRoman(self, num: int) -> str:
        hashmap = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M"
        }


        return_str = ""
        vals = sorted(hashmap.keys(), reverse = True)
        for el in vals:
            while el <= num:
                return_str += hashmap[el]
                num -= el
        
        return return_str
