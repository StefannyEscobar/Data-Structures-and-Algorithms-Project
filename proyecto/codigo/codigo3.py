import numpy as np
from PIL import Image
import pandas as pd
import os
import matplotlib.pyplot as plt
import time

def namesCSV(path):
    names = os.listdir(path)
    return names

#Load csv files (Sick cattle)
def loadCSV_Sick(name):
    archivo = pd.read_csv(r'''C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\enfermo_csv\{}'''.format(name))
    return archivo

#Load csv files (Sick cattle)    
def loadCSV_Healthy(name):
    archivo = pd.read_csv(r'C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\sano_csv\{}'.format(name))
    return archivo

#Lossy compression
##SVD - SINGULAR VALUE DESCOMPOSITION
def decompress(arr):
    inicialTime = time.time()
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
        plt.imshow(reconstimg, cmap ='gray')
        title = "n = %s" % i
        plt.title(title)
        plt.show()
    finalTime = time.time()
    print("Time: ", finalTime - inicialTime)

def img_matriz(img):
    #Convert to grayscale
    imge_2 = img.convert('LA')
    matrix_1 = np.array(list(imge_2.getdata(band=0)), float)
    print(matrix_1)
    matrix_1.shape = (imge_2.size[1], imge_2.size[0])
    print(matrix_1.shape)
    mat = np.matrix(matrix_1)
    plt.figure(figsize=(9,6))
    plt.imshow(mat, cmap='gray');
    return mat
    
def compress_loss(img):
    inicialTime = time.time()
    matriz = img_matriz(img)
    U, sigma, V = np.linalg.svd(matriz)
    reconstimg = np.matrix(U[:, :1]) * np.diag(sigma[:1]) * np.matrix(V[:1, :])
    plt.imshow(reconstimg, cmap='gray');
    for i in range(2, 4):
        reconstimg = np.matrix(U[:, :i]) * np.diag(sigma[:i]) * np.matrix(V[:i, :])
        plt.imshow(reconstimg, cmap= 'gray')
        title = "n = %s" % i
        plt.title(title)
    plt.show()
    finalTime = time.time()
    print("Time: ", finalTime - inicialTime)
    
#Lossless compression
# HUFFMAN COMPRESSION
def huffmanEncode(alfa, prob, s):
    final = []
    
    for i in range(len(alfa)):
        final.append([alfa[i], prob[i]])
    final.sort(key = lambda x: x[1])
    tot = 0
    tree = []
    for i in range(len(final) - 1):
        i = 0
        left = final[i]
        final.pop(i)
        right = final[i]
        final.pop(i)
        tot = left[1] + right[1]
        tree.append([left[0], right[0]])
        final.append([left[0] + right[0], tot])
        final.sort(key = lambda x: x[1])
    code = []
    tree.reverse()
    alfa.sort()
    for i in range(len(alfa)):
        cd = ""
        for j in range(len(tree)):
            if alfa[i] in tree[j][0]:
                cd = cd + '0'
                if alfa[i] == tree[j][0]:
                    break
            else:
                cd = cd + '1'
                if alfa[i] == tree[j][1]:
                    break
        code.append([alfa[i],cd])
    encode = ""
    print("Huffman coding")
    print("Alphabet", end = "\n")
    print("Word -- code")
    for i in range(len(code)):
        print(code[i][0], end = "\t\t")
        print(code[i][1])
    for i in range(len(s)):
        for j in range(len(code)):
            if s[i] == alfa[j][0]:
               encode = encode + str(code[j][1])
    print("Huffman coding for " + s + " is " + encode)
    return [encode, code]


def huffman_decode(master_file):
    encode = list(master_file[0])
    code = master_file[1]
    string = ""
    count = 0
    flag = 0
    for i in range(len(encode)):
        for j in range(len(code)):
            if encode[i] == code[j][1]:
                string = string + str(code[j][0])
                flag = 1
        if flag == 1:
            flag = 0
        else:
            count = count + 1
            if count == len(encode):
                break
            else:
                encode.insert(i + 1,str(encode[i] + encode[i + 1]))
                encode.pop(i + 2)
    print("String decoded for" + str(master_file[0]) + " is " + string)

def toString(arr):
    for car in arr:
        car = str(car)
    return arr

def huffman_decompress(arr):
    #To get the time
    inicialTime= time.time()
    image_string = toString(arr)
    
    string = str(image_string)
    len_str = len(string)
    d1 = dict()
    for i in string:
        if i in d1:
            d1[i] = d1[i] + 1
        else:
            d1[i] = 1
    alphabet = []
    prob = []
    for i in d1.items():
        alphabet.append(i[0])
        prob.append(i[1])
    for i in range(len(prob)):
        prob[i] = prob[i] / len_str
    file = huffmanEncode(alphabet, prob, string)
    huffman_decode(file)
    finalTime = time.time()
    print("Time",finalTime - inicialTime)
    import numpy
    numpo = numpy.array(arr)
    plt.imshow(numpo, cmap="gray")
    plt.savefig("huffmanCoding.jpg")
    plt.show() 

def main():
    path_Sick = r'C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\enfermo_csv'
    path_Healthy = r'C:\Users\ASUS\OneDrive - Universidad EAFIT\ST0245-Eafit\proyecto\datasets\csv\sano_csv'
    namelist_Sick = namesCSV(path_Sick)
    namelist_Healthy = namesCSV(path_Healthy)
    archivo1 = loadCSV_Sick(namelist_Sick[0])
    archivo2 = loadCSV_Healthy(namelist_Healthy[0])
    #print(archivo1)
    #LOAD THE IMAGE
    img = Image.open(r'F:\2021-2\DATOS Y ALGORITMOS\Entrega 3\image_1.jpg')
    file = r'F:\2021-2\DATOS Y ALGORITMOS\Entrega 3\image_1.jpg'
    #Decompression
    compress_loss(img)
    decompress(archivo1) 
    #decompress(archivo2)
    #Huffman
    huffman_image = huffman_decompress(archivo1)
    print(huffman_image)
    
main()