def load_values(file):
    values = []
    variables_size = 0
    clauses_size = 0
    max_var = 0
    clause = list()
    with open(file, "r") as ins:
        array = []
        for line in ins:
            if len(line) < 2:
                continue
            if line[0] == 'c':
                continue
            if line[0] == 'p':
                problem_line = line.split(" ")
                variables_size = int(problem_line[2])
                clauses_size = int(problem_line[3])
                continue

            line = ' '.join(line.split())
            splitted = line.split(" ")
            for num_str in splitted:
                num = int(num_str)
                if num == 0:
                    values.append(clause)
                    clause = []
                else:
                    clause.append(num)
    return values, variables_size, clauses_size