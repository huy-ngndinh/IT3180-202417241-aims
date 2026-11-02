import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title_found(self):
        items = [
            DigitalVideoDisc("The Lion King", cost=19.95),
            DigitalVideoDisc("Star Wars", cost=24.95),
            DigitalVideoDisc("Aladdin", cost=18.99),
        ]
        results = search_by_title(items, "Star")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Star Wars")

    def test_search_by_title_not_found(self):
        items = [
            DigitalVideoDisc("The Lion King", cost=19.95),
        ]
        results = search_by_title(items, "Avatar")
        self.assertEqual(len(results), 0)


if __name__ == "__main__":
    unittest.main()
