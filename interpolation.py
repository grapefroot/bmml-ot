import torch
from torch import nn
import numpy as np

def two_point_interpolation(tensor1, tensor2, t=0.5, do_scale=True):
    assert tensor1.size() == tensor2.size()
    #computes convex combination of 2 points
    scaling_factor = (t**2 + (1 - t)**2)**0.5
    resulting_tensor = (t * tensor1 + (1 - t) * tensor2)
    if do_scale:
  #      print(scaling_factor)
        return resulting_tensor / scaling_factor
    else:
        return resulting_tensor

def n_point_interpolation(value_tensor, coef_tensor, do_scale=True):
    assert coef_tensor.sum(0) == 1
    scaling_factor = (coef_tensor**2).sum(0)**0.5
    resulting_tensor = value_tensor.sum(0)
    if do_scale:
        return resulting_tensor / scaling_factor
    else:
        return resulting_tensor

def vicinity_sampling(initial_tensor, shift_tensor, eps, do_scale=True):
    assert initial_tensor.size() == shift_tensor.size()
    resulting_tensor = initial_tensor + eps * shift_tensor
    scaling_factor = (1 + eps**2)**0.5
    if do_scale:
#       print('scale')
        return resulting_tensor / scaling_factor
    else:
 #       print('no scale')
        return resulting_tensor

def analogies(tensor3, tensor2, tensor1, do_scale=True):
    assert tensor3.size() == tensor2.size() == tensor1.size()
    resulting_tensor = tensor3 + (tensor2 - tensor1)
    scaling_factor = 3**0.5
    if do_scale:
        return resulting_tensor / scaling_factor
    else:
        return resulting_tensor

def gaussian_interpolation(mu_0, sigma_0, mu_1, sigma_1, t=0.5):
    mu_new = t * mu_0 + (1 - t) * mu_1
    
    sigma_0_root = torch.diag(torch.sqrt(Sigma_0))
    sigma_0_root_inv = 1 / sigma_0_root
    sigma_1_root = torch.diag(torch.sqrt(Sigma_1))
    sigma_1_root_inv = 1 / sigma_1_root
    
    middle_part = (t * torch.diag(sigma_0) + 
                   (1 - t) * torch.sqrt(sigma_0_root * sigma_1 * sigma_1_root))**2
        
    sigma_new = sigma_0_root_inv * middle_part * sigma_0_root_inv
    return sigma_new
