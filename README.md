# Airlance Passenger
Membuat sebuah program untuk memprediksi apakah customer/penumpang dalam maskapai penerbangan merasa `puas` atau `tidak puas` Memanfaatkan teknologi Machine Learning untuk membuatnya, adapun beberapa teknologi yang kami gunakan untuk mengembangkan aplikasi website sederhana ini, antara lain,
- Python
- Scikit-learn
- XGBoost
- Flask
- HTML & CSS

## Alur Pipeline
Dalam pembuatannya kami menggunakan custom pipeline untuk mempermudah pengembangan model ML yang kami butuhkan, berikut merupakan Pipeline yang kami gunakan dalam projek

```python
numerical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy='median'))
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy='most_frequent')),
    ("onehot", OneHotEncoder())
])

ordinal_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy='most_frequent')),    
    ("ordinal", OrdinalEncoder(categories=[['0', '1', '2', '3', '4', '5']] * 11))
])
```

Setelah data kami proses di tahap tersebut, baru kami bisa proses untuk tahap training. Algoritma yang kami gunakan adalah `XGBoost` dan mendapatkan akurasi yang cukup bagus, yaitu sama-sama di `96%` di tahap Training da Testing.

## Result

Hasilnya adalah berupa website sederhana yang memanfaatkan ML untuk memprediksi apakah customer/penumpang merasa puas atau tidak selama proses penerbangan dari memesan tiket sampai tujuan akhir.

![web1](https://raw.githubusercontent.com/AgufSamudra/Airlance-Passenger/main/image/web1.jpg)
![web2](https://raw.githubusercontent.com/AgufSamudra/Airlance-Passenger/main/image/web2.jpg)

# Link
Kami juga sediakan link shorcut untuk langsung melihat inti projek ini,

[Exploratory Data Analysis](https://github.com/AgufSamudra/Airlance-Passenger/blob/main/Docmentation/EDA.md)<br>
[Pipeline](https://github.com/AgufSamudra/Airlance-Passenger/blob/main/Phase%205%20-%20Pipeline%20Testing.ipynb)<br>
[Last Experiment](https://github.com/AgufSamudra/Airlance-Passenger/blob/main/Docmentation/Doc%20Phase%203.md)<br>
