import cv2#Memanggil modul/library cv2
import numpy as np#Memanggil modul/library numpy
import matplotlib.pyplot as plt#Memanggil modul/library matplotlib
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray

image = cv2.imread('gedungsate.jpg', 0)#sebuah fungsi yang membaca file gambar dan mengembalikan sebuah array NumPy yang merepresentasikan gambar tersebut.
image_equalized = cv2.equalizeHist(image)#melakukan equalisasi histogram pada gambar yang disimpan dalam variabel image.
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8,8))#menggunakan library OpenCV (cv2) untuk membuat objek CLAHE (Contrast Limited Adaptive Histogram Equalization).
#Apply CLAHE to the original image
image_clahe = clahe.apply(image)#menerapkan metode CLAHE (Contrast Limited Adaptive Histogram Equalization) yang telah dibuat sebelumnya (clahe) pada gambar yang disimpan dalam variabel image.
# Create an empty array to store the final output
image_cs = np.zeros((image.shape[0],image.shape[1]),dtype = 'uint8')#membuat sebuah matriks nol dengan dimensi yang sama dengan gambar yang disimpan dalam variabel image.

# Apply Min-Max Contrasting
min = np.min(image)#menggunakan library NumPy (np) untuk mencari nilai terkecil (minimum) dalam gambar yang disimpan dalam variabel image.
max = np.max(image)#menggunakan library NumPy (np) untuk mencari nilai terbesar (maksimum) dalam gambar yang disimpan dalam variabel image.

for i in range(image.shape[0]):#melakukan iterasi (perulangan) sebanyak jumlah baris dalam gambar yang disimpan dalam variabel image.
    for j in range(image.shape[1]):#untuk melakukan iterasi (perulangan) sebanyak jumlah kolom dalam gambar yang disimpan dalam variabel image.
        image_cs[i,j] = 255*(image[i,j]-min)/(max-min)# untuk menghitung dan menetapkan nilai pada matriks image_cs pada posisi baris i dan kolom j dengan mengaplikasikan transformasi kontras ke gambar.
copyCamera = image.copy().astype(float)# untuk membuat salinan dari gambar yang disimpan dalam variabel image dengan tipe data float.

m1,n1 = copyCamera.shape#untuk mendapatkan dimensi (jumlah baris dan kolom) dari gambar yang disimpan dalam variabel copyCamera.
output1 = np.empty([m1, n1])#membuat array numpy (np) dengan ukuran m1 baris dan n1 kolom yang kosong.

for baris in range(0, m1-1):#perulangan for yang akan iterasi melalui rentang nilai dari 0 hingga m1-1. Dalam konteks ini, variabel baris akan berturut-turut mengambil nilai-nilai dari rentang tersebut dalam setiap iterasi perulangan.
    for kolom in range(0, n1-1):#perulangan for yang akan iterasi melalui rentang nilai dari 0 hingga n1-1. Dalam konteks ini, variabel kolom akan berturut-turut mengambil nilai-nilai dari rentang tersebut dalam setiap iterasi perulangan
        a1 = baris#nilai dari variabel a1 akan diisi dengan nilai dari variabel baris
        b1 = kolom#nilai dari variabel b1 akan diisi dengan nilai dari variabel kolom
        output1[a1, b1] = copyCamera[baris, kolom] * 1.9#mengassign nilai ke elemen pada posisi (a1, b1) dalam array output1. Nilai tersebut dihitung dengan mengalikan nilai pada posisi (baris, kolom) dalam array copyCamera dengan angka 1.9.
fig, axes = plt.subplots(5, 2, figsize=(20, 20))#membuat suatu gambar (figure) dengan 5 baris dan 2 kolom dari subplot.
ax = axes.ravel()#mengubah array multidimensi axes menjadi array satu dimensi ax menggunakan metode ravel()

