#tạo một danh sách rỗng để lưu trữ kết quả
j=[]
#duyệt qua tất cả các số trong đoạn từ 2000 đến 3200, kiểm tra xem số đó có chia hết cho 7 và không chia hết cho 5 hay không
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        j.append(str(i))
print(','.join(j))