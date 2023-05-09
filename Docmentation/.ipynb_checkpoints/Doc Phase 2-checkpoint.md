# Phase 2 - Improve by Feature Importance

Di phase 2 ini saya hanya ingin melihat bagaimana jika saya menghapus beberapa fitur yang memiliki kontribusi paling kecil pada tahap phase 1 sebelumnya, dan algoritma yang akan saya pakai terus kedepannya adalah XGBoost.

Pada phase 2 saya menghapus beberapa fitur yaitu sebagai berikut:
- Age
- Gender
- Food and drink
- Departure Delay in Minutes
- Departure/Arrival time convenient
- Flight Distance
- Arrival Delay in Minutes

7 fitur di atas saya drop, dan proses drop dilakukan sebelum melakukan One Hot Encoding. Setelah fitur tersebut di drop, baru saya langsung melakukan One Hot Encoding.

## Training
Saya tetap menggunakan RandomizedSearchCV untuk tuning parameternya, dan parameter yang saya gunakan masih sama pada tuning di phase 1. Dan hasil yang saya dapatkan sedikit lebih buruk dari sebelumnya, akurasi yang saya dapatkan `0.9609436893943526`

## Evaluasi

ketika saya melihat Feature Importance di phase 2 ada sedikit perubahan, walaupun tidak ada yang berubah secara signifikan seperti yang sebelumnya di posisi `5` sekarang menjadi posisi `7` dan bahkan ada beberapa fitur yang naik.

**Dan berikut hasil dari Classification Reportnya sebagai berikut**

```txt

       precision    recall  f1-score   support

           0       0.95      0.98      0.97     14528
           1       0.97      0.94      0.96     11365

    accuracy                           0.96     25893
   macro avg       0.96      0.96      0.96     25893
weighted avg       0.96      0.96      0.96     25893
```