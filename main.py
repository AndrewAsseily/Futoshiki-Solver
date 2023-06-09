from FileOperation import FileOperation
from FutoshikiUtility import FutoshikUtility

heuristic_remainder = [[0] * 5 for x in range(5)]


# initialize each cell of heuristic_remainder
def set_min_rem_val_heuristic():
    heuristic_remainder_len = len(heuristic_remainder)
    index = 0
    while index < heuristic_remainder_len:
        h_l = len(heuristic_remainder[index])
        index2 = 0
        while index2 < h_l:
            heuristic_remainder[index][index2] = {}
            index2 += 1
        index += 1


def main():
    # accept input file from user
    input_file = input("enter file name: ")
    # create instance of FileOperation
    fileOps = FileOperation(input_file)
    # read from input file and initialize game_state, v_constraints and h_constraints
    initial_game_state, v_constraints, h_constraints = fileOps.read_file()

    set_min_rem_val_heuristic()

    # create instance of FutoshikUtility and pass call the constraint
    utility = FutoshikUtility(initial_game_state, h_constraints, v_constraints, heuristic_remainder)
    valid = utility.execute_game(initial_game_state)
    # if game doesn't have valid solution, display user defined message
    if not valid:
        fileOps.write_invalid_solution()
    else:
        fileOps.write_valid_solution(initial_game_state)

# start of program
if __name__ == "__main__":
    main()
