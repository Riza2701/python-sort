def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Daftar angka yang ingin diurutkan
numbers = [42, 19, 33, 8, 55]

# Memanggil fungsi bubble_sort_descending
bubble_sort_descending(numbers)

# Menampilkan daftar angka yang sudah diurutkan secara descending
print(numbers)