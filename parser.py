""" Retourne une liste de liste avec le problème """
def ccf_parser(path):
    instance, comment = [], []
    n, m, i = 0, 0, 0
    with open(path, 'r') as ccf:
        data = ccf.readlines()
        # Récupération des paramètres
        for line in data:
            if line[0] == "c":
                comment.append(line)
                i += 1
                continue
            elif line[0] == "p":
                n = line[6]
                m = line[8]
                i += 1
                break
            else:
                print("ERROR: CCF File has a problem with c/p")


        # Récupération des clauses
        for line in data[i:]:
            if line == "\n":
                break
            j = 0
            clause = []
            while line[j] != "0":
                if line[j] == "-":
                    clause.append(int(line[j] + line[j+1]))
                    j += 3
                    continue
                elif line[j].isdigit():
                    clause.append(int(line[j] + line[j + 1]))
                    j += 2
                else:
                    print("ERROR: CNF File has a problem with clauses")
                    j += 1
            instance.append(clause)
            continue

    for line in comment:
        print(line, sep="")
    return instance
