"""
Dilihat dari formulanya, jarak antar kuartil didefinisikan sebagai selisih antara kuartil 3 (Q3) dan kuartil 1 (Q1), 
secara definisi jarak antar kuartil dapat diartikan sebagai ukuran 50% data yang terpusat di tengah data yang terurut.
Secara sederhana nilai jarak antar kuartil menggambarkan seberapa menyebar data, semakin 
besar nilai jarak antar kuartil maka semakin menyebar data, sebaliknya semakin kecil nilai jarak antar kuartil menandakan dataset lebih terpusat ke tengah.
"""

"""
Nilai jarak antar kuartil sangat baik digunakan untuk data -data yang memiliki banyak pencilan (outlier).
Pencilan merupakan data tersebar sangat jauh dari pusat sehingga tidak lagi merepresentasikan data yang ada. Umumnya pencilan dihilangkan dengan mengambil:

Batas bawah = Q1 - 1.5x jarak antar kuartil

Batas atas = Q3 + 1.5 x jarak antar kuartil
"""
import pandas as pd
import matplotlib.pylab as plt
import numpy as np
#definisi data
corona_indonesia=pd.ExcelFile("D:\TeguhPermana_data\Penyebaran_data\kawalcovid-data.xlsx")
corona_indonesia=corona_indonesia.parse("total_positive_cases")
#filter data
corona_indonesia=corona_indonesia[corona_indonesia["Total Kasus"]=="3/18/2020"]
total_kasus=corona_indonesia.iloc[:,1:-1].values[0]
ranged=range(0,len(total_kasus))

# ploat penyebaran data
figure,ax=plt.subplots()
ax.scatter(ranged,total_kasus)
ax.set_ylabel("Kasus Covid")
ax.set_title("Kasus corona chicken naget mantap")
plt.show()

#pada data tersebut terdapat sebuah pencilan sehingga data menjadi tidak normal cara untuk membuat data tersebut normal adalah dengan cara dengan jarak antar kuartil


#menghitung jarak antar kuartil
Q1=np.percentile(total_kasus,25)
Q2=np.percentile(total_kasus,75)
iqr=Q2-Q1

print(total_kasus)
#Menyaring  data dari pencilan
new_total_kasus_index=np.where((total_kasus>=Q1-1.5*iqr)&(total_kasus<=Q2+1.5*iqr))
#1   merupakan kode untuk menyaring data dengan nilai yang memiliki batas bawah Q1 – 1.5*IQR dan Q3 + 1.5*IQR.
#  Hasilnya berupa indeks array yang memiliki nilai dengan kondisi tersebut.
new_total_kasus=total_kasus[new_total_kasus_index]
print(new_total_kasus)
#2   merupakan kode untuk mengambil data dari array total_case berdasarkan indeks data yang telah disaring.

#plot pesebaran data corona
ranged2=range(0,len(new_total_kasus))
print(ranged2)
figure,ax=plt.subplots()
ax.scatter(ranged2,new_total_kasus)
# ax.set_ylim(0,max(total_kasus))
plt.show()



