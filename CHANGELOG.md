# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-11-02
### Fixed
- Sửa lỗi `search_by_title` không phân biệt hoa thường (case-insensitive) (#17).

## [1.0.0] - 2026-11-02
### Added
- `Cart.print_cart()`: In danh sách chi tiết các đĩa và tổng chi phí trong giỏ hàng.
- `search_by_title()`: Tìm kiếm đĩa DVD theo tiêu đề từ khóa.
- `Cart.total_cost_with_discount()`: Tính tổng chi phí giỏ hàng sau khi áp dụng chiết khấu.
- Bộ 4 bài unit test tự động cho `Cart` và `Search`.
- Tài liệu mô tả và sơ đồ Use Case (`docs/use-case.md`).
- Mẫu mô tả Pull Request (`.github/pull_request_template.md`).

### Fixed
- Sửa lỗi giỏ hàng chấp nhận đĩa thứ 21 vượt quá giới hạn 20 đĩa (#6).
- Sửa công thức tính chiết khấu và kiểm tra điều kiện phần trăm hợp lệ.
