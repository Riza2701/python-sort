def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Daftar angka yang ingin diurutkan
numbers = [9, 5, 3, 8, 2]

# Panggil fungsi selection_sort
sorted_numbers = selection_sort(numbers)

# Tampilkan hasil pengurutan
print("Hasil pengurutan:", sorted_numbers)