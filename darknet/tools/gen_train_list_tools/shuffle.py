import numpy as np
import numpy.random as npr
import os

def shuffle_list(txt_path):
    txt = open(txt_path, 'r')
    lines = txt.readlines()
    nums = len(lines)
    txt.close()
    txt = open(txt_path, 'w')
    keep_lines = npr.choice(nums, size=int(nums),replace=False)

    for i in keep_lines:
        txt.write(lines[i])
    txt.close()

if __name__ == '__main__':
    txt = '../../data/train_list/train_list.txt'
    shuffle_list(txt)

    txt = '../../data/train_list/train_list_cv4aug4.txt'
    shuffle_list(txt)
