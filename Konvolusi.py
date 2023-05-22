import cv2#Memanggil modul/library cv2
import numpy as np#Memanggil modul/library numpy
import matplotlib.pyplot as plt#Memanggil modul/library matplotlib
from skimage import data
from skimage.io import imread#Memanggil modul/library skimage imread
from skimage.color import rgb2gray

citra1 = imread(fname="boneka2.tif")##membaca citra dengan nama file "boneka2.tif" menggunakan fungsi imread() dari modul io di pustaka Scikit-Image (skimage) dan menyimpannya ke dalam variabel citra2.
print(citra1.shape)#Menampilkan gambar/bentuk citra1

plt.imshow(citra1, cmap='gray')#untuk menampilkan citra (citra1) sebagai plot menggunakan fungsi imshow() dari library Matplotlib.

kernel = np.array([[-1, 0, -1],# membuat array numpy (np.array) dengan elemen-elemen yang terdiri dari -1, 0, dan -1.
                   [0, 4, 0],# membuat array numpy (np.array) dengan elemen-elemen yang terdiri dari -1, 0, dan -1.
                   [-1, 0, -1]])# membuat array numpy (np.array) dengan elemen-elemen yang terdiri dari -1, 0, dan -1.

citraOutput = cv2.filter2D(citra1, -1, kernel)# untuk melakukan operasi konvolusi pada citra (citra1) menggunakan kernel (kernel) dengan menggunakan fungsi filter2D() dari library OpenCV (cv2).

fig, axes = plt.subplots(1, 2, figsize=(12, 12))#untuk membuat sebuah gambar (figure) dengan satu baris dan dua kolom subplot. Gambar tersebut akan ditampilkan dengan ukuran (figsize) sebesar 12 x 12 inci.
ax = axes.ravel()##mengubah array multidimensi axes menjadi array satu dimensi ax menggunakan metode ravel()

ax[0].imshow(citra1, cmap = 'gray')#menampilkan citra (citra1) pada subplot pertama (ax[0]) menggunakan fungsi imshow() dari library Matplotlib. Citra akan ditampilkan dalam skala abu-abu (grayscale) menggunakan colormap (cmap) 'gray'.
ax[0].set_title("Citra Input")##memberikan judul ("Citra Input") pada subplot pertama (ax[0]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[1].imshow(citraOutput, cmap = 'gray')#menampilkan citra (citra1) pada subplot pertama (ax[1]) menggunakan fungsi imshow() dari library Matplotlib. Citra akan ditampilkan dalam skala abu-abu (grayscale) menggunakan colormap (cmap) 'gray'.
ax[1].set_title("Citra Output")##memberikan judul ("Citra Input") pada subplot pertama (ax[1]) dalam gambar (figure) yang telah dibuat sebelumnya.

fig.tight_layout()#menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show()#menampilkan semua gambar


