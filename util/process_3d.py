import numpy as np

def zpad(img_arr, pad_size=[0,0,0], mode='constant'):
    p_size = pad_size
    if img_arr.ndim>3:
        for i in range(3,img_arr.ndim):
            p_size = p_size + [0]    
    
    p_size = tuple([(size,size) for size in p_size])
    img_arr_n = np.pad(img_arr, p_size, mode)
    return img_arr_n

def zpad2(img_arr, r_size, mode='constant'):
    img_size = np.array(img_arr.shape)
    p_sizeL = np.round((np.array(r_size)-img_size)/2)
    p_sizeR = np.float((np.array(r_size)-img_size)/2)
    p_size  = np.stack([p_sizeL,p_sizeR],axis=1) 
    p_size = tuple(map(tuple,psize))
    
    img_arr_n = np.pad(img_arr, p_size, mode)
    return img_arr_n
    