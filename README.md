<h1 align ='center' style = 'color:red;'> <b> Thị giác máy tính trong tương tác giữa người và máy  </b></h1>

## Giới thiệu môn học

* **Tên môn học:** Nhập môn Thị giác máy tính
* **Mã môn học:** CS532
* **Mã lớp:**  CS532.M21.KHCL
* **Giảng viên:** Đỗ Văn Tiến

## Thành viên
| STT | MSSV       |Họ và tên       |
| ----|:----------:|----------------|
| 1   | 19521622   | Nguyễn Quan Huy|
| 1   | 19521270   | Nguyễn Nhật Huy|
| 1   | 19522395   | Trương Đình Đức Trí|

## Thông tin đồ án
* ***Tên đồ án:*** Nhận dạng biển số xe ô tô
* ***Công cụ:*** VS Code và flask

## Cài đặt môi trường
Clone repository và tạo môi trường sử dụng file requirements.txt

```
pip install -r requirements.txt
```

## Chạy chương trình
Chạy file test Test.py , thay đổi path của cv2.imread ở dòng thứ 11 sẽ thay đổi tấm ảnh muốn chạy
Sau khi chạy file sẽ xuất hiện 2 hình ảnh

<img src ="./img/bienso.png" alt ="Ảnh biển số" width = "350" height ="250"/>
<img src ="./img/anhxe.png" alt ="Ảnh đọc biển số" width ="350" height ="250"/>

## Deploy app locally 
Chạy file app.py , chương trình sẽ được chạy local trên url: http://127.0.0.1:5000 

## Deployment 
Ứng dụng được deploy trên heroku trên đường link: https://cs532.herokuapp.com/
