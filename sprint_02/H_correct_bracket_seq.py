# H correct_bracket_seq

def is_correct_bracket_seq(seq):
    stack = []
    for i in range(len(seq)):
        if len(stack) == 0:
            stack.append(seq[i])
        else:
            if seq[i] in (')', ']', '}'):
                if stack[-1] == '(' and seq[i] == ')':
                    stack.pop()
                elif stack[-1] == '[' and seq[i] == ']':
                    stack.pop()
                elif stack[-1] == '{' and seq[i] == '}':
                    stack.pop()
                else:
                    stack.append(seq[i])
            else:
                stack.append(seq[i])
    return len(stack) == 0


seq = input()
print(is_correct_bracket_seq(seq))