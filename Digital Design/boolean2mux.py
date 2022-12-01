

def generate_last2_row(variable_num,boolean_eq):
    out = []
    for i in range(2**variable_num):
        out.append([i%2,boolean_eq[i]])
    return out

def autofillboolean(boolean_equation_list, variable_num):
    out = [1 if t in boolean_equation_list else 0 for t in range(2**variable_num)]
    return out

def solve(boolean_equation_list, variable_list, variable_num):
    out = []
    last2_row = generate_last2_row(variable_num,autofillboolean(boolean_equation_list, variable_num))
    for i in range(0,2**variable_num,2):
        #four cases
        #case 1 : always 0
        if last2_row[i][1] == last2_row[i+1][1] == 0:
            out.append('0')
        #case 2 : always 1
        elif last2_row[i][1] == last2_row[i+1][1] == 1:
            out.append('1')
        #case 3 : list[-1]
        elif (last2_row[i][1] != last2_row[i+1][1]) and (last2_row[i][1] == last2_row[i][0]) and (last2_row[i+1][1] == last2_row[i+1][0]):
            out.append(f"{variable_list[-1]}")
        #case 4 : ~ list[-1]
        else:
            out.append(f"~{variable_list[-1]}")
    return out

def boolean2mux(boolean_equation_list, variable_list, variable_num):
    out = []
    out.append(solve(boolean_equation_list, variable_list, variable_num))
    return out

if __name__ == '__main__':
    variable_num = int(input("Enter the number of variables: "))
    variable_list = list(map(str,input("Enter the variable list: ").split()))
    print(f"variable_list: {variable_list}")
    boolean_equation_list = list(map(int, input("Enter the boolean equation: ").split()))
    print(f"boolean_equation_list: {boolean_equation_list}")
    out_temp = boolean2mux(boolean_equation_list, variable_list, variable_num)
    s_list = []
    for i in range(variable_num-1):
        s_list.append(f"{variable_list[i]}")
    print(f"mux({','.join(s_list)},{','.join(out_temp[0])})")