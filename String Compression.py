class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars): # iterate through the array 
            char = chars[read]
            count = 0

            # Count occurrences of current char
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the char
            chars[write] = char
            write += 1

            # Write the count if more than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
