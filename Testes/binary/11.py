import array

arr = array.array("i", [10, 5, 9, 5, 1, 4])
arr_bin = arr.tobytes()

new_arr = array.array("i") # array vazio
new_arr.frombytes(arr_bin)

print(new_arr)

