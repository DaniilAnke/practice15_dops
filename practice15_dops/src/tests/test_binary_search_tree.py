import unittest

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        self.bst = BinarySearchTree()
        for i in range(10):
            self.bst.insert(i * 10, f'Value {i}')

    def test_insert_and_search(self):
        result = self.bst.search(50)
        self.assertEqual(result, 'Value 5')

    def test_delete(self):
        self.bst.delete(50)
        result = self.bst.search(50)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()