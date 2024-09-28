from abc import ABC, abstractmethod


class StringComparator(ABC):
    """
    Abstract class that defines the contract for string comparison.
    """

    @abstractmethod
    def compare(self, str1, str2):
        """
        Compare two strings based on a specific rule.

        :param str1: First string to compare.
        :param str2: Second string to compare.
        :return: True if strings are considered equal, False otherwise.
        """
        pass


class CaseInsensitiveComparator(StringComparator):
    """
    A case-insensitive string comparison implementation.
    """

    def compare(self, str1, str2):
        """
        Compare two strings in a case-insensitive manner.

        :param str1: First string to compare.
        :param str2: Second string to compare.
        :return: True if strings are equal ignoring case, False otherwise.
        """
        if len(str1) != len(str2):
            return False

        # Compare each character case-insensitively
        for i in range(len(str1)):
            if str1[i].lower() != str2[i].lower():
                return False
        return True


class StringMatcher:
    """
    Responsible for finding matching strings based on the provided comparator.
    """

    def __init__(self, comparator: StringComparator):
        """
        Initialize StringMatcher with a specific comparator.

        :param comparator: An instance of StringComparator to define the comparison rule.
        """
        self.comparator = comparator

    def find_first_matching_set(self, string_list):
        """
        Find the first set of matching strings in the list.

        :param string_list: A list of strings to be compared.
        :return: A list of indices (1-based) of matching strings, or False if no matches are found.
        """
        n = len(string_list)
        for i in range(n):
            matching_indices = [i + 1]  # Store the index of the first string
            for j in range(i + 1, n):
                if self.comparator.compare(string_list[i], string_list[j]):
                    matching_indices.append(j + 1)

            if len(matching_indices) > 1:
                return matching_indices
        return False


class InputHandler:
    """
    Responsible for handling input and output operations.
    """

    def get_input(self):
        """
        Prompt the user for input, including the number of strings and the strings themselves.

        :return: A list of strings provided by the user.
        """
        n = int(input("Enter the number of strings: "))
        string_list = []
        for i in range(n):
            string_input = input(f"Enter string {i + 1}: ")
            string_list.append(string_input)
        return string_list

    def display_result(self, result):
        """
        Display the result of the string matching operation.

        :param result: A list of indices (1-based) or False if no matches are found.
        """
        if result:
            print(" ".join(map(str, result)))
        else:
            print("false")


def main():
    """
    The main function that orchestrates the input, matching, and output.
    """
    input_handler = InputHandler()
    string_list = input_handler.get_input()

    comparator = CaseInsensitiveComparator()
    matcher = StringMatcher(comparator)

    result = matcher.find_first_matching_set(string_list)
    input_handler.display_result(result)


if __name__ == "__main__":
    main()
