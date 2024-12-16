import unittest
import change_text

class TestChangeText(unittest.TestCase):
  
  def test_uppercase(self):
    word = 'guitar'
    result = change_text.all_capitals(word)

    self.assertEqual(result, 'GUITAR')


if __name__ == '__main__':
  unittest.main()