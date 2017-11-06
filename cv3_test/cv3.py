def add_line_numbers(filename):
    try:
        orig_file = open(filename, 'r')
        new_file = open('n_' + filename, 'w')
        no_of_line = 1
        for line in orig_file:
            new_file.write(str(no_of_line) + "   " + line)
            no_of_line += 1
        orig_file.close()
        new_file.close()
        print("ok")

    except IOError as e:
            print(e)


def my_filtered_map(lst, fun, **param):
    lst = [x for x in lst if type(x) == int or type(x) == float]
    out_lst = list(map(fun, lst))

    if 'min' in param:
        out_lst = [x for x in out_lst if x >= param['min']]

    if 'max' in param:
        out_lst = [x for x in out_lst if x <= param['max']]
    
    return out_lst
    

def bank_account (*filenames):
        accounts = {}
        open_files = []
        for file in filenames:
            open_files.append(open(file, 'r'))

        for opened_file in open_files:
            for line in opened_file:
                splt_ln = line.split(" ")
                if splt_ln[1] == 'D':
                    if splt_ln[0] in accounts:
                        accounts[splt_ln[0]] += int(splt_ln[2])
                    else:
                        accounts.update({splt_ln[0] : int(splt_ln[2])})
                if splt_ln[1] == 'W':
                    if splt_ln[0] in accounts:
                        accounts[splt_ln[0]] -= int(splt_ln[2])
                    else:
                        accounts.update({splt_ln[0] : -1 * int(splt_ln[2])})
                if splt_ln[1] == 'I':
                    if splt_ln[0] in accounts:
                        accounts[splt_ln[0]] *= (1 + float(splt_ln[2]))
                    else:
                        accounts.update({splt_ln[0] : 0})
        return accounts
                
                
add_line_numbers("text.txt")
print(my_filtered_map ([1,2,3, "x", 5, 8, 13], lambda x: x*2, min=5, max=20))

print(my_filtered_map ([True, -2.2, -1, 0, 1, 2],  lambda x: 2*x, max=0))

print(bank_account("bank_01.txt", "bank_02.txt"))
