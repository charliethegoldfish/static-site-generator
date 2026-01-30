import unittest

from textnode import TextNode, TextType
from split_node_functions import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_code_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertIsInstance(new_nodes[0], TextNode)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
    
    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertIsInstance(new_nodes[0], TextNode)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_italic_delimiter(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertIsInstance(new_nodes[0], TextNode)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_multiple_passes(self):
        node = TextNode("This is text with a _italic_ word and a **bold** word", TextType.TEXT)
        bold_split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        final_split_nodes = split_nodes_delimiter(bold_split_nodes, "_", TextType.ITALIC)
        self.assertEqual(len(final_split_nodes), 5)
        self.assertEqual(final_split_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(final_split_nodes[1].text_type, TextType.ITALIC)
        # self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(final_split_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(final_split_nodes[3].text_type, TextType.BOLD)
        self.assertEqual(final_split_nodes[4].text_type, TextType.TEXT)


if __name__ == "__main__":
    unittest.main()