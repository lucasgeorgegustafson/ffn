import sys

def ffn(grammar):
    """
    ffn(grammar) takes a path as argument (grammar) and reads in grammar from
    text file. File should be formatted as follows:

        - First line is whitespace delimited terminal symbols
        - Second line is whitespace delimited non-terminal symbols
        - Remaining lines are productions of the form E xE
        - A production whose right-hand side is the empty string is written
          as a standalone left-hand side. E.g., if the grammar contains the
          production E -> empty string, the production would be represented
          in the text file by a line consisting solely of E

    ffn() computes and prints the grammar's first, follow, and nullable sets.
    """

    with open(grammar) as f:
        gram = f.read().splitlines()
        terms = gram[0].split()
        non_terms = gram[1].split()
        nullable = set()
        first = {}
        follow = {}
        for term in terms:
            first[term] = {term}
        for non_term in non_terms:
            first[non_term] = set()
            follow[non_term] = set()
        nullable_old = set()
        first_old = {}
        follow_old = {}
        while nullable_old != nullable or first_old != first or follow_old != follow:
            nullable_old = nullable.copy()
            first_old = first.copy()
            follow_old = follow.copy()
            for rule in gram[2:]:
                ls = rule[0]
                rs = rule[2:]
                k = len(rs) - 1
                i = 0
                if rs == '':
                    nullable.add(ls)
                while i <= k:
                    sym_i = 0
                    while sym_i < len(rs):
                        if rs[sym_i] in nullable:
                            sym_i += 1
                        else:
                            break
                    if sym_i == len(rs):
                        nullable.add(ls)

                    sym_i = 0
                    while sym_i <= i - 1:
                        if rs[sym_i] in nullable:
                            sym_i += 1
                        else:
                            break
                    if sym_i == i:
                        first[ls] = first[ls] | first[rs[i]]

                    sym_i = i + 1
                    while sym_i <= k:
                        if rs[sym_i] in nullable:
                            sym_i += 1
                        else:
                            break
                    if sym_i == k + 1 and rs[i] not in terms:
                        follow[rs[i]] = follow[rs[i]] | follow[ls]

                    j = i + 1
                    while j <= k:
                        sym_i = i + 1
                        while sym_i < j:
                            if rs[sym_i] in nullable:
                                sym_i += 1
                            else:
                                break
                        if sym_i == j and rs[i] not in terms:
                            follow[rs[i]] = follow[rs[i]] | first[rs[j]]
                        j += 1
                    i += 1
        print("nullable: " + str(nullable))
        print("first: " + str(first))
        print("follow: " + str(follow))

# Run from command line passing path to grammar as argument
if __name__ == '__main__':
    ffn(sys.argv[1])

