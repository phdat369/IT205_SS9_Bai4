# Phân tích 
# Đề bài yêu cầu chúng ta cần tạo 1 menu gồm có 4 chức năng : 
# 1. Hien thị danh sách đơn hàng
# 2. Cập nhat danh sach đon hàng
# 3. Thong ke don hang theo trang thái
# 4. Thoat chuong trinh
# Ở chức năng đầu tiên thì chúng ta cần hiển thị ra toàn bộ danh sách đơn hàng, để làm chức năng này thì chúng ta cần duyệt vòng for và in ra tất cả phần tử trong list 
# Chức năng thứ 2 thì chúng ta cần cập nhật đơn hàng 
# Trong chức năng này thì chúng ta có 1 menu con ở trong menu chính và nó cũng có 4 chức năng 
# Chức năng con đầu tiên là thêm đơn hàng thì người dùng cần nhập mã đơn hàng và trạng thái và sau đó chúng ta cần xóa khoảng trắng, chuyển mã đơn thành chữ hoa và ghép lại theo đúng định dạng 
# Tiếp theo là sửa đơn theo vị trí thì chúng ta yêu cầu người dùng nhập từ vị trí thứ 1 đi và sau đó phải kiểm tra có hợp lệ 
# Nếu hợp lệ thì cho người dùng nhập lại mã đơn và trạng thái sau đó chuẩn hóa và gán lại bằng index 
# Chức năng con tiếp theo là xóa đơn theo vị trí người dùng nhập 
# Để xóa thì đầu tiên kiểm tra vị trí người dùng nhập có hợp lệ hay không, nếu hợp lệ thì xóa còn không thì hiển thị thông báo 
# Và chức năng cuối cùng thì là quay lại menu chính 
# Còn chức năng cha thứ 3 là chức năng đếm số theo trạng thái xem mỗi trạng thái có bao nhiêu đơn hàng 
# Để làm chức năng này thì chúng ta cần tách mã đơn hàng và trạng thái sau đó đếm theo từng trạng thái 
# Và cuối cùng là break ra khỏi vòng lặp và kết thúc chương trình 

# Viết code 

order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED" ]

while True:
    choose = int(input("""===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====
1. Hiển thị danh sách đơn hàng
2. Cập nhật danh sách đơn hàng
3. Thống kê đơn hàng theo trạng thái
4. Thoát chương trình 
Chọn chức năng của bạn: """))
    print()
    match choose:
        case 1:
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống")
            else:
                for index, order in enumerate(order_list):
                    print(f"{index+1}. {order}")
            print()
        case 2:
            while True:
                pick = int(input("""----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----
1. Thêm đơn hàng mới
2. Sửa đơn hàng theo vị trí
3. Xóa đơn hàng theo vị trí
4. Quay lại menu chính
Chọn chức năng của bạn: """))
                match pick:
                    case 1:
                        id_order = input("Nhập mã đơn hàng: ")
                        status_order = input("Nhập trạng thái đơn hàng: ")
                        new_order = id_order.strip().upper() + " - " + status_order.strip().upper()
                        order_list.append(new_order)
                        print("Thêm đơn hàng thành công")
                        print()
                    case 2:
                        update_index = int(input("Nhập vị trí của đơn hàng cần sửa (Bắt đầu từ 1): "))
                        valid = True
                        for index,order in enumerate(order_list):
                            if index + 1 == update_index:
                                new_id_order = input("Nhập mã đơn hàng mới: ")
                                new_status_order = input("Nhập trạng thái mới cho đơn hàng: ")
                                update_order = new_id_order.strip().upper() + " - " + new_status_order.strip().upper()
                                order_list[update_index-1] = update_order
                                print("Cập nhật thành công")
                                print()
                                valid = False
                        if valid == True:
                            print("Không tồn tại đơn hàng ở vị trí này")
                    case 3: 
                        order_delete = int(input("Nhập vị trí sản phẩm bạn muốn xóa: "))
                        valid = True
                        for index,order in enumerate(order_list):
                            if index + 1 == order_delete:
                                order_list.pop(index)
                                print("Xóa thành công")
                                print()
                                valid = False
                        if valid == True:
                            print("Không tồn tại đơn hàng ở vị trí này")
                    case 4:
                        break
                    case _:
                        print("Lựa chọn không hợp lệ")
        case 3:
            count_pending = 0
            count_delivering = 0
            count_cancelled = 0
            count_completed = 0
            for item in order_list:
                status_item = item.split(" - ")[1]
                if status_item == "PENDING":
                    count_pending += 1
                elif status_item == "DELIVERING":
                    count_delivering += 1
                elif status_item == "CANCELLED":
                    count_cancelled += 1
                elif status_item == "COMPLETED":
                    count_completed += 1
            print(f"""===== THỐNG KÊ ĐƠN HÀNG =====
PENDING: {count_pending}
DELIVERING: {count_delivering}
CANCELLED: {count_cancelled}
COMPLETED: {count_completed}""")
            print()
        case 4:
            print("=== CHƯƠNG TRÌNH KẾT THÚC ===")
            break
        case _:
            print("Lựa chọn không hợp lệ")