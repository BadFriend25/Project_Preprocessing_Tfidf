# Project_WordValuer
---
 
Tujuan dari prosedur ini adalah untuk mengekstrak semua kata unik dari file PDF, kecuali beberapa stop word - yaitu kata seperti 'dan', 'di', 'yang', 'dari', & 'ke' - dan mengurutkannya berdasarkan skor TF-IDF.

Berikut adalah langkah-langkah untuk mencapai hal ini:
1. Impor library yang diperlukan:
    - `PyPDF2` digunakan untuk mengekstrak teks dari file PDF.
    - `string` digunakan untuk menghapus tanda baca dari teks.
    - `sklearn.feature_extraction.text.TfidfVectorizer` digunakan untuk menghitung skor TF-IDF untuk setiap kata dalam file PDF.
2. Menentukan fungsi `get_all_words_in_pdf` yang membutuhkan dua argumen:
    - `pdf_path` adalah jalur ke file PDF.
    - `stop_words` adalah daftar stop word untuk dikecualikan dari daftar kata.
3. Membuka file PDF dalam mode biner menggunakan fungsi `open` dan baca menggunakan kelas `PyPDF2.PdfReader`.
4. Mengekstrak teks dari setiap halaman dalam file PDF menggunakan metode `extract_text` dari kelas `PyPDF2.page`.
5. Menggabungkan seluruh teks dari seluruh halaman menjadi satu string.
6. Tokenisasi teks menjadi kata-kata dengan cara memotong rangkaian kata berdasarkan letak spasi.
7. Mengapus tanda baca dari kata-kata menggunakan method `translate` dari kelas `str` dan method `maketrans` dari modul `string`.
8. Buat objek `TfidfVectorizer` dengan argumen `stop_words`yang di set ke daftar stop word.
9. Sesuaikan objek `TfidfVectorizer` dengan daftar kata menggunakan metode `fit_transform`.
10. Lakukan GET pada kata unik dan skor TF-IDF-nya menggunakan metode `get_feature_names_out` dan `toarray` pada objek `TfidfVectorizer`.
11. RETURN kata unik dan skor TF-IDF sebagai tuple.
12. Definisikan daftar stop word yang ada didalam bahasa Indonesia.
13. Definisikan alamat file PDF yang akan digunakan.
14. Panggil fungsi `get_all_words_in_pdf` dengan argumen `stop_words` diatur ke daftar stop word dan argumen `pdf_path` diatur ke alamat file PDF.
15. Dapatkan nama unik dan skor TF-IDF sebagai tuple.
16. Urutkan kata-kata berdasarkan skor TF-IDF mereka dalam urutan menurun menggunakan fungsi `sorted` dan argumen `zip` dan `reverse`.
17. Cetak 10 kata teratas dan 10 kata terbawah berdasarkan skor TF-IDF-nya menggunakan daftar `sorted_words` dan irisan `[:10]` dan `[-10:]`.  

Dengan mengikuti langkah-langkah ini, Kata unik / Unique Word dapat diekstrak dari file PDF, kecuali kata-kata yang ada didaftar stop word, dan mengurutkannya berdasarkan nilai TF-IDF, yang merepresentasikan keunikannya di dalam file PDF.

---

