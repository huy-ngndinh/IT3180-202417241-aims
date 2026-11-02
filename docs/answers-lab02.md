# Trả lời câu hỏi thảo luận - Lab 02

## 1. Vì sao phải đồng bộ master trước khi PR?
- **Phát hiện và giảm thiểu rủi ro xung đột (Conflict)**: Khi phát triển song song, `master` có thể đã tích hợp các commit mới từ các thành viên khác. Việc kéo `master` mới nhất về merge/rebase vào nhánh tính năng ở local giúp phát hiện và giải quyết xung đột ngay tại máy của lập trình viên trước khi tạo PR lên remote.
- **Đảm bảo tính tương thích và kiểm thử toàn diện**: Giúp kiểm tra xem tính năng mới có hoạt động ăn khớp với mã nguồn mới nhất trên dòng chính hay không, tránh tình trạng "code chạy tốt trên nhánh của tôi nhưng gộp vào master thì lỗi".
- **Giữ cho quá trình review PR diễn ra trôi chảy**: PR không bị rơi vào trạng thái "This branch has conflicts that must be resolved" trên giao diện GitHub.

## 2. Khi nào không được rebase?
- **Quy tắc vàng của Git Rebase**: *Không bao giờ rebase trên các nhánh công khai (public branch) hoặc nhánh dùng chung đã được chia sẻ với các thành viên khác (ví dụ: `master`, `main`, `release/*`)*.
- **Lý do**: Rebase làm thay đổi lịch sử commit (viết lại commit hash). Nếu các thành viên khác đang làm việc dựa trên các commit cũ của nhánh công khai đó, việc rebase và force push sẽ làm đứt gãy lịch sử, gây phân kỳ (diverged history) và xung đột trầm trọng cho toàn bộ đội ngũ phát triển.

## 3. `feature/*` khác `topic/*` ra sao?
- **Nhánh `feature/*` (Feature branch)**:
  - Dành riêng cho việc phát triển các chức năng nghiệp vụ phần mềm trực tiếp phục vụ người dùng cuối (User-facing / Business features), ví dụ: thêm giỏ hàng, tìm kiếm sản phẩm, áp mã giảm giá,...
  - Thường gắn liền với một User Story hoặc yêu cầu chức năng cụ thể trong Sprint.
- **Nhánh `topic/*` (Topic branch)**:
  - Dành cho các chủ đề kỹ thuật ngắn hạn, thử nghiệm ý tưởng (Spike / PoC), cấu hình hạ tầng, quy trình CI/CD hoặc bổ sung tài liệu dự án (ví dụ: thêm pull request template, bổ sung tài liệu use-case, cấu hình linting,...).
  - Cả hai đều tuân thủ quy tắc nhánh sống ngắn trong Release Flow, nhưng `topic/*` nhấn mạnh vào công việc kỹ thuật/tài liệu hỗ trợ hơn là tính năng nghiệp vụ.
