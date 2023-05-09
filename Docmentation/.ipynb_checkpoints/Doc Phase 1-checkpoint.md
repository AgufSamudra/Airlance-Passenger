# Phase 1 - Improve by Algorithm

Untuk proses seperti import dataset, splitting data, mini feature engineering masih sama seperti pada notebook sebelumnya. Bedanya di sini saya menggunakan Algoritma lain untuk training data tersebut.

Jadi saya sudah mencoba 2 Alogiritma yaitu,
- SVC
- XGBoost

Saya sudah mencoba keduanya, akan tetapi saya mendapat masalah ketika menggunakan SVC. Sehingga di notebook hanya ada XGBoost yang tertera.

## Problem SVC
Sebelumnya saya mengatakan adanya masalah di algoritma SVC yaitu komputasi yang terlalu lama. Saya sudah mengurangi kombinasi pada tuning namun hasilnya tetap sama, komputasi yang dilakukan SVC sangat lama.

### Step Combination
Pada kombinasi pertama saya melakukan dengan RandomizedSearch dengan jumlah kombinasi sebanyak 150 fit, dan hasilnya sangat lama.

Percobaan kedua saya mengurangi kombinasi menjadi 75 fit, dan tidak ada perubahan yang terjadi, komputasi pada SVC tetap sangat lama.

Percobaan ketiga saya kurangi lagi menjadi 24 fit, dan saya sudah menunggu selama kurang lebih 20 menitan dan hasilnya tetap sama. Komputasi yang di lakukan sangat terasa berat.

Pada Akhirnya saya memutuskan untuk meninggalkan Algoritma tersebut dan langsung mencoba algoritma yang kedua yaitu `XGBoost`

## XGBoost
Pada percobaan XGboost saya benar-benar menghemat waktu komputasi menjadi lebih cepat sama seperti Random Forest, ada beberapa parameter tuning yang saya gunakan diantaranya,

```python
parameters_xgb = {
    "learning_rate": [0.1, 0.01, 0.001],
    "max_depth": [3, 5, 7],
    "gamma": [0, 0.1, 0.2],
    "colsample_bytree": [0.5, 0.8, 1],
    "reg_alpha": [0.001, 0.01, 0.1],
    "reg_lambda": [0.001, 0.01, 0.1]
}
```

Setelah tuning selesai didapati best parameter dan hasil akurasi yang sedikit lebih baik di banding Random Forest, berikut adalah beberapa best parameternya,

```python
Best hyperparameters:  {
    'reg_lambda': 0.1, 
    'reg_alpha': 0.001, 
    'max_depth': 7, 
    'learning_rate': 0.1, 
    'gamma': 0.1, 
    'colsample_bytree': 0.8
}
```

Dan Akurasi di: `0.9621117200266296`

## Evaluasi

```txt
      precision    recall  f1-score   support

           0       0.96      0.98      0.97     14528
           1       0.97      0.94      0.96     11365

    accuracy                           0.96     25893
   macro avg       0.96      0.96      0.96     25893
weighted avg       0.96      0.96      0.96     25893
```