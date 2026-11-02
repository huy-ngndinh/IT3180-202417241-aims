# Trả lời câu hỏi thảo luận - Lab 05

## 1. Ưu, nhược điểm của Upstream First so với Release First?
- **Release First (Mô hình áp dụng trong bài thực hành)**:
  - *Ưu điểm*: Tập trung sửa chữa và khắc phục sự cố trực tiếp trên phiên bản đang chạy trong thực tế (`release/*`), giúp phát hành bản vá PATCH (`v1.0.1`) nhanh chóng nhất đến tay người dùng cuối để giảm thiểu thiệt hại.
  - *Nhược điểm*: Đòi hỏi lập trình viên phải chủ động thực hiện lan truyền ngược (backport/cherry-pick) sang nhánh chính `master` và các phiên bản đang phát triển khác (`release/lab05`). Nếu quy trình kiểm soát lỏng lẻo và bỏ quên bước này, lỗi sẽ bị tái diễn (regression) ở các bản phát hành tương lai.
- **Upstream First (Khuyến nghị trong các dự án quy mô lớn, ví dụ Linux Kernel, Microsoft)**:
  - *Ưu điểm*: Sửa lỗi triệt để ngay trên dòng phát triển mới nhất (`master`), đảm bảo toàn bộ mã nguồn tương lai luôn sạch lỗi và tuân thủ kiến trúc mới nhất. Sau đó bản sửa lỗi mới được cherry-pick ngược về các nhánh bảo trì cũ.
  - *Nhược điểm*: Quy trình kiểm thử và review trên nhánh chính thường khắt khe và mất nhiều thời gian hơn, có thể làm chậm trễ thời gian phát hành bản vá khẩn cấp cho người dùng đang gặp sự cố.

## 2. Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?
- **Lệnh so sánh commit giữa các dòng phiên bản**:
  - `git cherry -v origin/release/lab05 origin/release/lab04`: Nếu có dấu `+` trước commit sửa lỗi nghĩa là nhánh `release/lab05` chưa có bản vá tương đương từ `release/lab04`.
  - `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"`: Nếu chỉ thấy 1 commit (trên master) thay vì 2 commit thì phát hiện ngay việc thiếu sót trên `release/lab05`.
- **Lệnh kiểm toán hành vi tự động bằng vòng lặp test**:
  ```bash
  for ref in v1.0.1 v1.1.0 master; do
    git switch --detach -q $ref; printf "%-8s " $ref
    python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; \
    print(len(search_by_title([D('The Lion King')], 'lion')))"
  done; git switch -q master
  ```
  Nếu quên lan truyền sang `release/lab05`, kết quả in ra sẽ là:
  ```
  v1.0.1   1
  v1.1.0   0   <-- Phát hiện lỗi ngay lập tức!
  master   1
  ```

## 3. Vì sao ở Phần A chưa gắn tag v1.1.0?
- Vì nhánh `release/lab05` tại Phần A mới chỉ là baseline sơ bộ, chưa trải qua quá trình kiểm toán toàn diện và nghiệm thu cuối cùng.
- Nếu đã gắn tag `v1.1.0` ngay từ đầu, theo quy tắc bất biến của Semantic Versioning ("Tag đã chia sẻ thì không xóa, không di chuyển"), sau khi nhận bản vá hotfix ta sẽ buộc phải nâng và phát hành phiên bản `v1.1.1`.
- Việc trì hoãn gắn tag cho đến khi tích hợp trọn vẹn bản vá giúp đảm bảo bản phát hành chính thức `v1.1.0` ra mắt hoàn chỉnh và sạch lỗi.
