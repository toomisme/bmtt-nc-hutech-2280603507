#khai báo
from array import array
int_array = array('i',[1,2,3,4,5])
float_array = array('f',[3.14,2.5,6.7])

#truy cập phần tử trong mảng
print(int_array[0])
print(float_array[2])

#cập nhật giá trị trong mảng
int_array[2] = 10
