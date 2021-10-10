#SVD - SINGULAR VALUE DESCOMPOSITION
import numpy as np
from PIL import Image
import pandas as pd
import os
import matplotlib.pyplot as plt


#SICK CATTLE
#File Upload Sick Cattle
path_Enfermos = r'C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\enfermo_csv'
names = os.listdir(path_Enfermos)
n = 0
n2 = 0
for i in names:   
    n += 1
#Zero array
lista_dfE = [0]*(n+1)
path_Enfermos = r'C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\enfermo_csv'
#print(os.listdir(path_Enfermos))
for i in names:   
    archivo = pd.read_csv(r'''C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\enfermo_csv\{}'''.format(i))
    lista_dfE [n2] = (archivo)
    n2 +=1
#print(lista_dfE,[0,1])

# HEALTHY CATTLE
#File Upload Sick Cattle
path_Sanos = r'C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\sano_csv'
names_sanos = os.listdir(path_Sanos)
n_sanos = 0
n2_sanos = 0
for i in names_sanos:   
    n_sanos += 1
#Zero array
lista_dfS = [0]*(n_sanos+1)
path_Sanos= r'C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\sano_csv'
#print(os.listdir(path_Enfermos))
for i in names_sanos:   
    archivo_sanos = pd.read_csv(r'''C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\sano_csv\{}'''.format(i))
    lista_dfS [n2_sanos] = (archivo_sanos)
    n2_sanos +=1
#print(lista_dfS,[0,1])


def decompress(arr):
    img = np.matrix(arr)
    U, sigma, V = np.linalg.svd(img)
    reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
    plt.imshow(reconstimg, cmap='gray');
    for i in range(2, 4):
        reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap='gray')
        title = "n = %s" % i
        plt.title(title)
    plt.show()
    for i in range(5, 51, 5):
        reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap='gray')
        title = "n = %s" % i
        plt.title(title)
        plt.show()
        
#LOAD THE IMAGE
img = Image.open('image_1.jpg')
file = 'image_1.jpg'
#Decompression
decompress(lista_dfS[1]) 

def img_matriz(img):
    
    imge_2 = img.convert('LA')
    matrix_1 = np.array(list(imge_2.getdata(band=0)), float)
    print(matrix_1)
    matrix_1.shape = (imge_2.size[1], imge_2.size[0])
    print(matrix_1.shape)
    mat = np.matrix(matrix_1)
    plt.figure(figsize=(9,6))
    plt.imshow(mat, cmap='gray');
    return mat
    
def compress(img):
    matrix_2 = img_matriz(img)
    U, sigma, V = np.linalg.svd(matrix_2)
    img_reconst = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
    plt.imshow(img_reconst , cmap='gray');
    for i in range(2, 4):
        img_reconst  = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(img_reconst , cmap='gray')
        title = "n = %s" % i
        plt.title(title)
    if(i==3):
        img.save("Compressed_"+file,"JPEG",optimize=True,quality=85)
    plt.show()
    for i in range(5, 51, 5):
        img_reconst  = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(img_reconst , cmap='gray')
        title = "n = %s" % i
        plt.title(title)
        plt.show()
#Compression
compress(img) 