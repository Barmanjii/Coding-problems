"""
  ### Daily Coding Problem: Problem #809 [Easy]

  This problem was asked by Facebook.

  Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

  For example, given the string "([])[]({})", you should return true.

  Given the string "([)]" or "((()", you should return false.

"""


def main(*, data: str):
    # we can use a stack to keep track of item and pop as we find the corresponding other
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in data:
        if char in mapping.values():  # as we find opening bracket push them into the stack
            stack.append(char)
        elif char in mapping.keys():
            # if we find closing bracket and stack is not empty and these are equal to the last pushed data into the stack then we can we found one pair and just pop the last item with that we have a empty stack.
            if stack and mapping[char] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            continue
    return not stack


if __name__ == "__main__":
    user_input_string = input(
        "Provide the string to check whether they are in complete form of brackets or not:- ")
    print(main(data=user_input_string))
