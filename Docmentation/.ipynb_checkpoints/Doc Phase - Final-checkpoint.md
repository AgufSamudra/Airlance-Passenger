# Final - Pipeline

Akhirnya sampai di penghujung projek tahap Machine Learning Modeling, setelah melewati beberapa phase dan sedikit EDA, di tahap ini saya akan membuat pipeline untuk keseluruhan projek. Menggunakan bawaan Scikit-learn yaitu Pipeline dan ColoumnTransformer.

## Drop Columns

Ada beberapa kolom yang saya hapus karena menurut saya fitur tersebut kurang mempengaruhi dalam prediksi tingkat kepuasan penumpang ketika penerbangan. Kolom-kolom yang saya buang sebagai berikut,

```python
df_train.drop(columns=['Unnamed: 0', 'Gate location', 'Leg room service', 'Baggage handling'], inplace=True)
df_test.drop(columns=['Unnamed: 0', 'Gate location', 'Leg room service', 'Baggage handling'], inplace=True)
```

## Preprocessor

Pada tahap ini saya membuat pipeline untuk preprocessing datanya terlebih dahulu sebelum masuk dalam pipeline modeling, karena ada beberapa data yang harus di Impute, dan convert categorical dan numerical.

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

Setelah pipeline untuk processing selesai di buat, saya langsung membuat ColumnTransformer untuk memilih kolom-kolom apa saja yang di masukan ke setiap pipeline processing, dan menggabungkannya menjadi satu yang di namakan `Preprocessor`

```python
preprocessor = ColumnTransformer([
    ("numeric", numerical_pipeline, ["Age", "Flight Distance", "Departure Delay in Minutes", "Arrival Delay in Minutes"]),
    ("categoric", categorical_pipeline, ['Gender', 'Customer Type', 'Type of Travel', 'Class']),
    ("ordinal", ordinal_pipeline, ['Inflight wifi service',
        'Departure/Arrival time convenient', 'Ease of Online booking', 
        'Food and drink', 'Online boarding', 'Seat comfort',
        'Inflight entertainment', 'On-board service', 'Checkin service', 
        'Inflight service', 'Cleanliness'])
])
```

## Training / Modeling

Di sini saya membuat pipeline kembali untuk training serta menyertakan beberapa parameter XGBoost yang sudah di Tuning, jadi Full code untuk pipeline seperti berikut,

```python
parameters = {
    "learning_rate": 0.17070059179090855,
    "max_depth": 10,
    "gamma": 3.941904591403078,
    "colsample_bytree": 0.7109662235514159,
    "reg_alpha": 0.7194571167899805,
    "reg_lambda": 5.521019924961057
}

pipeline = Pipeline([
    ("prep", preprocessor),
    ("algo", XGBClassifier(**parameters, n_jobs=-1, random_state=42))
])

pipeline.fit(X_train, y_train)

print(f"Training: {pipeline.score(X_train, y_train)*100:.2f}% | Testing: {pipeline.score(X_test, y_test)*100:.2f}%")
```

