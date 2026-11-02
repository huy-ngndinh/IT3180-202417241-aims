# Trả lời câu hỏi thảo luận - Lab 04

## 1. Vì sao chuẩn bị trên master trước, không sửa trên nhánh release?
- **Nguyên tắc "Single Source of Truth"**: Nhánh `master` đại diện cho dòng phát triển chính thống. Việc chuẩn bị phát hành (tăng phiên bản, cập nhật CHANGELOG, chạy kiểm thử tích hợp) trên `master` đảm bảo mọi thông tin phát hành đều có mặt trên dòng chính trước khi phân nhánh.
- **Tránh việc quên đồng bộ hoặc gây xung đột**: Nếu thực hiện thay đổi trên nhánh `release/*` rồi cố gắng merge ngược lại `master`, quy trình sẽ bị đảo chiều, dễ phát sinh xung đột không đáng có hoặc bỏ sót commit trên nhánh chính khi các nhánh tính năng khác tiếp tục được đưa vào `master`.

## 2. Vì sao `release/*` không bao giờ merge vào master? So sánh với GitFlow
- **Quy tắc của Release Flow**:
  - Nhánh `release/*` sau khi tạo ra chỉ dùng để nộp bài hoặc bảo trì bản phát hành (maintenance stream). Nếu phát hiện lỗi trên bản phát hành, ta tạo nhánh `hotfix/*`, sửa lỗi, rồi dùng lệnh `git cherry-pick -x` để chỉ mang đúng commit sửa lỗi về `master`.
  - Không bao giờ merge cả nhánh `release/*` vào `master` vì commit nâng số phiên bản của nhánh release (ví dụ `1.0.1`) sẽ xung đột hoặc ghi đè sai lệch lên số phiên bản mới đang phát triển trên `master` (ví dụ `1.1.0` hoặc `2.0.0`).
- **So sánh với GitFlow**:
  - Trong **GitFlow**, có 2 nhánh sống dài song song là `main` và `develop`. Nhánh `release` được tách từ `develop`, sau khi hoàn thiện phải merge kép vào cả `main` lẫn `develop`. Điều này khiến cấu trúc đồ thị commit của GitFlow phức tạp, nhiều nhánh sống dài, dễ dẫn đến "merge hell".
  - Trong **Release Flow**, chỉ có duy nhất một nhánh sống dài là `master`. Các nhánh `release/*` sống độc lập đóng băng từng phiên bản, các sửa chữa được lan truyền có chọn lọc bằng `cherry-pick`, giúp lịch sử Git trong sáng, trực quan và dễ quản lý hơn rất nhiều.

## 3. Vì sao lên 1.0.0 mà không phải 0.4.0?
- **Quy chuẩn Semantic Versioning (SemVer)**:
  - Các phiên bản `0.y.z` là giai đoạn sản phẩm sơ khai (Initial Development), API chưa ổn định và thường xuyên thay đổi kiến trúc.
  - Sau khi trải qua 3 bài thực hành ban đầu (Lab 01-03), hệ thống AIMS-mini đã hoàn thiện đầy đủ các chức năng nền tảng (quản lý giỏ hàng, in ấn, tìm kiếm, tính chiết khấu), có bộ unit test tự động đầy đủ, cấu trúc package chuẩn mực và tài liệu use case rõ ràng.
  - Do đó, việc nâng phiên bản lên **1.0.0** đánh dấu cột mốc phiên bản phát hành ổn định đầu tiên (First Stable Public Release), cam kết tính ổn định của API và quy chuẩn hoạt động với người dùng.
