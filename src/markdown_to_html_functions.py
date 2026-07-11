import re
from parentnode import ParentNode
from block_functions import markdown_to_blocks, block_to_block_type, BlockType, block_type_to_html_tag
from extract_functions import extract_heading_level
from node_conversion_functions import text_to_code_html_node, text_to_textnodes, text_node_to_html_node
from config import ORD_LIST_REMOVE_REGEX, UNORD_LIST_REMOVE_REGEX

def list_block_to_html_nodes(block, ordered = False):
	block_items = block.splitlines()

	split_regex = ORD_LIST_REMOVE_REGEX if ordered else UNORD_LIST_REMOVE_REGEX

	nodes = []
	for item in block_items:
		# Split it so we have the markdown artifact, then the rest of the text
		split_item = re.split(split_regex, item, maxsplit=1)
		if (len(split_item)) > 0:
			text_item = split_item[1]
			child_nodes = text_to_children_nodes(text_item)
			list_node = ParentNode("li", child_nodes)
			nodes.append(list_node)
	return nodes

def paragraph_block_to_html_nodes(block):
	nodes = text_to_children_nodes(block, True)
	return nodes

def text_to_children_nodes(text, remove_newlines = False):
	if remove_newlines:
		text = text.replace('\n', ' ')

	nodes = []
	text_nodes = text_to_textnodes(text)

	for t_node in text_nodes:
		nodes.append(text_node_to_html_node(t_node))

	return nodes

def block_to_parent_html_node(block_type, block):
	heading_level = None
	if block_type == BlockType.HEADING:
		heading_level = extract_heading_level(block)
	html_tag = block_type_to_html_tag(block_type, heading_level)
	return ParentNode(html_tag, [])

def markdown_to_html_node(markdown):
	# Split into blocks
	blocks = markdown_to_blocks(markdown)

	block_nodes = []
	# loop over blocks
	for block in blocks:
		# for each block grab its type
		block_type = block_to_block_type(block)

		# create a htmlnode for its type
		block_node = block_to_parent_html_node(block_type, block)

		# create appropriate children nodes and assign
		# code block is a special case
		children_nodes = []

		match block_type:
			case BlockType.CODE:
				node = text_to_code_html_node(block)
				children_nodes.append(node)
			case BlockType.ORDERED_LIST:
				children_nodes = list_block_to_html_nodes(block, True)
			case BlockType.UNORDERED_LIST:
				children_nodes = list_block_to_html_nodes(block, False)
			case BlockType.QUOTE:
				pass
			case BlockType.PARAGRAPH:
				children_nodes = paragraph_block_to_html_nodes(block)
			case _:
				pass
		
		block_node.children = children_nodes
		
		block_nodes.append(block_node)
			

	# block nodes should be children of a single div html node
	return ParentNode("div", block_nodes)