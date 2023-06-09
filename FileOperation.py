import re


class FileOperation:
    # constructor
    def __init__(self, fileName):
        self.fileName = fileName
        self.initial_game_state = [["0"] * 5 for x in range(5)]
        self.h_constraints = [["0"] * 4 for x in range(5)]
        self.v_constraints = [["0"] * 5 for x in range(4)]

    # return file number from file name
    def get_numbers_from_filename(self, filename):
        return re.search(r'\d+', filename).group(0)

    # write final valid solution to a text file
    def write_valid_solution(self, output):
        f_number = self.get_numbers_from_filename(self.fileName)
        solution = self.build_final_solution(output)
        output_file_Name = "Output" + str(f_number) + ".txt"
        f = open(output_file_Name, "w+")
        f.write(solution)
        f.close()

    # iterate over each row and column
    def build_final_solution(self, output):
        solution = ""
        len1 = len(output)
        index = 0
        while index < len1:
            index2 = 0
            len2 = len(output[index])
            while index2 < len2:
                solution += output[index][index2] + " "
                index2 += 1
            solution = solution.rstrip()
            solution += "\n"
            index += 1
        return solution

    # write invalid solution to a text file
    def write_invalid_solution(self):
        f_number = self.get_numbers_from_filename(self.fileName)
        output_file_Name = "Output" + str(f_number) + ".txt"
        f = open(output_file_Name, "w+")
        f.write("No Solution")
        f.close()

    # read from text file and build constraint
    def read_file(self):
        x = []
        f = open(self.fileName, "r")
        file_value = f.read()

        # Remove spaces from data
        file_value = self.remove_space(file_value, x)
        input_sec = file_value.split("\n\n")
        self.build_game_state(input_sec)
        # build horizontal_conditions
        self.build_h_constraints(input_sec)
        # build vertical_conditions
        self.build_v_constraints(input_sec)
        return self.initial_game_state, self.v_constraints, self.h_constraints

    # remove space
    def remove_space(self, file_value, x):
        file_len = len(file_value.split("\n"))
        index = 0
        while index < file_len:
            val = file_value.split("\n")[index].rstrip()
            x.append(val)
            index += 1
        file_value = "\n".join(x)
        return file_value

    # build game state from input
    def build_game_state(self, input_sec):
        game_b_r = input_sec[0].split("\n")
        index = 0
        while index < 5:
            game_b_c = game_b_r[index].split(" ")
            index2 = 0
            while index2 < 5:
                self.initial_game_state[index][index2] = game_b_c[index2]
                index2 += 1
            index += 1

    # build horizontal_conditions
    def build_h_constraints(self, input_sec):
        hc_row = input_sec[1].split("\n")
        index = 0
        while index < 5:
            hc_col = hc_row[index].split(" ")
            index2 = 0
            while index2 < 4:
                self.h_constraints[index][index2] = hc_col[index2]
                index2 += 1
            index += 1

    # build vertical_conditions
    def build_v_constraints(self, input_sec):
        vc_row = input_sec[2].split("\n")
        index = 0
        while index < 4:
            vc_col = vc_row[index].split(" ")
            index2 = 0
            while index2 < 5:
                self.v_constraints[index][index2] = vc_col[index2]
                index2 += 1
            index += 1
