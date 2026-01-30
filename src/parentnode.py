from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parentnode requires a tag!")
        if self.children == None:
            raise ValueError("ParentNode requires children!")
        if not isinstance(self.children, list):
            raise TypeError("ParentNode children should be a list!")
        
        html_inside = ""
        for child in self.children:
            if not isinstance(child, (HTMLNode, LeafNode, ParentNode)):
                raise TypeError("ParentNode children should be a subclass of HTMLNode")
            html_inside += child.to_html()
        
        return f'<{self.tag}{self.props_to_html()}>{html_inside}</{self.tag}>'
