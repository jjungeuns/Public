# 20220160 Jungeun Kim

# Define the operation
E = {1:1, 2:2, 3:3, 'name':'E'}
D = {1:3, 2:1, 3:2, 'name':'D'}
F = {1:2, 2:3, 3:1, 'name':'F'}
A = {1:1, 2:3, 3:2, 'name':'A'}
B = {1:3, 2:2, 3:1, 'name':'B'}
C = {1:2, 2:1, 3:3, 'name':'C'}
dict_P3 = [E, D, F, A, B, C]


# Define the product between two operation
def prod(X, Y) :    # X acts first, Y acts last.
    temp_list = []
    for i in [1, 2, 3] :
        temp_list.append(Y[X[i]])

    for Z in dict_P3 :
        if [Z[1], Z[2], Z[3]] == temp_list : # If there is a operation in the P(3) that matches with the product result, return the operation.
            return Z

# prod(A, D)


# check Associativity
num = 0
for P in dict_P3 :
    for Q in dict_P3 :
        for R in dict_P3 :
            # Compare P(QR) = (PQ)R
            if prod(P, prod(Q, R)) == prod(prod(P, Q), R) :
                print("True")
            else :
                print("False")



# To print the result within an equation
num = 0
for P in dict_P3 :
    for Q in dict_P3 :
        for R in dict_P3 :
            
            string = "{}: {}({}{}) = {}{} = {} = {}{} = ({}{}){} &".format(
                num+1, P['name'], Q['name'], R['name'], P['name'], prod(Q, R)['name'], prod(P, prod(Q, R))['name'], prod(P, Q)['name'], R['name'], P['name'], Q['name'], R['name']
            )
            if num%3 == 2 and num != 0 :
                string = string[:-1]
                string += "\\\\"

            print(string)
            num += 1
