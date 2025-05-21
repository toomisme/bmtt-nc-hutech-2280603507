from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("***************************MENU***************************")
    print("**  1. Them sinh vien                                   **")
    print("**  2. Cap nhat thong tin sinh vien boi ID              **")
    print("**  3. Xoa sinh vien boi ID                             **")
    print("**  4. Tim kiem sinh vien theo ten                      **")
    print("**  5. Sap xep sinh vien theo diem trung binh           **")
    print("**  6. Sap xep sinh vien theo chuyen nganh              **")
    print("**  7. Hien thi danh sach sinh vien                     **")
    print("**  0. Thoat chuong trinh                               **")
    print("**********************************************************")
    
    key = int(input("Nhap lua chon: "))
    if (key == 1):
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")
        
    elif (key == 2):
        if (qlsv.soluongSinhVien() > 0):
            print("\n2. Cap nhat thong tin sinh vien")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien trong!")
            
    elif (key == 3):
        if (qlsv.soluongSinhVien() > 0):
            print("\n3. Xoa sinh vien")
            print("\nNhap ID: ")
            ID = int(input())
            if(qlsv.deleteSinhVien(ID)):
                print("\nSinh vien co ID = {} da bi xoa".format(ID))
            else:
                print("\nSinh vien co ID = {} khong ton tai".format(ID))
        else:
            print("Danh sach sinh vien trong!")
        
    elif (key == 4):
        if (qlsv.soluongSinhVien() > 0):
            print("\n4. Tim kiem sinh vien theo ten")
            print("\nNhap ten sinh vien: ")
            name = input()
            listSV = qlsv.findbyName(name)
            searchResult = qlsv.findbyName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sach sinh vien trong!")
            
    elif (key == 5):
        if (qlsv.soluongSinhVien() > 0):
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA)")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
        
    elif (key == 6):
        if (qlsv.soluongSinhVien() > 0):
            print("\n6. Sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
        
    elif (key == 7):
        if (qlsv.soluongSinhVien() > 0):
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")
        
    elif (key == 0):
        print("\nBan da chon thoat chuong trinh!")
        break
    
    else:
        print("Lua chon khong hop le")