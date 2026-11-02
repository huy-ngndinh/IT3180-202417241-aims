def search_by_category(items, category):
    """Tìm kiếm các đĩa DVD thuộc danh mục category."""
    return [dvd for dvd in items if category.lower() in dvd.category.lower()]


def search_by_title(items, keyword):
    """Tìm kiếm các đĩa DVD có chứa từ khóa keyword trong tiêu đề."""
    return [dvd for dvd in items if keyword in dvd.title]
