# Phase 3 - More Improve

Saya mencoba untuk lebih improve lagi di phase 3 ini, dan di phase ini saya mencoba menyeleksi fitur-fiturnya dengan logika saya sendiri. Contoh bila suatu fitur tidak masuk akal untuk memprediksi label maka saya akan buang, karena sebelumnya saya melakukan seleksi sesuai dengan informasi dari Feature Importance.

Ada beberapa yang menurut saya pribadi bahwa fitur tersebut kurang mempengaruhi label dataset,
- Age
- Gender
- Flight Distance
- Leg room service
- Departure/Arrival time convenient

Fitur-fitur di atas merupakan yang menurut saya pribadi tidak akan berpengaruh terhadap kepuasan penumpang.

## Training

Pada tahap training saya melakukan 4 kali percobaan, dengan tuning value parameter yang berbeda. Berikut merupakan beberapa tuning yang saya gunakan pada 4 kali percobaan.

**Versi 1**
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

**Versi 2**
```python
parameters_xgb2 = {
    "learning_rate": loguniform(0.001, 1),
    "max_depth": [3, 5, 7],
    "gamma": loguniform(0.001, 10),
    "colsample_bytree": loguniform(0.1, 10),
    "reg_alpha": loguniform(0.001, 10),
    "reg_lambda": loguniform(0.001, 10)
}
```

**Versi 3**
```python
parameters_xgbV3 = {
    "learning_rate": loguniform(0.1, 5),
    "max_depth": [5, 7, 8],
    "gamma": loguniform(0.01, 5),
    "colsample_bytree": loguniform(0.1, 5),
    "reg_alpha": loguniform(0.01, 5),
    "reg_lambda": loguniform(0.1, 10)
}
```

**Versi 4**
```python
parameters_xgbV4 = {
    "learning_rate": loguniform(0.1, 4),
    "max_depth": [8, 9, 10],
    "gamma": loguniform(0.3, 5),
    "colsample_bytree": loguniform(0.5, 5),
    "reg_alpha": loguniform(0.1, 5),
    "reg_lambda": loguniform(2, 10)
}
```

Di atas adalah beberapa parameter yang saya gunakan untuk 4 percobaan yang berbeda. Kenyataan pahitnya adalah ke empat versi di atas tidak memberikan improve yang signifikan, bahkan hasil dari keempatnya hampir sama.

- **Versi 1** = Training: `96.46%` | Testing: `96.14%`
- **Versi 2** = Training: `96.72%` | Testing: `96.19%`
- **Versi 3** = Training: `97.05%` | Testing: `96.27%`
- **Versi 4** = Training: `96.67%` | Testing: `96.35%`

Dari keempat versi di atas, saya akan memilih `Versi 4` Karena Hasil Training dan Testing yang konsisten. Hasil yang di berikan tidak terpaut jauh antara training dan testing, walaupun selisihnya sama dengan `versi 1` Namun di sini saya memilih model `versi 4` saja untuk saya `Save` modelnya.

```txt
                precision    recall  f1-score   support

           0       0.96      0.98      0.97     14528
           1       0.97      0.94      0.96     11365

    accuracy                           0.96     25893
   macro avg       0.96      0.96      0.96     25893
weighted avg       0.96      0.96      0.96     25893
```