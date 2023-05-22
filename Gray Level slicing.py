import cv2#Memanggil modul/library cv2
import numpy as np#Memanggil modul/library numpy
import matplotlib.pyplot as plt#Memanggil modul/library matplotlib

img = image = cv2.imread('gedungsate.jpg', 0)#sebuah fungsi yang membaca file gambar dan mengembalikan sebuah array NumPy yang merepresentasikan gambar tersebut.

row, column = img.shape# Menetapkan nilai baris dan kolom dari atribut bentuk

img1 = np.zeros((row, column), dtype='uint8')#membuat sebuah array numpy dengan bentuk (shape) yang sama dengan gambar img, yang berisi semua nilai nol dengan unsigned integer dengan panjang 8 bit

min_range = 10#nilai minimum
max_range = 60#nilai maksimum

for i in range(row):#perulangan for untuk mengulangi sebuah blok kode sebanyak row kali.
    for j in range(column):#perulangan for untuk mengulangi sebuah blok kode sebanyak column kali.
        if img[i, j] > min_range and img[i, j] < max_range:#melakukan pengecekan kondisi pada nilai piksel citra. Jika nilai piksel pada koordinat
            img1[i, j] = 255# mengatur nilai piksel citra img1 pada koordinat (i, j) menjadi 255.
        else:## Kode yang akan dijalankan jika kondisi tidak terpenuhi
            img1[i, j] = 0#mengatur nilai piksel citra img1 pada koordinat (i, j) menjadi 0.

fig, axes = plt.subplots(2, 2, figsize=(12, 12))# menghasilkan sebuah objek Figure dan objek-objek Axes yang digunakan untuk membuat subplot dengan tata letak 2x2.
ax = axes.ravel()#mengubah array multidimensi axes menjadi array satu dimensi ax menggunakan metode ravel()

ax[0].imshow(img, cmap=plt.cm.gray)# menampilkan citra img pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap=plt.cm.gray).
ax[0].set_title("Citra Input")# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".
ax[1].hist(img.ravel(), bins=256)#membuat histogram dari piksel-piksel dalam citra img dan menampilkannya pada subplot kedua (indeks 1).
ax[1].set_title('Histogram Input')# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".

ax[2].imshow(img1, cmap=plt.cm.gray)## menampilkan citra img pada subplot pertama (indeks 0) dengan menggunakan skema warna abu-abu (cmap=plt.cm.gray).
ax[2].set_title("Citra Output")# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".
ax[3].hist(img1.ravel(), bins=256)#membuat histogram dari piksel-piksel dalam citra img dan menampilkannya pada subplot kedua (indeks 1).
ax[3].set_title('Histogram Output')# mengatur judul pada subplot pertama (indeks 0) menjadi "Citra Input".

plt.tight_layout()#menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show()#menampilkan semua gambar

