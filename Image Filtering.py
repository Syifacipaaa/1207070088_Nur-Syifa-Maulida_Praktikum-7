# memanggil modul yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt

#bgr
img = cv2.imread('gedungsate.jpg')#untuk membaca dan memuat citra dengan nama file 'gedungsate.jpg' menggunakan library OpenCV (cv2).

#rgb
cat = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#mengubah mode warna citra dari BGR (Blue-Green-Red) ke RGB (Red-Green-Blue) menggunakan fungsi cv2.cvtColor() dari library OpenCV (cv2).


# tampilkan gambar awal tanpa filter
cv2.imshow('foto asli', img)#menampilkan citra dengan menggunakan jendela tampilan (window) dengan judul 'foto asli' menggunakan fungsi cv2.imshow() dari library OpenCV (cv2).
cv2.waitKey(0)# untuk menunggu tombol keyboard ditekan untuk menutup jendela tampilan.
cv2.destroyAllWindows()#perintah untuk menutup semua jendela tampilan yang dibuat menggunakan fungsi cv2.imshow() dari library OpenCV (cv2).

# membuat filter: matriks berukuran 5 x 5
kernel = np.ones((5,5),np.float32)/25#untuk membuat matriks berukuran 5x5 dengan semua elemen bernilai 1.
print(kernel)#menampilkan matriks kernel tersebut.

# lakukan filtering
Anjing_filter = cv2.filter2D(img,-1,kernel)#untuk menerapkan operasi pemulusan citra pada citra yang disimpan dalam variabel 'img' menggunakan kernel yang telah didefinisikan sebelumnya dengan variabel 'kernel'.

cv2.imshow('Kucing Filter', Anjing_filter)#menampilkan citra dengan menggunakan jendela tampilan (window) dengan judul 'foto asli' menggunakan fungsi cv2.imshow() dari library OpenCV (cv2).
cv2.waitKey(0)# untuk menunggu tombol keyboard ditekan untuk menutup jendela tampilan.
cv2.destroyAllWindows()#perintah untuk menutup semua jendela tampilan yang dibuat menggunakan fungsi cv2.imshow() dari library OpenCV (cv2).
# salt and pepper

# perbesar ukuran hasil plotting jika diperlukan
plt.rcParams["figure.figsize"] = (15,15)#untuk mengatur ukuran default dari gambar yang akan ditampilkan menggunakan library Matplotlib (plt).

# plot pertama, gambar asli
plt.subplot(121),plt.imshow(cat),plt.title('Original')#untuk mengatur subplot, menampilkan citra 'cat', dan memberikan judul "Original" pada subplot tersebut menggunakan library Matplotlib (plt).
plt.xticks([]), plt.yticks([])# untuk menghilangkan tanda sumbu (ticks) pada sumbu x (horizontal) dan sumbu y (vertikal) pada gambar yang ditampilkan menggunakan library Matplotlib (plt).

# kedua, hasil filter
plt.subplot(122),plt.imshow(Anjing_filter)#untuk mengatur subplot, menampilkan citra 'cat', dan memberikan judul "Original" pada subplot tersebut menggunakan library Matplotlib (plt).
plt.title('Averaging')#untuk memberikan judul "Averaging" pada subplot yang aktif menggunakan library Matplotlib (plt).
plt.xticks([]), plt.yticks([])# untuk menghilangkan tanda sumbu (ticks) pada sumbu x (horizontal) dan sumbu y (vertikal) pada gambar yang ditampilkan menggunakan library Matplotlib (plt).

# Plot!
plt.show()#untuk menampilkan gambar atau plot yang telah dibuat menggunakan library Matplotlib (plt).

Anjing_blur = cv2.blur(img,(5,5))

cv2.imshow('Anjing Blur', Anjing_blur)
cv2.waitKey(0)# untuk menunggu tombol keyboard ditekan untuk menutup jendela tampilan.
cv2.destroyAllWindows()#perintah untuk menutup semua jendela tampilan yang dibuat menggunakan fungsi cv2.imshow() dari library OpenCV (cv2).

# ini adalah cara lain untuk membuat sebuah kernel,
# yaitu dengan menggunakan np.matrix
# kali ini, ukuran matriksnya 3 x 3
kernel = np.matrix([#untuk mendefinisikan kernel dalam bentuk matriks menggunakan library NumPy (np).
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]
          ])/25
