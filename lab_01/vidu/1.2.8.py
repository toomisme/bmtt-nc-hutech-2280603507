#khai báo hàm
def my_function(parameter1,parameter2):
    result = parameter1 + parameter2
    return result

#cách sử dụng
#gọi hàm 
result = my_function(10,20)
print(result)

#Tham số và đối số
def caculate_sum(a,b): #định nghĩa hàm tính tổng
    result = a + b
    return result
sum_result = caculate_sum(10,20) #gọi hàm và lưu kết quả vào biến
print("Tổng hai số là:",sum_result)

#hàm không trả về giá trị chỉ in ra thông báo
def greet(name):
    print("xin chào,",name)
greet("Alice")
