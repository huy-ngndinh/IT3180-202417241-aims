import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title, search_by_category


class TestSearch(unittest.TestCase):
    def test_search_by_title_found(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", cost=19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", cost=24.95),
            DigitalVideoDisc("Aladdin", "Animation", cost=18.99),
        ]
        results = search_by_title(items, "Star")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Star Wars")

    def test_search_by_title_case_insensitive(self):
        items = [
            DigitalVideoDisc("The Lion King", cost=19.95),
        ]
        results = search_by_title(items, "lion")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "The Lion King")

    def test_search_by_title_not_found(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", cost=19.95),
        ]
        results = search_by_title(items, "Avatar")
        self.assertEqual(len(results), 0)

    def test_search_by_category_found(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", cost=19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", cost=24.95),
            DigitalVideoDisc("Aladdin", "Animation", cost=18.99),
        ]
        results = search_by_category(items, "Animation")
        self.assertEqual(len(results), 2)

    def test_search_by_category_not_found(self):
        items = [
            DigitalVideoDisc("The Lion King", "Animation", cost=19.95),
        ]
        results = search_by_category(items, "Action")
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()
