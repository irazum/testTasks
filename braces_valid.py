
def braces_valid_check(string: str):
    braces_couples = {')': '(', ']': '[', '}': '{'}
    stack = list()

    for symb in string:
        if symb in braces_couples.values():
            stack.append(symb)
        elif symb in braces_couples.keys():
            try:
                if braces_couples[symb] != stack.pop():
                    return False
            except IndexError:
                return False
    return len(stack) == 0


if __name__ == "__main__":
    print(braces_valid_check(input("input: ")))
