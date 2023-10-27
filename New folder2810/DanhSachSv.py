from SinhVien import SinhVien
from datetime import datetime
class DanhSachSv:
    def __init__(self) -> None:
        self.dssv = []

    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    #tim sinh vien theo mssv, neu co tra ve sinh vien
    def timSvtheoMssv(self, mssv: int):
        return [sv for sv in self.dssv if sv.mssv == mssv]

    #tim sinh vien theo mssv, neu co tra ve vi tri cua sinh vien trong ds
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1

    #xoa sinh vien co ma so mssv, thong bao xoa dc hoac 0
    def xoaSvTheoMssv(self, moSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False

    #Tim sinh vien ten "Nam"
    def timSvTheoTen(self, ten: str):
        return [sv for sv in self.dssv if sv.hoTen == ten]

    #Tim nhung sinh vien sinh truoc 15/06/2000
    def timSvSinhTruocNgay(self, ngay: datetime):
        return [sv for sv in self.dssv if sv.ngaySinh < ngay]

    def DocTuFile(self, tenFile):
        with open(tenFile, 'r', encoding='utf-8') as f:
            for hang in f:
                dl = hang.split('*')
                ms = int(dl[0])
                ht = dl[1]
                ns = datetime.strptime(dl[2].strip("\n"), "%d/%m/%Y")
                sv = SinhVien(ms, ht, ns)
                self.themSinhVien(sv)
    
    def SapXepTangTheoTen(self):
        return self.dssv.sort(key = lambda x: x.__hoTen, reverse=False)
    
    def SapXepGiamTheoTen(self):
        return self.dssv.sort(key = lambda x: x.__hoTen, reverse=True)

ds = DanhSachSv()
ds.DocTuFile('dssv.txt')
ds.xuat()

#ds.SapXepTangTheoTen()
#mssv = str(input("Mời nhập mã số muốn tìm: "))
#ds.timSVTheoMSSV(mssv)