"""Note: 

Problem: 
    Given a string, return the reversed string with vowels as uppercase and consonants as lowercase. 
        
"""


class ReverseStringWithModification:
    """String Reverse with Vowels as Uppercase and Consonants are Lowercase."""

    def reverse_str(self, inp_str: str) -> str:
        """Using Two-Pointers to reverse the string.

        @param: inp_str - a string with alphabts

        Time Complexity: O(n)

        Space Complexity: O(n)

        Why O(n) Space Complexity:
                - String in python is immutable, hence a complementary space is needed to modify the string.
        """

        inp_str_lst = list(inp_str)

        start = 0
        end = len(inp_str_lst) - 1

        while start < end:
            inp_str_lst[start], inp_str_lst[end] = inp_str_lst[end], inp_str_lst[start]

            start += 1
            end -= 1

        return "".join(inp_str_lst)

    def modify_str(self, inp_str: str) -> str:
        """'Modify the input string based on vowel and consonant

        @param: inp_str - a string with alphabts

        Condition:
                uppercase: character is vowel
                lowercase: character is consonant

                - The method assumes that the string only contains "alphabets" as how to handle
                not alphabetic characters are not mentioned

        Time Complexity: O(n)

        Space Complexity: O(1)
                - Although a set of 10 constants are used, but it's nominal.

        Why set is used:
                - The TC of membership checking of set is O(1)
        """
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        res_str = ""

        # Reverse string. Ex: Hello World => dlroW olleH
        inp_str = self.reverse_str(inp_str=inp_str)

        for ch in inp_str:
            if ch in vowels:
                res_str += ch.upper()
            else:
                res_str += ch.lower()

        return res_str

    def run(self, inp_str: str) -> str:
        """Entrypoint method to Reverse a String with vowels as uppercase and consonats as loweracase.

        @param: inp_str - a string with alphabts
        """

        return self.modify_str(inp_str=inp_str)


string_reverser = ReverseStringWithModification()


def main(inp_str: str):
    reversed_string = string_reverser.run(inp_str=inp_str)

    print("\nThe Reversed String is: ", reversed_string, "\n")


if __name__ == "__main__":
    inp_str = input("Input Str for Reversal: ")

    main(inp_str=inp_str)
