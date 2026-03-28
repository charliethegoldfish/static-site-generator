import unittest

from block_functions import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
	# Heading Blocks
	def test_heading_block_type(self):
		block_type = block_to_block_type("# Heading here")
		self.assertEqual(BlockType.HEADING, block_type)
	
	def test_not_heading_block_type(self):
		block_type = block_to_block_type("#NotHeading here")
		self.assertNotEqual(BlockType.HEADING, block_type)
	
	def test_too_many_heading_hashes(self):
		block_type = block_to_block_type("####### Also not Heading here")
		self.assertNotEqual(BlockType.HEADING, block_type)

	# Code Blocks
	def test_code_block_type(self):
		block = "```\ncode here\n```"
		block_type = block_to_block_type(block)
		self.assertEqual(BlockType.CODE, block_type)

	def test_code_block_multi_lines(self):
		block = "```\ncode here\nmore code here\n```"
		block_type = block_to_block_type(block)
		self.assertEqual(BlockType.CODE, block_type)

	def test_not_code_block_type(self):
		block = "```code```"
		block_type = block_to_block_type(block)
		self.assertNotEqual(BlockType.CODE, block_type)

	def test_code_block_no_content(self):
		block = "```\n```"
		block_type = block_to_block_type(block)
		self.assertEqual(BlockType.CODE, block_type)

	# Quote Blocks
	def test_quote_block_type(self):
		block = "> quote start\n>quote continue"
		block_type = block_to_block_type(block)
		self.assertEqual(BlockType.QUOTE, block_type)

	def test_not_quote_block_type(self):
		block = "> quote start\nquote not continue\n>quote again"
		block_type = block_to_block_type(block)
		self.assertNotEqual(BlockType.QUOTE, block_type)
	
	# Unordered List Blocks
	def test_unordered_list_block_type(self):
		block = "- list item\n- another list item"
		block_type = block_to_block_type(block)
		self.assertEqual(BlockType.UNORDERED_LIST, block_type)
	
	def test_invalid_unordered_list_block_type(self):
		block = "- list item\n-an invalid list item"
		block_type = block_to_block_type(block)
		self.assertNotEqual(BlockType.UNORDERED_LIST, block_type)
	
	# Ordered List Blocks
	def test_ordered_list_block_type(self):
		block = "1. list\n2. more list\n3. listy list"
		block_type = block_to_block_type(block)
		self.assertEqual(BlockType.ORDERED_LIST, block_type)
	
	def test_not_ordered_list_block_type(self):
		block = "1. list\n3. more list\n4. listy list"
		block_type = block_to_block_type(block)
		self.assertNotEqual(BlockType.ORDERED_LIST, block_type)

	def test_ordered_list_wrong_start_block_type(self):
		block = "0. list\n1. more list\n2. listy list"
		block_type = block_to_block_type(block)
		self.assertNotEqual(BlockType.ORDERED_LIST, block_type)
	
	# Paragraph Blocks
	def test_paragraph_block_type(self):
		block = "literally a paragraph aye"
		block_type = block_to_block_type(block)
		self.assertEqual(BlockType.PARAGRAPH, block_type)