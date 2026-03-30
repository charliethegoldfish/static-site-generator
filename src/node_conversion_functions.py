from textnode import TextNode, TextType
from leafnode import LeafNode
from split_node_functions import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_image([node])
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("text_node needs to be a TextNode type")
    
    match text_node.text_type:
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            props = {}
            props["href"] = text_node.url
            return LeafNode("a", text_node.text, props)
        case TextType.IMAGE:
            props = {}
            props["src"] = text_node.url
            props["alt"] = text_node.text
            return LeafNode("img", "", props)
        case _:
            raise Exception(f"{text_node.text_type} not supported")
        
def text_to_code_html_node(text):
    # NOTE: If we allow levels of code backticks, this will fall down
    node = TextNode(text.strip('`').lstrip(), TextType.CODE)
    return text_node_to_html_node(node)