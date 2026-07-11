import unittest

from markdown_to_html_functions import markdown_to_html_node

class TestMarkdownToHTML(unittest.TestCase):
	def test_codeblock(self):
		md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

		node = markdown_to_html_node(md)
		html = node.to_html()
		self.assertEqual(
			html,
			"<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
		)

	def test_unordered_list(self):
		md = """
- A list element
- Another with **bold**
- How about `code`
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		success = "<div><ul><li>A list element</li><li>Another with <b>bold</b></li><li>How about <code>code</code></li></ul></div>"

	def test_ordered_list(self):
		md = """
1. A list element
2. Another with **bold**
3. How about `code`
"""
		node = markdown_to_html_node(md)
		html = node.to_html()
		success = "<div><ol><li>A list element</li><li>Another with <b>bold</b></li><li>How about <code>code</code></li></ol></div>"