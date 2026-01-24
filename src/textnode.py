from enum import Enum

class TextType(Enum):
    TEXT_PLAIN = "plain"
    TEXT_BOLD = "bold"
    TEXT_ITALIC = "italic"
    TEXT_CODE = "code"
    TEXT_LINK = "link"
    TEXT_IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        if not isinstance(text_type, TextType):
            raise Exception("text_type needs to be a member of TextType enum")
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            raise Exception("Can't compare objects of different types")
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"