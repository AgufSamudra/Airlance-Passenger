# Phase 4 - EDA

pada phase ke 4 ini saya mencoba melakukan sedikit EDA untuk melihat informasi dari data lebih jauh. Dengan harapan melakukan EDA saya melakukan improve pada model saya sebelumnya, walaupun tidak ada jaminan model akan improve.

## Count Label
Label kita adalah,
- neutral or dissatisfied  = `0`
- satisfied = `1`

Saya ingin melihat banyak data dari label yang saya miliki, dengan bantuan seaborn saya dengan mudah menemukan jumlah dari label yang saya miliki.

0  =  73225 </br>
1  =  56262

![countLabel](https://raw.githubusercontent.com/AgufSamudra/Airlance-Passenger/main/image/EDA/count_label.png)

Di dapati bahwa label `0` memiliki jumlah yang lebih banyak ketimbang label `1`, tapi menurut saya data tersebut masih belum termasuk data `imbalance` karena label tersebut tidak terlalu jomplang sekali dan semestinya mesin masih bisa mencari pola dari data tersebut.

## Age for Label

Di sini saya ingin melihat rentang umur berapa sampai berapa yang memiliki tingkat puas atau tidak puas paling tinggi dan rendah pada data kita. Atau kita bisa sebut Age vs Label.

![ageVSlabel](image/EDA/age_with_label.png)

Jika kita melihat dari grafik di atas bahwa kebanyakan orang yang berumur di bawah 30 tahun cenderung tidak puas terhadap maskapai penerbangan. Tapi dari usia 31-85 tahun justru kebanyakan dari penumpang merasa puas terhadap maskapai penerbangan.

## Class for Label

Sebelumnya saya sudah melihat komparasi antara age dan label, sekarang saya mencoba melihat fitur `Class` terhadap label yang saya miliki. Sebelumnya dalam fitur Class saya memiliki 3 kategori di dalamnya yaitu,

- Eco
- Eco Plus
- Business

Ketiga Class tersebut merupakan kategori yang di dalam fitur `Class`, sekarang saya coba melihatnya dalam bentuk grafik agar mudah di baca.

![classVSlabel](image/EDA/class_for_label.png)

Class yang digunakan dalam maskapai penerbangan sangat mempengaruhi tingkat kepuasan dari penumpang, Class Eco dan Eco Plus menjadi kelas yang memiliki tingkat ketidak puasan yang cukup tinggi, sedangkan Class Business hampir `60%` dari penumpang merasa puas.

Mungkin ada beberapa fasilitas tambahan yang di sediakan atau sebuah prioritas terhadap penumpang dengan Class Business, sehingga kenyamanan yang di berikan sesuai dengan harga yang di bayar.

## Class for Customer Type

Kita tau bahwa kategori Class terbagi menjadi 3, kemudian ada lagi yang namanya Customer Type yang terbagi menjadi 2 yaitu,

- Loyal Customer
- Disloyal Customer

Loyal berarti penumpang yang setia menggunakan layanan maskapai sedangkan Disloyal berarti sebaliknya. Di sini saya ingin melihat antara keduanya dengan visual agar mudah dalam membaca informasi dari kedua fitur tersebut. Serta juga kita akan melihat jumlah dari pengguna Class paling banyak,

![classVScustomerType](image/EDA/class_for_custuomer_type.png)
![countClass](image/EDA/count_class.png)

Dari ketiga Class kita tau bahwa ketiganya memiliki Loyal Customer lebih banyak daripada Disloyal, karena memang data yang kita miliki kebanyakan dilakukan kepada customer Loyal.

Pengguna Business memang terlihat yang paling banyak, namun antara Eco dan Eco Plus ada jarak yang signifikan. Kita tau Eco plus adalah class yang lebih tinggi dari Eco, akan tetap pengguna dengan Class Eco jauh lebih banyak.

Mungkin dari segi kenyamanan yang di tawarkan tidak semewah Business dan harga yang di patok lebih mahal dari pada Eco membuat customer berfikir 2 kali. Jika dengan kenyamanan yang di tambahkan hanya sedikit dan harga yang tawarkan terbilang lebih mahal, maka Customer akan tetap memilih class Eco untuk menghemat uang mereka.

## Class for Flight Distance

Saya juga melihat dari segi jarak tempuh penumpang terhadap Class yang digunakan nya,

![classVSflightDistance](image/EDA/class_for_flightDistance.png)

Bahkan jarak tempuh sangat mempengaruhi pemilihan Class pada Customer, kalau kita lihat Class Eco dan Eco Pluss rata-rata hanya untuk jarak tempuh yang relatif dekat. Namun jika jaraknya sudah sangat jauh, biasanya Customer memilih untuk membeli tiket Business karena kenyamanan dalam perjalanan jauh cukup penting.

## Type of Travel for Class

![totVSclass](image/EDA/typeOfTravel_for_class.png)

- **Personal Travel** </br> Personal Travel sendiri merujuk pada tujuan perjalanan untuk pribadi atau liburan, kebanyakakan dari mereka yang Personal Travel hanya akan membeli Class Eco untuk mengirit biaya transportasi. Sedikit orang yang memilih Eco Plus apalagi memilih Class Business untuk perjalanan pribadi.
- **Business Travel** </br> Business Travel merujuk pada tujuan perjalanan kepentingan bisnis. Dan sudah pasti jelas pada Business Travel Class yang dipilih adalah Business, namun juga ada Business Travel yang memilih untuk Class Eco, dan sangat sedikit untuk Eco Plus.

## Arrival Delay dan Depature Delay
### Arrival
![arrivalDelay](image/EDA/arrivalDelay_for_label.png)

![depatureDelay](image/EDA/depatureDelay_for_label.png)

kalau kita lihat keduanya rata-rata keterlambatan maskapai itu di sekitar 14-15 Menit, dan ada beberapa maskapai yang keterlambatannya mencapai 1600 dalam Menit. Jika dilihat grafik di atas bagian kanan maka akan ada garis merah, yang sudah pasti jelas bahwa keterlambatan yang begitu lama sangat membuat customer merasa tidak puas.

## Like Rating Value

Maksudnya kebanyakan fitur di dalam dataset berupa nilai rating, bahkan 60%-70% dataset kita berupa rating dari semua fasilitas maskapai penerbangan, walaupun saya pikir mungkin ada beberapa fasilitas yang tidak di masukan ke dalam dataset.

Tingkat Rating

- `0` Sangat Tidak Bagus
- `1` Tidak Bagus
- `2` Cukup Bagus
- `3` Bagus
- `4` Sangat Bagus
- `5` Luar Biasa Bagus

![rating](image/EDA/rating_service.png)

# Kesimpulan

1. Customer yang memiliki umur di bawah 30 memiliki tingkat ketidak puasan yang lebih tingi.
2. Class Eco dan Eco Plus memiliki tingkat ketidak puasan yang lebih tinggi ketimbang Business yang memiliki tingkat puas yang cukup tinggi.
3. Dan kebanyakan dari Customer merupakan Customer yang Loyal.
4. Customer lebih prefer ke Class Eco ketimbah Eco Plus, mungkin dari segi harga lebih murah.
5. Jarak tempuh yang begitu jauh Customer lebih memilih Business untuk kenyamanan perjalanan.
6. Class Eco dan Eco Plus lebih sering digunakan untuk Personal Travel, ketimbang Class Business yang biasanya digunakan untuk Business Travel/perjalanan bisnis.
7. Dan pasti keterlambatan yang begitu parah benar-benar sangat mempengaruhi tingkat kepuasan Customer maskapai.
