def search_by_title(items, keyword):
    """Tìm kiếm các đĩa DVD có chứa từ khóa keyword trong tiêu đề."""
    return [dvd for dvd in items if keyword in dvd.title]
