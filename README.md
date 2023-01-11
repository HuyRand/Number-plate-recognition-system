<h1 align ='center' style = 'color:red;'> <b> Thị giác máy tính trong tương tác giữa người và máy  </b></h1>

## Giới thiệu môn học

* **Tên môn học:** Thị giác máy tính trong tương tác giữa người và máy
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
## Dataset
Bộ dataset kí tự được lấy từ bộ dữ liệu được cung cấp bởi miAI: https://drive.google.com/file/d/17jmzqJCsbaX22kMBymorxad8WkRVNnoF/view?usp=sharing

Bộ dataset biển số xe ô tô gồm 192 ảnh được lấy bộ dữ liệu hình ảnh biển số xe ô tô của thigiacmaytinh.com và được nhóm tự label: https://drive.google.com/drive/folders/1Rhgx6nfW4JesW7Gz2HbxMVp5puH5eGSD?usp=sharing
## Chạy chương trình
Chạy file test Test.py , thay đổi path của cv2.imread ở dòng thứ 11 sẽ thay đổi tấm ảnh muốn chạy
Sau khi chạy file sẽ xuất hiện 2 hình ảnh

<img src ="./img/bienso.png" alt ="Ảnh biển số" width = "350" height ="250"/>
<img src ="./img/anhxe.png" alt ="Ảnh đọc biển số" width ="350" height ="250"/>

## Chạy file test độ chính xác của mô hình 
Tải bộ dataset biển số xe được đưa ra trên và cho vào thư mục chương trình

Install các công cụ để tính độ CER và WER
```
pip install pybind11
pip install fastwer
```
Chạy file Test2.py
## Deploy app locally 
Chạy file app.py , chương trình sẽ được chạy local trên url: http://127.0.0.1:5000 

## Deployment 
Ứng dụng được deploy trên heroku trên đường link(deprecated, heroku stops being free): https://cs532.herokuapp.com/
