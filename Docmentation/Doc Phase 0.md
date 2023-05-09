# Phase 0 - Simple Model

Phase 0 di sini saya hanya membuat simple model atau model yang digunakan untuk benchmark, dan melakukan beberapa pembersihan data karena ditemui adanya data yang bolong dan categorical feature.

## Splitting Data
Pada tahap splitting saya menggunakan teknik yang manual karena data train dan test sudah terpisah sebelumnya, jadi saya meisahkan datanya menjadi 4 yaitu: `X_train` `X_test` `y_train` `y_test`

```Python

X_train = df_train.drop(columns="satisfaction")
y_train = df_train.satisfaction

X_test = df_test.drop(columns="satisfaction")
y_test = df_test.satisfaction
```

## Mini Feature Engineering
Pada dataset `label` berupa categorical object, oleh karenanya saya mengubah terlebih dahulu menjadi categorical numeric. Dan juga melakukan One Hot Encoding pada data X menggunakan `pd.get_dummies()`

```python

y_train = y_train.replace({'neutral or dissatisfied': 0, 'satisfied': 1})
y_test = y_test.replace({'neutral or dissatisfied': 0, 'satisfied': 1})

X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)
```

## Training
Pada Simple Model saya menggunakan algoritma Random Forest yang sudah di tuning dengan RandomizedSearchCV, alasannya karena data kita lumayan besar. Saya memilih Randomized untuk efesiensi Simple Model dan menghindari dari komputasi yang terlalu lama.

Saya juga menaruh beberapa parameter untuk tuning modelnya, berikut adalah parameter yang saya gunakan,

```python

parameters = {
    "n_estimators": range(100, 250, 5),
    "max_depth": range(1, 40, 2),
    "min_samples_split": range(2, 10, 2),
    "min_samples_leaf": range(1, 10),
    "max_features": ['auto', 'sqrt']
}
```

Dan di dapat hasilnya sebagi berikut:<br>
```python
Best hyperparameters:  {
    'n_estimators': 200,  
    'min_samples_split': 4, 
    'min_samples_leaf': 1, 
    'max_features': 'auto', 
    'max_depth': 39 
}
```

Dengan Score Awal sebesar: `0.9620827541114724`

## Evaluasi
```txt

              precision    recall  f1-score   support

           0       0.96      0.98      0.97     14528
           1       0.97      0.94      0.96     11365

    accuracy                           0.96     25893
    macro avg       0.96      0.96     0.96     25893
    weighted avg    0.96      0.96     0.96     25893
```