- Data
    - [Kementerian Kominfo: Situs Elaelo Pengganti X/Twitter Bukan Buatan Pemerintah](https://tekno.kompas.com/read/2024/06/19/10310047/kementerian-kominfo--situs-elaelo-pengganti-x-twitter-bukan-buatan-pemerintah)  
    Artikel Utama pada [halaman utama kompas.com](https://www.kompas.com/) pada tanggal 19 Juni 2024.  
    - Samkok : Kisah Tiga Kerajaan
    Novel yang ditulis oleh Luo Guanzhong ditranslasikan oleh Leo Junaedi. Salah satu dari empat kumpulan novel klasik Tiongkok. Menceritakan tentang jatuhnya kekaisaran dinasti Han (206 BC–220 AD) dan kekacauan yang terjadi pada waktu itu.  

- #### Hardware   
    - ##### Lenovo Thinkpad X260  
    
    Processor	Intel(R) Core(TM) i5-6200U CPU @ 2.30GHz  
    Video Card	Intel(R) HD Graphics 520  
    Operating System	Windows 10  
    RAM	8.0 GB  

- #### Software   
    - ##### Jupyter Lab  
    JupyterLab adalah lingkungan pengembangan interaktif berbasis web untuk pemrograman dalam beberapa bahasa pemrograman, terutama Python. Ini adalah pengembangan dari proyek Jupyter Notebook, yang dikenal luas di kalangan ilmu data, peneliti, dan pengembang karena kemampuannya menyediakan lingkungan interaktif untuk menulis dan menjalankan kode, menampilkan visualisasi data, dan menyusun dokumen dengan campuran elemen teks, kode, dan output.  

    Berikut beberapa poin penting tentang JupyterLab:  

    1. **Antarmuka Web**: JupyterLab menyediakan antarmuka pengguna berbasis web yang fleksibel dan kuat. Ini memungkinkan pengguna untuk bekerja dengan notebook, editor teks, terminal, dan berbagai komponen lainnya dalam satu tampilan yang terintegrasi.

    2. **Integrasi dengan Jupyter Notebooks**: JupyterLab mempertahankan kemampuan Jupyter Notebook untuk menulis kode dalam sel-sel yang dapat dieksekusi secara terpisah. Ini memungkinkan pengguna untuk menjalankan kode, melihat outputnya, dan menyimpan hasilnya dalam satu dokumen interaktif.

    3. **Fleksibilitas dan Ekstensibilitas**: JupyterLab dirancang untuk menjadi fleksibel dan dapat diperluas. Pengguna dapat menyesuaikan antarmuka pengguna, mengatur layout tampilan, dan mengintegrasikan ekstensi tambahan untuk menambahkan fungsionalitas baru.

    4. **Multi-language Support**: Meskipun Python adalah bahasa yang paling umum digunakan dalam JupyterLab, lingkungan ini mendukung beberapa bahasa pemrograman lainnya seperti R, Julia, dan banyak lainnya. Ini membuatnya cocok untuk pengembangan dan analisis data lintas platform.

    5. **Interaktif dan Visualisasi Data**: JupyterLab memfasilitasi interaksi langsung dengan data melalui integrasi dengan pustaka visualisasi seperti Matplotlib, Plotly, dan sebagainya. Pengguna dapat membuat grafik dan visualisasi langsung dalam notebook mereka.

    6. **Komunitas dan Dukungan**: JupyterLab didukung oleh komunitas yang aktif dan memiliki dukungan yang luas dari berbagai pihak, termasuk peneliti, ilmuwan data, dan pengembang perangkat lunak.  

    Secara keseluruhan, JupyterLab adalah alat yang sangat berguna untuk pengembangan interaktif, analisis data, eksplorasi, dan dokumentasi dalam berbagai bahasa pemrograman. Itu memfasilitasi kolaborasi, pembelajaran, dan penelitian dalam sebuah lingkungan yang terintegrasi dan mudah digunakan.  
    - ##### Python  
    Python adalah bahasa pemrograman tingkat tinggi yang bersifat serbaguna, populer dalam pengembangan perangkat lunak, analisis data, pengembangan web, dan banyak aplikasi lainnya. Berikut adalah beberapa poin utama tentang Python:  

    1. **Bahasa Pemrograman**: Python adalah bahasa pemrograman yang mudah dipahami dan digunakan. Dia diketahui untuk sintaksisnya yang bersih dan mudah dibaca, yang memudahkan pengembang untuk mengekspresikan ide-ide mereka dengan jelas dan efisien.

    2. **Serbaguna**: Python mendukung berbagai paradigma pemrograman, termasuk pemrograman terstruktur, pemrograman berorientasi objek, dan pemrograman fungsional. Ini membuatnya cocok untuk berbagai tugas, dari pengembangan web hingga analisis data, kecerdasan buatan, dan pengembangan perangkat lunak.

    3. **Mudah Dipelajari**: Python sering dipilih sebagai bahasa pertama bagi pemula dalam pemrograman karena kemudahannya dipelajari dan dipahami. Ini memiliki komunitas yang besar dan aktif yang menyediakan banyak sumber daya pembelajaran.

    4. **Interpretatif dan Dinamis**: Python adalah bahasa interpretatif, yang berarti kode Python dieksekusi baris per baris oleh interpreter tanpa memerlukan proses kompilasi sebelumnya. Selain itu, Python adalah bahasa yang dinamis, yang berarti tipe data dari variabel dikenali saat waktu runtime.

    5. **Ekosistem yang Kaya**: Python memiliki ekosistem yang kaya dengan ribuan pustaka dan framework yang mendukung berbagai kebutuhan pengembangan. Contoh pustaka terkenal termasuk NumPy untuk komputasi numerik, Pandas untuk analisis data, Flask dan Django untuk pengembangan web, dan TensorFlow dan PyTorch untuk kecerdasan buatan.

    6. **Open Source dan Komunitas yang Aktif**: Python adalah perangkat lunak sumber terbuka, yang berarti kode sumbernya dapat diakses dan dimodifikasi oleh siapa saja. Ini memiliki komunitas yang besar dan aktif yang terus mengembangkan bahasa ini, menyediakan dukungan, dan menciptakan pustaka baru.  

    Python menjadi pilihan yang populer di kalangan pengembang karena kesederhanaannya, kemampuan untuk menangani berbagai tugas pemrograman, dan ekosistemnya yang luas.  
    - ##### PyPDF2  
    `PyPDF2` adalah sebuah perpustakaan (library) Python yang digunakan untuk memanipulasi dokumen PDF. Perpustakaan ini memungkinkan pengguna untuk melakukan berbagai operasi pada file PDF, seperti menggabungkan dokumen PDF, memisahkan halaman, mengubah isi halaman, dan lain-lain.  

                Berikut adalah beberapa fitur utama dari `PyPDF2`:  

                1. **Manipulasi PDF**: Menggabungkan beberapa file PDF menjadi satu file, membagi file PDF menjadi beberapa bagian, atau mengubah halaman dalam file PDF.
   
                2. **Pengambilan Informasi**: Mengekstrak informasi seperti metadata (misalnya judul, penulis, dan lain-lain) dari file PDF.

                3. **Manipulasi Konten**: Menambahkan teks, gambar, atau bentuk lainnya ke halaman PDF.

                4. **Enkripsi dan Perlindungan**: `PyPDF2` mendukung enkripsi dan perlindungan terhadap file PDF dengan menambahkan kata sandi atau mengatur izin akses.

                5. **Kompatibilitas**: Perpustakaan ini kompatibel dengan Python 2.7 dan Python 3.x.  

                `PyPDF2` tidak hanya memungkinkan akses ke konten dari file PDF tetapi juga memberikan kontrol penuh terhadap struktur dan elemen dalam dokumen PDF tersebut. Hal ini membuatnya berguna untuk otomatisasi tugas-tugas yang melibatkan dokumen PDF, seperti pengolahan batch, pembuatan laporan, atau penyuntingan konten.  

                Penting untuk dicatat bahwa `PyPDF2` adalah proyek open-source dan dapat diunduh serta digunakan secara gratis oleh pengembang Python.  
    - ##### string 1.4.0  
    Dalam konteks library Python, string merujuk pada tipe data dasar yang terdapat di dalam bahasa pemrograman Python itu sendiri. Namun, string juga dapat merujuk kepada modul atau pustaka tertentu yang digunakan untuk memanipulasi atau bekerja dengan teks dan karakter dalam Python.  

            Berikut ini beberapa pustaka atau modul Python yang umum digunakan untuk bekerja dengan string:  

            1. **`str` (String Methods)**: Ini adalah tipe data bawaan Python untuk merepresentasikan string dan menyediakan berbagai metode bawaan untuk manipulasi string, seperti `split()`, `join()`, `upper()`, `lower()`, `strip()`, dan banyak lagi.

            2. **`re` (Regular Expressions)**: Modul ini digunakan untuk pencarian dan pemrosesan pola teks kompleks menggunakan ekspresi regular (regular expressions). Dengan modul ini, developer dapat mencari, memfilter, dan memanipulasi teks berdasarkan pola tertentu.

            3. **`string` (Constants and Template Strings)**: Modul `string` menyediakan konstanta-konstanta yang digunakan dalam operasi-operasi dengan string, seperti `ascii_letters`, `digits`, `whitespace`, dan lain-lain. Modul ini juga mendukung template strings untuk formatting teks.

            4. **`textwrap` (Text Wrapping and Formatting)**: Modul ini menyediakan fungsi-fungsi untuk memformat teks menjadi paragraf atau teks yang terpotong dengan rapi berdasarkan lebar kolom tertentu.

            5. **`unicodedata` (Unicode Database)**: Modul `unicodedata` digunakan untuk bekerja dengan karakter unicode, seperti memeriksa jenis karakter (digit, huruf, dll.), mengubah huruf kecil ke huruf besar, dan sebaliknya.

            6. **`io` (Input/Output)**: Modul ini menyediakan kelas-kelas untuk memanipulasi data dalam bentuk string, seperti `StringIO` yang memungkinkan string diolah seperti file.

            7. **`PyPDF2`**: `PyPDF2` adalah sebuah library Python khusus untuk memanipulasi dokumen PDF, bukan string secara langsung, tetapi kadang-kadang string juga terlibat dalam operasi manipulasi teks dalam dokumen PDF.  

            Dengan menggunakan modul-modul ini, pengembang dapat melakukan berbagai operasi terhadap teks dan karakter dalam Python, mulai dari operasi sederhana seperti pencarian dan penggantian hingga penggunaan pola dan ekspresi regular untuk pemrosesan teks yang lebih kompleks.  
    - ##### sklearn  
    `sklearn`, atau `scikit-learn`, adalah sebuah library Python yang populer digunakan untuk machine learning. Library ini menyediakan berbagai alat dan fungsi untuk melakukan tugas-tugas umum dalam machine learning seperti klasifikasi, regresi, clustering, dan lain-lain. Berikut adalah beberapa poin utama tentang `sklearn`:  

        1. **Machine Learning Algorithms**: `sklearn` menyediakan implementasi dari berbagai algoritma machine learning, termasuk klasifikasi (misalnya SVM, k-Nearest Neighbors, decision trees), regresi (misalnya linear regression, ridge regression), clustering (misalnya k-means), dan lain-lain.

        2. **Preprocessing Data**: Library ini menyediakan berbagai fungsi untuk memproses dan mempersiapkan data sebelum melakukan pembelajaran, seperti penskalaan fitur, normalisasi, pengisian nilai yang hilang, dan ekstraksi fitur.

        3. **Evaluasi Model**: `sklearn` memiliki alat untuk mengevaluasi performa model machine learning, termasuk metrik seperti akurasi, presisi, recall, dan area di bawah kurva ROC (AUC).

        4. **Pemodelan Statistik**: Selain machine learning, `sklearn` juga menyediakan beberapa fungsi statistik dasar seperti pengujian hipotesis, regresi linear, dan analisis komponen utama (PCA).

        5. **Integrasi dengan NumPy, SciPy, dan Pandas**: `sklearn` bekerja secara langsung dengan struktur data yang umum digunakan dalam analisis data di Python, seperti array NumPy, DataFrame Pandas, dan matriks sparse SciPy.

        6. **Open Source dan Community-driven**: `sklearn` adalah proyek open source yang aktif dikembangkan dan didukung oleh komunitas yang besar, yang berarti pengguna dapat dengan mudah menemukan dokumentasi, tutorial, dan dukungan dari komunitas.  

        `sklearn` sangat populer di kalangan praktisi machine learning karena kemudahannya digunakan, dokumentasi yang kaya, dan dukungan yang luas terhadap berbagai jenis tugas machine learning.  
    - ##### Microsoft Edge  
    Microsoft Edge adalah sebuah peramban web yang dikembangkan oleh Microsoft. Ini adalah penerus dari Internet Explorer dan dirilis pertama kali pada tahun 2015 sebagai bagian dari sistem operasi Windows 10. Microsoft Edge dirancang untuk memberikan pengalaman menjelajah yang lebih cepat, lebih aman, dan lebih produktif daripada pendahulunya.  

    Beberapa fitur utama dari Microsoft Edge termasuk integrasi yang kuat dengan layanan Microsoft seperti Cortana (asisten virtual), OneDrive (layanan penyimpanan cloud), dan Office Online. Selain itu, Edge juga mendukung ekstensi untuk memperluas fungsionalitasnya, dan menggunakan mesin render baru yang disebut EdgeHTML (sebelumnya menggunakan Trident pada Internet Explorer).  

    Microsoft secara teratur mengupdate Edge dengan fitur-fitur baru dan perbaikan keamanan untuk menjaga agar tetap kompetitif dengan peramban web lainnya seperti Google Chrome, Mozilla Firefox, dan Safari.
