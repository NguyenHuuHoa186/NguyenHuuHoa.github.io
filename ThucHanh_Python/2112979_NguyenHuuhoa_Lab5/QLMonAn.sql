CREATE DATABASE QLMonAn
 
CREATE TABLE MonAn(
	MaMonAn int  NOT NULL PRIMARY KEY,
	TenMonAn nvarchar(50) NOT NULL,
	DonViTinh nvarchar(50) NULL,
	DonGia int NULL,
	Nhom int NULL)

CREATE TABLE NhomMonAn(
	MaNhom int  NOT NULL PRIMARY KEY,
	TenNhom nvarchar(50) NOT NULL)
 
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (1, N'Gỏi thập cẩm', N'Dĩa', 120000, 1)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (2, N'Gỏi sứa', N'Dĩa', 140000, 1)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (3, N'Gỏi tai heo', N'Dĩa', 110000, 1)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (4, N'Tôm nướng muối ớt', N'Kg', 250000, 2)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (5, N'Mực nướng muối ớt', N'Kg', 290000, 2)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (6, N'Tôm hấp bia', N'Kg', 230000, 2)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (7, N'Sò nướng mỡ hành', N'Kg', 300000, 2)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (8, N'Bia Heniken', N'Chai', 18000, 3)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (9, N'Bia tiger bạc', N'Chai', 16000, 3)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (10, N'Coca', N'Lon', 16000, 3)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (11, N'Lẩu hải sản', N'Nồi', 220000, 4)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (12, N'Lẩu cá tầm', N'Nồi', 270000, 4)
INSERT MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (14, N'Lẩu gà lá é', N'nồi', 250000, 4)

select * from MonAn

INSERT NhomMonAn (MaNhom, TenNhom) VALUES (1, N'Khai vị')
INSERT NhomMonAn (MaNhom, TenNhom) VALUES (2, N'Hải sản')
INSERT NhomMonAn (MaNhom, TenNhom) VALUES (3, N'Bia - Nước ngọt')
INSERT NhomMonAn (MaNhom, TenNhom) VALUES (4, N'Lẩu')

SELECT * FROM NhomMonAn
