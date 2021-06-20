import time

def biniry_search(lys, target):
    if len(lys) < 1:
        return -1
    mid_idx = (len(lys)-1)//2
    mid_val = lys[mid_idx]
    if target == mid_val:
        return mid_idx
    elif target < mid_val:
        return biniry_search(lys[:mid_idx], target)
    else:
        right = biniry_search(lys[mid_idx+1:], target)
        right_corr = mid_idx + right + 1
        if lys[right_corr] == target:
            return right_corr
        else:
            return -1
def biniry_search_indeses(lys, target):
    if len(lys) < 1:
        return -1
    left = 0
    right = len(lys)-1
    while left <= right:
        mid_idx = left + (right-left)//2
        mid_val = lys[mid_idx]
        if target == mid_val:
            return mid_idx
        elif target < mid_val:
            right = mid_idx -1
        else:
            left = mid_idx + 1
    return -1



#
ns = list(range(8*200000))
tt = time.time()
biniry_search(ns, 200000)
tt2 = time.time() - tt
print(f"Bites long: {ns.__sizeof__()}. Searched for: {tt2}")


tt3 = time.time()
biniry_search_indeses(ns, 200000)
tt4 = time.time() - tt3
print(f"Bites long: {ns.__sizeof__()}. Searched for: {tt4}")
# def sparse_search(data, search_val):
#   print("Data: " + str(data))
#   print("Search Value: " + str(search_val))
#   first = 0
#   last = len(data)-1
#   while first <= last:
#     mid = (first + last)//2
#     if not data[mid]:
#       left = mid - 1
#       right = mid + 1
#       while True:
#         if left < first and right > last:
#           print("{} is not in the dataset".format(search_val))
#           return
#         elif right <= last and data[right]:
#           mid = right
#           break
#         elif left >= first and data[left]:
#           mid = left
#           break
#         right = right +1
#         left += left +1
#     if data[mid] == search_val:
#       print("{0} found at position {1}".format(search_val, mid))
#       return
#     elif data[mid] < search_val:
#       first = mid + 1
#     else:
#       last = mid - 1
#
#
#   print("{0} is not in the dataset".format(search_val))
#


# sparse_search(["A", "", "", "", "B", "", "", "", "C", "", "", "D"], "A")
