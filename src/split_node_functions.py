from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if not isinstance(old_nodes, list):
        raise TypeError("old_nodes needs to be a list!")
    
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            raise TypeError("nodes in old_nodes need to be TextNode's")
        if node.text_type != TextType.TEXT:
            # We only split text nodes for now
            new_nodes.append(node)
            continue

        # Make sure that any delimiters found have a closing one
        num_appearances = node.text.count(delimiter)
        if num_appearances == 0:
            new_nodes.append(node)
            continue
        if num_appearances % 2 != 0:
            raise Exception(f'Node: "{node}", requires closing delimiter: "{delimiter}" to be valid markdown')

        split_nodes = []
        split_text = node.text.split(delimiter)
        for i in range(len(split_text)):
            new_node = None
            # Even indices are the text type, and odd are the new type
            if i % 2 == 0:
                new_node = TextNode(split_text[i], TextType.TEXT)
            else:
                new_node = TextNode(split_text[i], text_type)
            split_nodes.append(new_node)
        
        new_nodes.extend(split_nodes)
    
    return new_nodes





        
