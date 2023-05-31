def bubble_sort_books(books):
    n = len(books)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if books[j]['Jumlah Halaman'] > books[j+1]['Jumlah Halaman']:
                books[j], books[j+1] = books[j+1], books[j]
    
    return books

# Daftar buku yang perlu diurutkan
books = [
    {
        'No.': 1,
        'Judul Buku': "Harry Potter and the Sorcerer's Stone",
        'Penulis': "J.K. Rowling",
        'Jumlah Halaman': 320
    },
    {
        'No.': 2,
        'Judul Buku': "To Kill a Mockingbird",
        'Penulis': "Harper Lee",
        'Jumlah Halaman': 281
    },
    {
        'No.': 3,
        'Judul Buku': "The Great Gatsby",
        'Penulis': "F. Scott Fitzgerald",
        'Jumlah Halaman': 180
    },
    {
        'No.': 4,
        'Judul Buku': "Pride and Prejudice",
        'Penulis': "Jane Austen",
        'Jumlah Halaman': 432
    },
    {
        'No.': 5,
        'Judul Buku': "1984",
        'Penulis': "George Orwell",
        'Jumlah Halaman': 328
    }
]

# Mengurutkan daftar buku menggunakan Bubble Sort
sorted_books = bubble_sort_books(books)

# Menampilkan daftar buku yang sudah diurutkan
print("Daftar Buku yang Sudah Diurutkan:")
print("No.  Judul Buku                           Penulis                  Jumlah Halaman")
print("------------------------------------------------------------------------------")
for book in sorted_books:
    print(f"{book['No.']:<5} {book['Judul Buku']:<35} {book['Penulis']:<25} {book['Jumlah Halaman']}")