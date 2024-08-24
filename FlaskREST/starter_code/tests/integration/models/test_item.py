from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
    # here we access to db which going to load everything we need  from app context in order to access
      with self.app_context():
          item = ItemModel('test', 19.99)
    # before we save it to db, make sure that item is not exist
          self.assertIsNone(ItemModel.find_by_name('test'), f"Found an item with name {item.name}, but expected no to ")
          item.save_to_db()
          self.assertIsNone(ItemModel.find_by_name('test'))

          item.delete_from_db()

          self.assertIsNone(ItemModel.find_by_name('test'))



