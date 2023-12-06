import importlib
import sys


SCRIPTS_DIR = "days"
INPUTS_DIR = "input"


def get_script_name(p):
    return f"day{p}"


def get_input_path(p):
    return f"{INPUTS_DIR}/iday{p if 'p' not in p else p.split('p')[0]}.txt"


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
            inp = input("Enter day (with p2 for second part of day): ")
            problem = get_module(inp)
            input_file = open(get_input_path(inp), 'r')
        except ValueError:
            print("Cannnot find module or input (day may not be implemented yet), try again: ")

    problem.solve(input_file)
    input_file.close()
