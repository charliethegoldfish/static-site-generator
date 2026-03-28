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