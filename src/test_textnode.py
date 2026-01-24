import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT_BOLD)
        self.assertEqual(node, node2)

    def test_type_different(self):
        node = TextNode("This is a text node", TextType.TEXT_BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT_CODE)
        self.assertNotEqual(node, node2)
    
    def test_url_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT_LINK, "boot.dev")
        node2 = TextNode("This is a text node", TextType.TEXT_LINK)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()