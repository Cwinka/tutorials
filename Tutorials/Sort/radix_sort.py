from random import shuffle
import time
def radix_sort(to_be_sorted):
    maximum_value = max(to_be_sorted)
    max_exponent = len(str(maximum_value))
    being_sorted = to_be_sorted[:]

    for exponent in range(max_exponent): # W
        position = exponent + 1
        index = -position

        digits = [[] for i in range(10)]

        for number in being_sorted: # N
            number_as_a_string = str(number)
            try:
                digit = number_as_a_string[index]
                digit = int(digit)
            except IndexError:
                digit = 0

            digits[digit].append(number)

        being_sorted = []
        for numeral in digits:
            being_sorted.extend(numeral)

    return being_sorted

unsorted_list1 = list((12,41,21,44,12,76,95,34)*120000) #здесь набор данных с максимальной длинной экспоненты 2, если брать range(), то runtime O(N*W)
shuffle(unsorted_list1)
tt = time.time()
radix_sort(unsorted_list1)
tt2 = time.time() - tt
print(f"Bites long: {unsorted_list1.__sizeof__()}. Sorted for: {tt2}")
# # O(NW) w это колличество цифр в макс экспоненте
# # Омега(N)
