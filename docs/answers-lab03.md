# Trả lời câu hỏi thảo luận - Lab 03

## 1. Merge base là gì?
- **Định nghĩa**: Merge base là commit tổ tiên chung gần nhất (most recent common ancestor) giữa hai nhánh trong đồ thị có hướng không chu trình (DAG - Directed Acyclic Graph) của Git.
- **Vai trò**: Khi thực hiện hòa trộn (merge) hai nhánh (ví dụ nhánh A và nhánh B), Git sử dụng merge base làm điểm quy chiếu trong thuật toán 3-way merge:
  - So sánh `merge base` ➔ `nhánh A` (để tìm những gì nhánh A đã thay đổi).
  - So sánh `merge base` ➔ `nhánh B` (để tìm những gì nhánh B đã thay đổi).
  - Tự động kết hợp cả hai tập thay đổi. Nếu cả hai nhánh cùng sửa đổi cùng một dòng hoặc cùng một khối mã so với merge base, Git sẽ phát hiện xung đột (Merge Conflict).
- Lệnh kiểm tra merge base: `git merge-base branchA branchB`.

## 2. Vì sao master/release/* phải dùng revert?
- **Tính bất biến của lịch sử công khai**: Nhánh `master` và các nhánh phát hành `release/*` là các nhánh dùng chung, đại diện cho sản phẩm đang hoạt động hoặc chuẩn bị bàn giao. Lịch sử của các nhánh này đã được chia sẻ (push) tới tất cả các thành viên và hệ thống tự động (CI/CD).
- **Nguy cơ khi dùng Reset**: `git reset` viết lại lịch sử commit bằng cách xóa hoặc lùi con trỏ nhánh, đòi hỏi phải sử dụng force push (`git push --force`). Điều này bị chặn hoàn toàn bởi **Branch Protection Rules** và sẽ gây phá vỡ môi trường làm việc của mọi thành viên khác (khiến họ bị phân kỳ lịch sử và mất commit).
- **Lợi ích của Revert**: `git revert` không viết lại lịch sử quá khứ; thay vào đó, nó tạo ra một **commit mới** mang nội dung đảo ngược chính xác những thay đổi của commit cần hủy bỏ. Cách này an toàn tuyệt đối, duy trì trọn vẹn nhật ký kiểm toán (audit trail), tuân thủ nguyên tắc SCM và dễ dàng tích hợp qua quy trình Pull Request có kiểm duyệt.
