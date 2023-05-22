import cv2#Memanggil modul/library cv2
import numpy as np#Memanggil modul/library numpy
import matplotlib.pyplot as plt#Memanggil modul/library matplotlib
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray

citra1 = imread(fname="mobil.tif")#membaca citra dengan nama file "mobil.tif" menggunakan fungsi imread() dari modul io di pustaka Scikit-Image (skimage) dan menyimpannya ke dalam variabel citra1.
citra2 = imread(fname="boneka2.tif")#membaca citra dengan nama file "mobil.tif" menggunakan fungsi imread() dari modul io di pustaka Scikit-Image (skimage) dan menyimpannya ke dalam variabel citra1.

print('Shape citra 1 : ', citra1.shape)
print('Shape citra 1 : ', citra2.shape)

fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()

ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Citra 1")
ax[1].imshow(citra2, cmap = 'gray')
ax[1].set_title("Citra 2")

copyCitra1 = citra1.copy()
copyCitra2 = citra2.copy()

m1,n1 = copyCitra1.shape
output1 = np.empty([m1, n1])

m2,n2 = copyCitra2.shape
output2 = np.empty([m2, n2])
print('Shape copy citra 1 : ', copyCitra1.shape)
print('Shape output citra 1 : ', output1.shape)

print('m1 : ',m1)
print('n1 : ',n1)
print()

print('Shape copy citra 2 : ', copyCitra2.shape)
print('Shape output citra 3 : ', output2.shape)
print('m2 : ',m2)
print('n2 : ',n2)
print()

for baris in range(0, m1 - 1):
    for kolom in range(0, n1 - 1):
        a1 = baris
        b1 = kolom
        dataA = [copyCitra1[a1 - 1, b1 - 1], copyCitra1[a1 - 1, b1], copyCitra1[a1 - 1, b1 + 1], \
                 copyCitra1[a1, b1 - 1], copyCitra1[a1, b1], copyCitra1[a1, b1 + 1], \
                 copyCitra1[a1 + 1, b1 - 1], copyCitra1[a1 + 1, b1], copyCitra1[a1 + 1, b1 + 1]]

        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j] = tmpA;

        output1[a1, b1] = dataA[5]

for baris in range(0, m2 - 1):
    for kolom in range(0, n2 - 1):
        a1 = baris
        b1 = kolom
        dataA = [copyCitra2[a1 - 1, b1 - 1], copyCitra2[a1 - 1, b1], copyCitra2[a1 - 1, b1 + 1], \
                 copyCitra2[a1, b1 - 1], copyCitra2[a1, b1], copyCitra2[a1, b1 + 1], \
                 copyCitra2[a1 + 1, b1 - 1], copyCitra2[a1 + 1, b1], copyCitra2[a1 + 1, b1 + 1]]

        # Urutkan
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i];
                    dataA[i] = dataA[j];
                    dataA[j] = tmpA;

        output2[a1, b1] = dataA[5]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))#membuat sebuah objek Figure dan dua objek Axes dalam tata letak horizontal (1 baris, 2 kolom), dengan ukuran total gambar sebesar (10, 10).
ax = axes.ravel()#mengubah array multidimensi axes menjadi array satu dimensi ax menggunakan metode ravel()

ax[0].imshow(citra1, cmap = 'gray')#menampilkan citra output2 pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap='gray').
ax[0].set_title("Input Citra 1")# mengatur judul pada subplot pertama (indeks 0)

ax[1].imshow(citra2, cmap = 'gray')#menampilkan citra output2 pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap='gray').
ax[1].set_title("Input Citra 1")# mengatur judul pada subplot pertama (indeks 0)

ax[2].imshow(output1, cmap = 'gray')#menampilkan citra output2 pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap='gray').
ax[2].set_title("Output Citra 1")# mengatur judul pada subplot pertama (indeks 0)

ax[3].imshow(output2, cmap = 'gray')#menampilkan citra output2 pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap='gray').
ax[3].set_title("Output Citra 2")# mengatur judul pada subplot pertama (indeks 0)

plt.tight_layout()#menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show()#menampilkan semua gambar