from datetime import datetime

class SinhVien:
    # Bien cua lop, chung cho all doi tuong thuoc lop
    truong = "Dai hoc Da Lat"

    #Ham khoi tao, ham tao lap: khoi gan cac thuoc tinh cua doi tuong
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo #thuoc tinh private
        self.__hoTen = hoTen #thuoc tinh private
        self.__ngaySinh = ngaySinh #thuoc tinh private

    #cho phep truy xuat toi thuoc tinh tu ben ngoai thong qua truong maSo
    @property
    def maSo(self):
        return self.__maSo
    
    #cho phep thay doi gia tri thuoc tinh maSo
    @maSo.setter
    def maSo(self, maso):
        if self.laMaSoHopLe(maso):
            self.__maSo = maso
    
    #phuong thuc tinh : cac phuong thuc 0 truy xuat gi den thuoc tinh, hanh vi cua lop
    #nhung phuong thuc nay khong can truyen tham so mac dinh self
    #day 0 phai la 1 hanh vi (phuong thuc) cua 1 doi tuong thuoc lop
    @staticmethod
    def doiTenTruong(self, tenmoi):
        self.truong = tenmoi

    #tuong tu ghi de phuong thuc toString()
    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"

    #hanh vi cua doi tuong sinh vien
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
