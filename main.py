import importlib
import sys


SCRIPTS_DIR = "days"


def get_script_name(p):
    return f"day{p}"


def get_module(p):
    try:
        sys.path.append(SCRIPTS_DIR)
        m = importlib.import_module(get_script_name(p))
        return m
    except ModuleNotFoundError:
        if sys.path[-1] == SCRIPTS_DIR:
            sys.path.pop()
        print("Could not find module:", f"{SCRIPTS_DIR}/{get_script_name(p)}")
        return None


if __name__ == '__main__':
    problem = None
    while not problem:
        try:
            problem = get_module(int(input()))
        except ValueError:
            print("Not a valid positive integer (day may not be implemented yet), try again: ")

    problem.solve()
