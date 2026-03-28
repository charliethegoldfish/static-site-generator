import unittest

from block_functions import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
	def test_heading_block_type(self):
		block_type = block_to_block_type("# Heading here")
		self.assertEqual(BlockType.HEADING, block_type)
	
	def test_not_heading_block_type(self):
		block_type = block_to_block_type("#NotHeading here")
		self.assertNotEqual(BlockType.HEADING, block_type)
	
	def test_too_many_heading_hashes(self):
		block_type = block_to_block_type("####### Also not Heading here")
		self.assertNotEqual(BlockType.HEADING, block_type)

	def test_code_block_type(self):
		block = "```\ncode here\n```"
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