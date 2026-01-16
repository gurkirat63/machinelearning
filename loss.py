
import math
from commonutils import print_output

#--------------------------------------------------------LOSS FUNCTIONS----------------------------------------------------

@print_output
def mse_loss(y_true:list, y_pred:list):
    if len(y_true) != len(y_pred):
        return False
    return sum([(i-j)**2 for i,j in zip(y_true, y_pred)]) / len(y_true)

@print_output
def mae_loss(y_true:list, y_pred:list):
    if len(y_true) != len(y_pred):
        return False
    return sum([abs(i-j) for i,j in zip(y_true, y_pred)]) / len(y_true)

@print_output
def binary_crossentropy_loss(y_true:list, y_pred:list):
    eps = 1e-10
    out_list = [-1 * ((y_i*math.log(p_i+eps) + (1-y_i)*math.log(1-p_i+eps))) for y_i,p_i in zip(y_true,y_pred)]
    out = sum(out_list)
    return out

@print_output
def crossentropy_loss(y_true:list, y_pred:list):
    eps = 1e-10
    out_list = [-1 * ((y_i*math.log(p_i+eps) + (1-y_i)*math.log(1-p_i+eps))) for y_i,p_i in zip(y_true,y_pred)]
    out = sum(out_list)
    return out

