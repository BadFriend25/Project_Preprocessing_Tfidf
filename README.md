# Project_WordValuer
 
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


