class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu = tu
        self.mau = mau

    def nhapPhanSo(self):
        self.tu = int(input("Nhập tử số: "))
        self.mau = int(input("Nhập mẫu số: "))

    def xuatPhanSo(self):
        print(self.tu, "/", self.mau)

class DanhSachPhanSo:
    def __init__(self):
        self.ds = []

    def themPhanSo(self, phanSo):
        self.ds.append(phanSo)

    def demSoPhanSoAm(self):
        dem = 0
        for phanSo in self.ds:
            if phanSo.tu * phanSo.mau < 0:
                dem += 1
        return dem

    def timPhanSoDuongNhoNhat(self):
        phanSoMin = None
        for phanSo in self.ds:
            if phanSo.tu * phanSo.mau > 0:
                if phanSoMin is None or phanSo.tu / phanSo.mau < phanSoMin.tu / phanSoMin.mau:
                    phanSoMin = phanSo
        return phanSoMin

    def timViTriCuaPhanSo(self, x):
        viTri = []
        for i, phanSo in enumerate(self.ds):
            if phanSo.tu == x.tu and phanSo.mau == x.mau:
                viTri.append(i)
        return viTri

    def tongCacPhanSoAm(self):
        tong = 0
        for phanSo in self.ds:
            if phanSo.tu * phanSo.mau < 0:
                tong += phanSo.tu / phanSo.mau
        return tong

    def xoaPhanSo(self, x):
        self.ds = [phanSo for phanSo in self.ds if (phanSo.tu != x.tu or phanSo.mau != x.mau)]

    def xoaTatCaPhanSoCoTuLa(self, x):
        self.ds = [phanSo for phanSo in self.ds if phanSo.tu != x]

    def sapXepPhanSo(self, kieu):
        self.ds.sort(key=lambda phanSo: (phanSo.tu / phanSo.mau) if kieu == "tang" else -(phanSo.tu / phanSo.mau))

danhSach = DanhSachPhanSo()
danhSach.themPhanSo(PhanSo(1, 2))
danhSach.themPhanSo(PhanSo(-25, 33))
danhSach.themPhanSo(PhanSo(3, 4))
danhSach.themPhanSo(PhanSo(100, 355))
danhSach.themPhanSo(PhanSo(20, -63))


print("Danh sách phân số : ")
for phanSo in danhSach.ds:
    phanSo.xuatPhanSo()

print("\nCó :", danhSach.demSoPhanSoAm()," phân số âm trong mảng")

phanSoMin = danhSach.timPhanSoDuongNhoNhat()
if phanSoMin is not None:
    print("\nPhân số dương nhỏ nhất:")
    phanSoMin.xuatPhanSo()

x = PhanSo(3, 4)
print("\nVị trí của phân số", end=" ")
x.xuatPhanSo()

print("trong mảng:", danhSach.timViTriCuaPhanSo(x))
print("\nTổng các phân số âm trong mảng:", danhSach.tongCacPhanSoAm())

x = PhanSo(1, 2)
print("\nXóa phân số", end=" ")
x.xuatPhanSo()
danhSach.xoaPhanSo(x)
print("Mảng sau khi xóa:")
for phanSo in danhSach.ds:
    phanSo.xuatPhanSo()
x = 2
print("\nXóa tất cả phân số có tử là", x)
danhSach.xoaTatCaPhanSoCoTuLa(x)

print("Mảng sau khi xóa:")
for phanSo in danhSach.ds:
    phanSo.xuatPhanSo()

print("\nSắp xếp phân số theo chiều tăng:")
danhSach.sapXepPhanSo("tang")
for phanSo in danhSach.ds:
    phanSo.xuatPhanSo()

print("\nSắp xếp phân số theo chiều giảm:")
danhSach.sapXepPhanSo("giam")
for phanSo in danhSach.ds:
    phanSo.xuatPhanSo()





