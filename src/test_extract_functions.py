import unittest

from extract_functions import extract_markdown_images, extract_markdown_links, extract_title

class TestExtractFunctions(unittest.TestCase):
	def test_extract_markdown_images(self):
		matches = extract_markdown_images(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
	
	def test_extract_markdown_link(self):
		matches = extract_markdown_links(
			"This is text with an [link](www.google.com)"
		)
		self.assertListEqual([("link", "www.google.com")], matches)

	def test_extract_markdown_link_from_image(self):
		matches = extract_markdown_links(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
		)
		self.assertListEqual([], matches)
	
	def test_extract_multiple_markdown_images(self):
		matches = extract_markdown_images(
			"This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
		)
		self.assertListEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

	def test_extract_multiple_markdown_links(self):
		text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
		matches = extract_markdown_links(text)
		self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
	
	def test_extract_title(self):
		title = extract_title("# Hello")
		self.assertEqual(title, "Hello")
	
	def test_extract_no_title(self):
		# title = extract_title("Hello")
		self.assertRaises(RuntimeError, extract_title, "Hello")

	def test_extract_title_more_text(self):
		md = """
# Hello

More text here!

## Another heading

"""
		title = extract_title(md)
		self.assertEqual(title, "Hello")