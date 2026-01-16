
import math
import random

class Matrix:
    def __init__(self, nrows, ncols, use_random=False, state=42):
        self.nrows = nrows
        self.ncols = ncols
        self.use_random = use_random
        self.state = state

        if self.use_random:
            self.data = [[random.uniform(-100,100) for _ in range(self.ncols)] for _ in range(self.nrows)]
        else:
            self.data = [[0.0 for _ in range(self.ncols)] for _ in range(nrows)]
       

def transpose(mat: Matrix):  
    out = Matrix(mat.ncols, mat.nrows, use_random=False) # swapped rows and columns sizes
    for i in range(mat.nrows):
        for j in range(mat.ncols):
            out.data[j][i] = mat.data[i][j]
    return out 


def matmul(mat_a:Matrix, mat_b:Matrix):
    if mat_a.ncols != mat_b.nrows:
        return False
    out = Matrix(mat_a.nrows, mat_b.ncols, use_random=False)
    for i in range(mat_a.nrows):
        for b in range(mat_b.ncols):
            sum_items = 0
            for j in range(mat_a.ncols):
                sum_items += mat_a.data[i][j] * mat_b.data[j][b]
            out.data[i][b] = sum_items
    return out

def scale(mat:Matrix, factor:float):
    out = Matrix(mat.nrows, mat.ncols, use_random=False) # swapped rows and columns sizes
    for i in range(mat.nrows):
        for j in range(mat.ncols):
            out.data[i][j] = factor * mat.data[i][j]
    return out        

def relu(mat:Matrix):
    out = Matrix(mat.nrows, mat.ncols, use_random=False) # swapped rows and columns sizes
    for i in range(mat.nrows):
        for j in range(mat.ncols):
            out.data[i][j] = max(0,mat.data[i][j])
    return out        

def softmax(mat: Matrix):
    out = Matrix(mat.nrows, mat.ncols, use_random=False) # swapped rows and columns sizes
    sum_exp = 0.0
    for i in range(mat.nrows):
        for j in range(mat.ncols):
            exp_term = math.exp(mat.data[i][j])
            sum_exp+=exp_term
            out.data[i][j] = exp_term
    for i in range(mat.nrows):
        for j in range(mat.ncols):
            out.data[i][j] = out.data[i][j]/sum_exp
    return out



mat1 = Matrix(2,3,use_random=True) 
mat2 = Matrix(2,3,use_random=True) 
mat2 = transpose(mat2)

print("printing Matmul out")
mat_out = matmul(mat1, mat2)
print(mat_out.data)

print("print mat1")
print(mat1.data)

print("Printing Relu output: ")
print(relu(mat1).data)

print("Printing softmax output: ")
print(softmax(relu(mat1)).data)