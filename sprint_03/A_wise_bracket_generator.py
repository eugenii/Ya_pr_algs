# A генерация ПСП.


def generate_psp(line, open, close):
    if close == 0:
        print(line)
    else:
        if open > 0:
            generate_psp(line + "(", open - 1, close)
        if open < close:
            generate_psp(line + ")", open, close - 1)
        

n = int(input())
generate_psp("", n, n)