print(kernel)#mencetak isi dari variabel 'kernel' ke dalam output.

# buat lagi filteringnya
Anjing_filter = cv2.filter2D(img,-1,kernel)# untuk menerapkan operasi konvolusi pada citra yang disimpan dalam variabel 'img' menggunakan kernel yang telah didefinisikan sebelumnya dengan variabel 'kernel'.

# tampilkan
cv2.imshow('Anjing Filter', Anjing_filter)#menampilkan citra dengan menggunakan jendela tampilan (window) dengan judul 'foto asli' menggunakan fungsi cv2.imshow() dari library OpenCV (cv2).
cv2.waitKey(0)# untuk menunggu tombol keyboard ditekan untuk menutup jendela tampilan.
cv2.destroyAllWindows()#perintah untuk menutup semua jendela tampilan yang dibuat menggunakan fungsi cv2.imshow() dari library OpenCV (cv2).

#High-Pass Filtering
# Highpass Filter

# sebenarnya kita tidak perlu melakukan filtering lagi. Cukup sekali saja
# di bagian awal, selama notebook ini tetap terhubung
import cv2#memanggil modul/library cv2
import numpy as np#memanggil modul library numpy
from matplotlib import pyplot as plt#memanggil modul/library matplotlib


# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('ml.jpg',0)#membaca dan memuat citra dengan nama file 'ml.jpg' dalam mode grayscale (grayscale image) menggunakan library OpenCV (cv2).

# menerapkan algoritma high-pass filtering:
# laplacian
laplacian = cv2.Laplacian(img,cv2.CV_64F)#untuk mengaplikasikan operator Laplacian pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).

# sobel dengan ukuran kernel 5
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)#untuk mengaplikasikan operator Sobel pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)#untuk mengaplikasikan operator Sobel pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).

# Catatan:
# CV_64F pada contoh di atas menunjukkan nilai bit dari citra
# yang dihasilkan serta tipe datanya (F = Float)

# perbesar ukuran hasil plotting
plt.rcParams["figure.figsize"] = (10,10)#untuk mengatur ukuran default dari gambar yang akan ditampilkan menggunakan library Matplotlib (plt)


# menampilkan hasil filter
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')#untuk mengatur subplot dan menampilkan citra 'img' dengan peta warna (colormap) 'gray' menggunakan library Matplotlib (plt).
plt.title('Original'), plt.xticks([]), plt.yticks([])#untuk memberikan judul pada subplot, menghilangkan tanda sumbu pada sumbu x dan sumbu y pada gambar yang ditampilkan menggunakan library Matplotlib (plt).
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')#untuk mengatur subplot dan menampilkan citra 'img' dengan peta warna (colormap) 'gray' menggunakan library Matplotlib (plt).
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])#untuk memberikan judul pada subplot, menghilangkan tanda sumbu pada sumbu x dan sumbu y pada gambar yang ditampilkan menggunakan library Matplotlib (plt).
plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')#untuk mengatur subplot dan menampilkan citra 'img' dengan peta warna (colormap) 'gray' menggunakan library Matplotlib (plt).
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])#untuk memberikan judul pada subplot, menghilangkan tanda sumbu pada sumbu x dan sumbu y pada gambar yang ditampilkan menggunakan library Matplotlib (plt).
plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')#untuk mengatur subplot dan menampilkan citra 'img' dengan peta warna (colormap) 'gray' menggunakan library Matplotlib (plt).
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])#untuk memberikan judul pada subplot, menghilangkan tanda sumbu pada sumbu x dan sumbu y pada gambar yang ditampilkan menggunakan library Matplotlib (plt).
plt.show()#untuk menampilkan gambar atau plot yang telah dibuat menggunakan library Matplotlib (plt).


# memanggil citra sebagai grayscale (argument 0)
img = cv2.imread('pubg.jpeg',0)#membaca dan memuat citra dengan nama file 'ml.jpg' dalam mode grayscale (grayscale image) menggunakan library OpenCV (cv2).

# memanggil fungsi Canny Edges dengan argument (citra, nilai_min, nilai_max)
edges = cv2.Canny(img,100,200)#untuk mengaplikasikan operator Canny pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).

