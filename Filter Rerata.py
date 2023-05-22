import cv2#Memanggil modul#library cv2
import numpy as np#Memanggil modul/library numpy
import matplotlib.pyplot as plt#Memanggil modul/library matplotlib
from skimage import data
from skimage.io import imread#mengimpor fungsi imread dari modul io yang ada dalam pustaka Scikit-Image (skimage).
from skimage.color import rgb2gray

citra1 = imread(fname="mobil.tif")#membaca citra dengan nama file "mobil.tif" menggunakan fungsi imread() dari modul io di pustaka Scikit-Image (skimage) dan menyimpannya ke dalam variabel citra1.
citra2 = imread(fname="boneka2.tif")#membaca citra dengan nama file "boneka2.tif" menggunakan fungsi imread() dari modul io di pustaka Scikit-Image (skimage) dan menyimpannya ke dalam variabel citra2.

print('Shape citra 1 : ', citra1.shape)#menampilkan/mencetak bentuk (shape) dari citra yang disimpan dalam variabel citra1.
print('Shape citra 2 : ', citra2.shape)#menampilkan/mencetak bentuk (shape) dari citra yang disimpan dalam variabel citra2.

fig, axes = plt.subplots(1, 2, figsize=(10, 10))#membuat sebuah objek Figure dan dua objek Axes dalam tata letak horizontal (1 baris, 2 kolom), dengan ukuran total gambar sebesar (10, 10).
ax = axes.ravel()#mengubah array multidimensi axes menjadi array satu dimensi ax menggunakan metode ravel()


ax[0].imshow(citra1, cmap = 'gray')#menampilkan gambar (image) pada subplot pertama (ax[0]) menggunakan fungsi imshow() dari library Matplotlib. Gambar akan ditampilkan dengan skala abu-abu (grayscale) menggunakan colormap (cmap) plt.cm.gray.
ax[0].set_title("Citra 1")# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".
ax[1].imshow(citra2, cmap = 'gray')#menampilkan gambar (image) pada subplot pertama (ax[1]) menggunakan fungsi imshow() dari library Matplotlib. Gambar akan ditampilkan dengan skala abu-abu (grayscale) menggunakan colormap (cmap) plt.cm.gray.
ax[1].set_title("Citra 2")# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".

copyCitra1 = citra1.copy().astype(float)#Untuk membuat salinan dari citra citra1 dengan tipe data float.
copyCitra2 = citra2.copy().astype(float)#Untuk membuat salinan dari citra citra1 dengan tipe data float.

m1,n1 = copyCitra1.shape#Untuk mengambil dimensi (shape) citra copyCitra1 dan menetapkan nilai dimensi tersebut ke dalam variabel m1 dan n1.
output1 = np.empty([m1, n1])#untuk membuat sebuah array kosong dengan ukuran [m1, n1] menggunakan fungsi empty() dari library NumPy.

m2,n2 = copyCitra2.shape#Untuk mengambil dimensi (shape) citra copyCitra1 dan menetapkan nilai dimensi tersebut ke dalam variabel m1 dan n1.
output2 = np.empty([m2, n2])#untuk membuat sebuah array kosong dengan ukuran [m2, n2] menggunakan fungsi empty() dari library NumPy.
print('Shape copy citra 1 : ', copyCitra1.shape)#untuk mencetak dimensi (shape) dari citra copyCitra1.
print('Shape output citra 1 : ', output1.shape)#untuk mencetak dimensi (shape) dari citra output1.

print('m1 : ',m1)#untuk mencetak nilai dari variabel m1.
print('n1 : ',n1)#untuk mencetak nilai dari variabel n1.
print()#menampilkan hasil dari citra

print('Shape copy citra 2 : ', copyCitra2.shape)#untuk mencetak dimensi (shape) dari citra copyCitra2.
print('Shape output citra 3 : ', output2.shape)#untuk mencetak dimensi (shape) dari citra output2.
print('m2 : ',m2)#untuk mencetak nilai dari variabel m2.
print('n2 : ',n2)#untuk mencetak nilai dari variabel n1.
print()#menampilkan hasil dari citra



