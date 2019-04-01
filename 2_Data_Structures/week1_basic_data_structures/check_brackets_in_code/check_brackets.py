# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def find_mismatch(text):
    stack = []
    for i, char in enumerate(text):
        val = Bracket(char, i + 1)
        if val[0] in '([{':
            stack.append(val)
        else:
            if val[0] in '}])':
                if len(stack) == 0:
                    return val[1]
                else:
                    top = stack.pop()
                    if ((top[0] == '[' and val[0] != ']') or
                            (top[0] == '(' and val[0] != ')') or
                            (top[0] == '{' and val[0] != '}')):
                           return val[1]
    return 'Success' if len(stack) == 0 else stack[-1][1]


def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()

