def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        swapped = False
        for j in range(length - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Daftar nilai sebelum diurutkan
nilai_hannah = [78, 65, 90, 82, 70]
print("Daftar nilai sebelum diurutkan:", nilai_hannah)

# Panggil fungsi bubble_sort untuk mengurutkan daftar nilai
bubble_sort(nilai_hannah)

# Daftar nilai setelah diurutkan
print("Daftar nilai setelah diurutkan:", nilai_hannah)