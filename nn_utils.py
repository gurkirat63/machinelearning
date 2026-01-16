from commonutils import print_output
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
       
@print_output
def transpose(mat: Matrix):  
    out = Matrix(mat.ncols, mat.nrows, use_random=False) # swapped rows and columns sizes
    for i in range(mat.nrows):
        for j in range(mat.ncols):
            out.data[j][i] = mat.data[i][j]
    return out 

@print_output
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

@print_output
def scale(mat:Matrix, factor:float):
    out = Matrix(mat.nrows, mat.ncols, use_random=False) # swapped rows and columns sizes
    for i in range(mat.nrows):
        for j in range(mat.ncols):
            out.data[i][j] = factor * mat.data[i][j]
    return out        

@print_output
def relu(x):
    if isinstance(x,Matrix):
        out = Matrix(x.nrows, x.ncols, use_random=False) # swapped rows and columns sizes
        for i in range(x.nrows):
            for j in range(x.ncols):
                out.data[i][j] = max(0,x.data[i][j])
        return out
    elif isinstance(x,int):
        return max(0,x)

@print_output
def sigmoid(x:int):
    num = math.exp(x)
    den = 1 + num
    return num/den

@print_output
def softmax(x):
    if isinstance(x, list):
        max_x = max(x)
        num = [math.exp(i-max_x) for i in x] # make it numerically stable for very large values
        den = sum(num)
        return [item/den for item in num]
    elif isinstance(x,Matrix):
        out = Matrix(x.nrows, x.ncols, use_random=False) # swapped rows and columns sizes
        sum_exp = 0.0
        for i in range(x.nrows):
            for j in range(x.ncols):
                exp_term = math.exp(x.data[i][j])
                sum_exp+=exp_term
                out.data[i][j] = exp_term
        for i in range(x.nrows):
            for j in range(x.ncols):
                out.data[i][j] = out.data[i][j]/sum_exp
        return out







