import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        success = "<p>Hello, world!</p>"
        self.assertEqual(node.to_html(), success)
    
    def test_leaf_to_html_a(self):
        props = {}
        props["href"] = "https://www.google.com"
        node = LeafNode("a", "Click me!", props)
        success = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), success)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "just text here")
        success = "just text here"
        self.assertEqual(node.to_html(), success)
    
    # TODO: Need to test img tags? But first we need to support self closing ones

if __name__ == "__main__":
    unittest.main()