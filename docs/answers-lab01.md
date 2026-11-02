# Trả lời câu hỏi thảo luận - Lab 01

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **Vị trí lưu trữ**:
  - Cấu hình `--global` được lưu trong tệp `~/.gitconfig` (hoặc `~/.config/git/config`) thuộc thư mục người dùng của hệ điều hành.
  - Cấu hình `--local` được lưu trong tệp `.git/config` nằm ngay trong thư mục kho lưu trữ (repository) cụ thể.
- **Sự khác biệt**:
  - Phạm vi áp dụng (Scope): `--global` có hiệu lực trên toàn bộ các repository của user hiện tại trên máy, trong khi `--local` chỉ áp dụng riêng cho repository đó.
  - Mức độ ưu tiên (Precedence): Thiết lập ở mức `--local` luôn ghi đè (ưu tiên cao hơn) cấu hình ở mức `--global`.

## 2. Vì sao dùng `git mv`?
- `git mv` thực hiện đồng thời hai thao tác: đổi tên/di chuyển tệp trên hệ thống tệp và đưa ngay trạng thái này vào Staging Area (`git add`).
- Giúp Git trực tiếp ghi nhận thao tác di chuyển/đổi tên (Rename 100%) thay vì hiểu lầm là xóa tệp cũ rồi tạo tệp mới hoàn toàn.
- Nhờ đó, Git dễ dàng theo dõi và bảo tồn trọn vẹn lịch sử commit của tệp xuyên suốt quá trình thay đổi cấu trúc thư mục (có thể kiểm tra bằng lệnh `git log --oneline --follow -- <path>`).

## 3. `release/lab01` có phải baseline?
- **Có**. Nhánh `release/lab01` (và commit tương ứng trên nhánh đó) đóng vai trò là một baseline (mốc cơ sở cấu hình).
- Đây là trạng thái mã nguồn và tài liệu đã được kiểm thử, nghiệm thu và thống nhất để giao nộp/phát hành. Sau khi được tạo, baseline này được đóng băng và mọi thay đổi sửa chữa sau đó bắt buộc phải tuân theo quy trình kiểm soát nghiêm ngặt (hotfix flow).

## 4. Vì sao không commit thẳng master dù làm một mình?
- **Duy trì tính toàn vẹn của nhánh chính (`master`)**: `master` luôn phải ở trạng thái "sạch", chạy tốt và sẵn sàng để phát hành bất kỳ lúc nào.
- **Tuân thủ quy trình Quản lý cấu hình (SCM)**: Mọi thay đổi đều phải gắn với một mục đích rõ ràng (qua nhánh riêng: refactor, feature, bugfix), có mã theo dõi độc lập và có thể rollback/hủy bỏ dễ dàng mà không ảnh hưởng nhánh chính.
- **Tập dượt quy trình chuẩn**: Tạo cơ hội tự kiểm tra lại thay đổi (self-review) qua giao diện Diff / Pull Request trước khi tích hợp vào nhánh chính, tạo thói quen làm việc chuyên nghiệp trong môi trường nhóm lớn sau này.
