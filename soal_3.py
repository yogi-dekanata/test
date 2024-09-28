def validate_string(s):
    """
    Validates if the input string has matching opening and closing brackets and is correctly nested.
    """
    # Stack to store opening brackets
    stack = []

    # Mapping of closing brackets to corresponding opening brackets
    matching_bracket = {
        '>': '<',
        '}': '{',
        ']': '['
    }

    # Ensure input length is between 1 and 4096
    if not (1 <= len(s) <= 4096):
        return False

    # Loop through each character in the string
    for char in s:
        if char in matching_bracket.values():  # If it's an opening bracket
            stack.append(char)
        elif char in matching_bracket:  # If it's a closing bracket
            if not stack or stack[-1] != matching_bracket[char]:  # Check if it matches the last opening bracket
                return False
            stack.pop()  # Pop the matched opening bracket
        else:
            # Invalid character found (not a valid bracket)
            return False

    # After loop, check that the stack is empty (all brackets are matched)
    return len(stack) == 0



if __name__ == "__main__":
    print(validate_string("{{[<>[{{}}]]}}"))
    print(validate_string("{}<>"))
    print(validate_string("[<{<{[{[{}[[<[<{{[<[<[[[<{{[<<<[[[<[<{{[<<{{<{<{<[<{["))
