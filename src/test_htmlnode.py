import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_none(self):
        node = HTMLNode("a", "something here", None, None)
        propHTML = node.props_to_html()
        self.assertEqual(propHTML, "")

    def test_props_to_html_empty(self):
        node = HTMLNode("a", "something here", None, {})
        propHTML = node.props_to_html()
        self.assertEqual(propHTML, "")

    def test_props_to_html_one(self):
        props = {}
        props["href"] = "https://www.google.com"
        node = HTMLNode("a", "something here", None, props)
        propHTML = node.props_to_html()
        success = ' href="https://www.google.com"'
        self.assertEqual(propHTML, success)
    
    def test_props_to_html_two(self):
        props = {}
        props["href"] = "https://www.google.com"
        props["target"] = "_blank"
        node = HTMLNode("a", "something here", None, props)
        propHTML = node.props_to_html()
        success = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(propHTML, success)

if __name__ == "__main__":
    unittest.main()