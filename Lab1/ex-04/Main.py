from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("*******************************")
    print("** 1. Them sinh vien.")
    print("** 2. Cap nhat thong tin sinh vien boi ID.")
    print("** 3. Xoa sinh vien boi ID.")
    print("** 4. Tim kiem sinh vien theo ten.")
    print("** 5. Sap xep sinh vien theo diem trung binh.")
    print("** 6. Sap xep sinh vien theo ten.")
    print("** 7. Hien thi danh sach sinh vien.")
    print("** 0. Thoat.")
    print("*******************************")

    try:
        key = int(input("Nhap tuy chon: "))
    except ValueError:
        print("Vui long nhap so nguyen!")
        continue

    if key == 1:
        print("\n1. Them sinh vien.")
        qlsv.nhapSinhVien()
        print("Them sinh vien thanh cong!")

    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            print("\n2. Cap nhat thong tin sinh vien.")
            ID = int(input("Nhap ID: "))
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sach sinh vien trong!")

    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Xoa sinh vien.")
            ID = int(input("Nhap ID: "))
            if qlsv.deleteById(ID):
                print("Sinh vien co ID = {} da bi xoa.".format(ID))
            else:
                print("Sinh vien co ID = {} khong ton tai.".format(ID))
        else:
            print("Danh sach sinh vien trong!")

    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("Nhap ten de tim kiem: ")
            result = qlsv.findByName(name)
            qlsv.showSinhVien(result)
        else:
            print("Danh sach sinh vien trong!")

    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sap xep sinh vien theo diem trung binh.")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")

    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sap xep 1sinh vien theo ten.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")

    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hien thi danh sach sinh vien.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sach sinh vien trong!")

    elif key == 0:
        print("Ban da chon thoat chuong trinh.")
        break

    else:
        print("Khong co chuc nang nay. Hay chon lai!")