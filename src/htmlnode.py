
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value

        if children != None and not isinstance(children, list):
            raise TypeError("children needs to be a list")

        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("HTMLNode base to_html not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        
        if not isinstance(self.props, dict):
            raise TypeError("props needs to be a dictionary")

        html = ""
        for key in self.props:
            html += f' {key}="{self.props[key]}"'
        return html
    
    def __repr__(self):
        formatted = f'HTMLNode:\nTag: {self.tag}\nValue: {self.value}\nChildren: '

        if self.children == None:
            formatted += f'{self.children}'
        else:
            for child in self.children:
                formatted += f'\n{child}'
        
        formatted += '\nProps: '
        if self.props == None:
            formatted += f'{self.props}'
        else:
            if not isinstance(self.props, dict):
                raise TypeError("props needs to be a dictionary")
            for key in self.props:
                formatted += f'\n"{key}": "{self.props[key]}"'
        return formatted


