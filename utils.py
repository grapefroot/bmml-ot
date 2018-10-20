import torch
from torch import nn
import matplotlib.pyplot as plt


def plot_torch_picture(tensor, ax=None):
   # print('tensor shape {}'.format(tensor.size()))
    tensor_to_print = (tensor + 1) / 2
    tensor_to_print = (tensor_to_print * 255).int()
    if ax is None:
#         print(tensor_to_print.squeeze(0).detach().permute(1,2,0))
        plt.imshow(tensor_to_print.squeeze(0).detach().permute(1,2,0).data.numpy())
        plt.axis('off')
        plt.show()
    else:
        ax.axis('off')
#         print(tensor_to_print.squeeze(0).detach().permute(1,2,0).data.numpy())
        ax.imshow(tensor_to_print.squeeze(0).detach().permute(1,2,0).data.numpy())

def draw_interpolation(tensor1, tensor2, n_steps=10, ax=None, do_scale=True):
    ts = torch.linspace(0, 1, steps=n_steps)
    for t in ts:
        yield two_point_interpolation(tensor1, tensor2, t=t, do_scale=do_scale)
