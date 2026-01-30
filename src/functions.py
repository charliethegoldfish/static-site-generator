from textnode import TextNode, TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if not isinstance(text_node, TextNode):
        raise TypeError("text_node needs to be a TextNode type")
    
    match text_node.text_type:
        case TextType.TEXT_BOLD:
            return LeafNode("b", text_node.text)
        case TextType.TEXT_PLAIN:
            return LeafNode(None, text_node.text)
        case TextType.TEXT_ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.TEXT_CODE:
            return LeafNode("code", text_node.text)
        case TextType.TEXT_LINK:
            props = {}
            props["href"] = text_node.url
            return LeafNode("a", text_node.text, props)
        case TextType.TEXT_IMAGE:
            props = {}
            props["src"] = text_node.url
            props["alt"] = text_node.text
            return LeafNode("img", "", props)
        case _:
            raise Exception(f"{text_node.text_type} not supported")