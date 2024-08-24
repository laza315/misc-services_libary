from unittest import TestCase
from models.item import ItemModel


class TestModelItem(TestCase):
    def test_create_item(self):
        item = ItemModel('test', 50.99)

        self.assertEqual(item.name, 'test')
        self.assertEqual(item.price, 50.99)

    def test_create_json(self):
        item = ItemModel('test', 50.99)
        expected = {
            'name': 'test',
            'price': 50.99
        }
        self.assertEqual(item.json(), expected, "Received {}, expected {}".format(item.json(), expected))