plt.subplot(121),plt.imshow(img,cmap = 'gray')#untuk mengatur subplot dan menampilkan citra 'img' dengan peta warna (colormap) 'gray' menggunakan library Matplotlib (plt).
plt.title('Original Image'), plt.xticks([]), plt.yticks([])#untuk memberikan judul pada subplot, menghilangkan tanda sumbu pada sumbu x dan sumbu y pada gambar yang ditampilkan menggunakan library Matplotlib (plt).
plt.subplot(122),plt.imshow(edges,cmap = 'gray')#untuk mengatur subplot dan menampilkan citra 'img' dengan peta warna (colormap) 'gray' menggunakan library Matplotlib (plt).
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])#untuk memberikan judul pada subplot, menghilangkan tanda sumbu pada sumbu x dan sumbu y pada gambar yang ditampilkan menggunakan library Matplotlib (plt).
plt.show()#untuk menampilkan gambar atau plot yang telah dibuat menggunakan library Matplotlib (plt).


#Image Thresholding
# membaca gambar baymax
img = cv2.imread('pubg.jpeg',0)#membaca dan memuat citra dengan nama file 'ml.jpg' dalam mode grayscale (grayscale image) menggunakan library OpenCV (cv2).

# Hitungan threshold.
# Perhatikan nilai ambang batas bawah dan atas dari tiap fungsi
# yang diberikan
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)#untuk melakukan thresholding pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)#untuk melakukan thresholding pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)#untuk melakukan thresholding pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)#untuk melakukan thresholding pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)#untuk melakukan thresholding pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).

# menampilkan hasil
titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']#berisi daftar judul (title) yang akan digunakan untuk menggambarkan beberapa citra dalam satu tampilan menggunakan library Matplotlib.
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]# berisi daftar citra yang akan digunakan untuk ditampilkan dalam satu tampilan menggunakan library Matplotlib.

# menampilkan beberapa gambar sekaligus
for i in range(6):#menginisiasi perulangan dengan menggunakan variabel iterasi 'i' yang akan mengambil nilai dari 0 hingga 5 (6 nilai).
    # 3 baris, 2 kolom
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')#mengatur subplot dan menampilkan citra dalam satu tampilan menggunakan library Matplotlib.
    plt.title(titles[i])#untuk mengatur judul (title) pada subplot yang sedang diakses dalam iterasi.
    plt.xticks([]),plt.yticks([])#untuk menghilangkan tanda sumbu (ticks) pada sumbu x dan sumbu y pada tampilan plot.
plt.show()#untuk menampilkan gambar atau plot yang telah dibuat menggunakan library Matplotlib (plt).

# masih menggunakan variabel img yang sama
#img = cv2.imread('images/baymax.jpg',0)

# digunakan median blur untuk menghaluskan tepi objek pada citra
# ini diperlukan agar thresholding memberikan hasil lebih baik
img = cv2.medianBlur(img,5)#untuk menerapkan filter median pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).

# Lakukan Thresholding
# Binary Threshold
ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)# untuk melakukan thresholding pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2) dengan mode 'THRESH_BINARY'.

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
#untuk melakukan threshold adaptif pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2).
#mengatur parameter-parameter untuk metode threshold adaptif.

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)#mengatur parameter-parameter untuk metode threshold adaptif.
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\:melakukan threshold adaptif pada citra yang disimpan dalam variabel 'img' menggunakan library OpenCV (cv2)
#cv2.THRESH_BINARY,11,2):mengatur parameter-parameter untuk metode threshold adaptif.

# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)',# untuk menampilkan subplot dalam tampilan plot.
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']

images = [img, th1, th2, th3]#inisialisasi daftar gambar yang akan ditampilkan dalam subplot dalam tampilan plot.

# menampilkan hasil
for i in range(4):#untuk melakukan iterasi sebanyak 4 kali. Dalam setiap iterasi, variabel i akan berisi nilai dari 0 hingga 3.
    plt.subplot(2,2,i+1)#untuk mengatur tata letak subplot dalam tampilan plot.
    plt.imshow(images[i],'gray')#untuk menampilkan gambar dalam subplot menggunakan fungsi imshow() dari library matplotlib.
    plt.title(titles[i])#untuk mengatur judul subplot dalam tampilan plot.
    plt.xticks([]),plt.yticks([])#untuk menghilangkan tanda sumbu (ticks) pada sumbu x dan sumbu y dalam subplot.
plt.show()#untuk menampilkan gambar atau plot yang telah dibuat menggunakan library Matplotlib (plt).