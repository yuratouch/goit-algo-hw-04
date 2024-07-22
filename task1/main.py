import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def generate_random_list(size):
    return [random.randint(0, size) for _ in range(size)]

def time_algorithm(algorithm, data):
    start_time = timeit.default_timer()
    algorithm(data)
    return timeit.default_timer() - start_time

sizes = [100, 1000, 10000]

for size in sizes:
    data = generate_random_list(size)

    print(f"Array size: {size}")

    merge_time = time_algorithm(merge_sort, data.copy())
    print(f"Merge Sort: {merge_time:.6f} seconds")

    insertion_time = time_algorithm(insertion_sort, data.copy())
    print(f"Insertion Sort: {insertion_time:.6f} seconds")

    timsort_time = time_algorithm(sorted, data.copy())
    print(f"Timsort: {timsort_time:.6f} seconds")

    print()


"""
Висновки:
За результатами проведеного тестування можна зробити висновки, що вбудовані функції Python
sort та sorted є найбільш ефективними в силу комбінованого підходу сортування з використанням 
алгоритмів сортування злиттям та вставкою. Це виправдовує використання програмістами вбудованих
функцій Python при розробці, оскільки вони є оптимізованими та ефективними. Сортування методом 
вставки показав найнижчу ефективність на великих масивах даних. 
"""

    