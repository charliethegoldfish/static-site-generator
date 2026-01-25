from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes must have a value!")
        if self.tag == None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        formatted = f'LeafNode:\nTag: {self.tag}\nValue: {self.value}'
        
        formatted += '\nProps: '
        if self.props == None:
            formatted += f'{self.props}'
        else:
            if not isinstance(self.props, dict):
                raise TypeError("props needs to be a dictionary")
            for key in self.props:
                formatted += f'\n"{key}": "{self.props[key]}"'
        return formatted