for baris in range(0, m1-1):#untuk melakukan iterasi atau perulangan sebanyak m1-1 kali, dengan variabel baris yang akan mengambil nilai dari rentang (range) 0 hingga m1-1.
    for kolom in range(0, n1-1):#untuk melakukan iterasi atau perulangan sebanyak n1-1 kali, dengan variabel baris yang akan mengambil nilai dari rentang (range) 0 hingga n1-1.
        a1 = baris# variabel atau elemen yang disebut "a1" mengacu pada nilai atau data yang ada di dalam kolom pertama
        b1 = kolom# variabel atau elemen yang disebut "b1" mengacu pada nilai atau data yang ada di dalam kolom pertama
        jumlah = copyCitra1[a1-1, b1-1] + copyCitra1[a1-1, b1] + copyCitra1[a1-1, b1-1] + \
                 copyCitra1[a1, b1-1] + copyCitra1[a1, b1] + copyCitra1[a1, b1+1] + \
                 copyCitra1[a1+1, b1-1] + copyCitra1[a1+1, b1] + copyCitra1[a1+1, b1+1];
        output1[a1, b1] = (1/9 * jumlah)

for baris1 in range(0, m2-1):
    for kolom1 in range(0, n2-1):
        a1 = baris1 #variabel atau elemen yang disebut "a1" mengacu pada nilai atau data yang ada di dalam kolom pertama
        b1 = kolom1# variabel atau elemen yang disebut "b1" mengacu pada nilai atau data yang ada di dalam kolom pertama
        jumlah = copyCitra2[a1-1, b1-1] + copyCitra2[a1-1, b1] + copyCitra2[a1-1, b1-1] + \
                 copyCitra2[a1, b1 - 1] + copyCitra2[a1, b1] + copyCitra2[a1, b1 + 1] + \
                 copyCitra2[a1+1, b1-1] + copyCitra2[a1+1, b1] + copyCitra2[a1+1, b1+1];
        output2[a1, b1] = (1/9 * jumlah)

#variabel atau elemen yang disebut "a1" mengacu pada nilai atau data yang ada di dalam kolom pertama
# variabel atau elemen yang disebut "b1" mengacu pada nilai atau data yang ada di dalam kolom pertama
#menjumlahkan nilai piksel pada tiga koordinat yang berbeda dalam citra copyCitra1
#menjumlahkan nilai piksel pada tiga koordinat yang berbeda dalam citra copyCitra2
#menjumlahkan nilai piksel pada tiga koordinat yang berbeda dalam citra copyCitra2
#mengisi nilai piksel pada koordinat (a1, b1) dalam citra output2 dengan hasil perhitungan (1/9 * jumlah).

fig, axes = plt.subplots(2, 2, figsize=(10, 10))#membuat sebuah objek Figure dan dua objek Axes dalam tata letak horizontal (1 baris, 2 kolom), dengan ukuran total gambar sebesar (10, 10).
ax = axes.ravel()#mengubah array multidimensi axes menjadi array satu dimensi ax menggunakan metode ravel()

ax[0].imshow(citra1, cmap = 'gray')#menampilkan citra citra1 pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap='gray').
ax[0].set_title("Input Citra 1")# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".

ax[1].imshow(citra2, cmap = 'gray')#menampilkan citra citra2 pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap='gray').
ax[1].set_title("Input Citra 1")# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".

ax[2].imshow(output1, cmap = 'gray')#menampilkan citra outpu1 pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap='gray').
ax[2].set_title("Output Citra 1")# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".

ax[3].imshow(output2, cmap = 'gray')#menampilkan citra output2 pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap='gray').
ax[3].set_title("Output Citra 2")# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".

fig.tight_layout()#menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show()#menampilkan semua gambar