ax[0].imshow(image, cmap=plt.cm.gray)#menampilkan gambar (image) pada subplot pertama (ax[0]) menggunakan fungsi imshow() dari library Matplotlib. Gambar akan ditampilkan dengan skala abu-abu (grayscale) menggunakan colormap (cmap) plt.cm.gray.
ax[0].set_title("Citra Input")#memberikan judul ("Citra Input") pada subplot pertama (ax[0]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[1].hist(image.ravel(), bins=256)#untuk membuat histogram pada subplot ketujuh (ax[1]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[1].set_title('Histogram Input')#memberikan judul ("Citra Input") pada subplot pertama (ax[1]) dalam gambar (figure) yang telah dibuat sebelumnya.

ax[2].imshow(image_equalized, cmap=plt.cm.gray)#menampilkan gambar (image) pada subplot pertama (ax[2]) menggunakan fungsi imshow() dari library Matplotlib. Gambar akan ditampilkan dengan skala abu-abu (grayscale) menggunakan colormap (cmap) plt.cm.gray.
ax[2].set_title("Citra Output HE")#memberikan judul ("Citra Input") pada subplot pertama (ax[2]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[3].hist(image_equalized.ravel(), bins=256)#untuk membuat histogram pada subplot ketujuh (ax[3]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[3].set_title('Histogram Output HE Method')#memberikan judul ("Citra Input") pada subplot pertama (ax[3]) dalam gambar (figure) yang telah dibuat sebelumnya.

ax[4].imshow(image_cs, cmap=plt.cm.gray)#menampilkan gambar (image) pada subplot pertama (ax[4]) menggunakan fungsi imshow() dari library Matplotlib. Gambar akan ditampilkan dengan skala abu-abu (grayscale) menggunakan colormap (cmap) plt.cm.gray.
ax[4].set_title("Citra Output CS")#memberikan judul ("Citra Input") pada subplot pertama (ax[4]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[5].hist(image_cs.ravel(), bins=256)#untuk membuat histogram pada subplot ketujuh (ax[5]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[5].set_title('Histogram Output CS Method')#memberikan judul ("Citra Input") pada subplot pertama (ax[5]) dalam gambar (figure) yang telah dibuat sebelumnya.

ax[6].imshow(image_clahe, cmap=plt.cm.gray)#menampilkan gambar (image) pada subplot pertama (ax[6]) menggunakan fungsi imshow() dari library Matplotlib. Gambar akan ditampilkan dengan skala abu-abu (grayscale) menggunakan colormap (cmap) plt.cm.gray.
ax[6].set_title("Citra Grayscale CLAHE")#memberikan judul ("Citra Input") pada subplot pertama (ax[6]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[7].hist(image_clahe.ravel(), bins=256)#untuk membuat histogram pada subplot ketujuh (ax[7]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[7].set_title('Histogram Output CLAHE Method')#memberikan judul ("Citra Input") pada subplot pertama (ax[7]) dalam gambar (figure) yang telah dibuat sebelumnya.

ax[8].imshow(output1, cmap=plt.cm.gray)#menampilkan gambar (image) pada subplot pertama (ax[8]) menggunakan fungsi imshow() dari library Matplotlib. Gambar akan ditampilkan dengan skala abu-abu (grayscale) menggunakan colormap (cmap) plt.cm.gray.
ax[8].set_title("Citra Grayscale Perkalian Konstanta")#memberikan judul ("Citra Input") pada subplot pertama (ax[8]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[9].hist(output1.ravel(), bins=256)#untuk membuat histogram pada subplot kesepuluh (ax[9]) dalam gambar (figure) yang telah dibuat sebelumnya.
ax[9].set_title('Histogram Output Perkalian Konstanta Method')#memberikan judul ("Citra Input") pada subplot pertama (ax[9]) dalam gambar (figure) yang telah dibuat sebelumnya.
fig.tight_layout()#menyesuaikan parameter subplot untuk memberikan padding yang ditentukan
plt.show()#menampilkan semua gambar