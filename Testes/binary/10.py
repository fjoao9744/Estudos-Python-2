import array

arr = array.array("i", [10, 5, 9, 5, 1, 4])
print(arr)

arr.append(20)
arr.pop(1)

arr_bin = arr.tobytes()

print(arr_bin)
