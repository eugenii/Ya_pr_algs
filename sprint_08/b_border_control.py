# Пограничный контроль.
import sys



def check_name(name: str, passport_name: str) -> str:
    if name == passport_name:
        return "OK"
    if abs(len(name) - len(passport_name)) > 1:
        return "FAIL"
    pos_name, pos_passport = 0, 0
    err = 0
    while pos_name < len(name) and pos_passport < len(passport_name):
        if name[pos_name] != passport_name[pos_passport]:
            if err == 1:
                return "FAIL"
            err += 1
            if len(name) > len(passport_name):
                pos_name += 1
            elif len(name) < len(passport_name):
                pos_passport += 1
        pos_name += 1
        pos_passport += 1
    return "OK"


if __name__ == "__main__":

    line = sys.stdin.read().splitlines()

    name = line[0]
    passport_name = line[1]
    print(check_name(name, passport_name))
