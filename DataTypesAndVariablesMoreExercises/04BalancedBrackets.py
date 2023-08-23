def balanced_brackets(lines):
    brackets = []
    for _ in range(lines):
        string = input()
        if string == "(" or string == ")":
            brackets.append(string)
    if len(brackets) == 0 or len(brackets) % 2 != 0:
        return "UNBALANCED"
    for idx in range(0, len(brackets) - 1, 2):
        if brackets[idx] != "(" or brackets[idx + 1] != ")":
            return "UNBALANCED"
    return "BALANCED"


number_lines = int(input())
print(balanced_brackets(number_lines))
