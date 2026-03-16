class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem


    def __eq__(self, other):
        return self.diem == other.diem



sv1 = SinhVien("Phong", 8)
sv2 = SinhVien("Hieu", 8)
sv3 = SinhVien("Linh", 9)

print(sv1 == sv2) 
print(sv1 == sv3)  



class SinhVien:
    dem = 0  

    def __init__(self, ten):
        self.ten = ten
        SinhVien.dem += 1

    @classmethod
    def so_luong(cls):
        return cls.dem

sv1 = SinhVien("Phong")
sv2 = SinhVien("Hieu")
sv3 = SinhVien("Linh")

print("Số sinh viên đã tạo:", SinhVien.so_luong())