import re
from textnode import TextType, TextNode
from htmlnode import HTMLNode
from config import SPLIT_IMAGE_REGEX, SPLIT_LINK_REGEX

def main():
    # dummy_text_node = TextNode("Some anchor text", TextType.TEXT_LINK, "https://www.bootdev.com")
    # print(dummy_text_node)

    split_text_list = re.split(SPLIT_IMAGE_REGEX, "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)")
    print(split_text_list)

    split_link_list = re.split(SPLIT_LINK_REGEX, "This is text with an [image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)")
    print(split_link_list)

    # props = {}
    # props["href"] = "https://www.google.com"
    # props["target"] = "_blank"
    # dummy_html_node = HTMLNode("a", "something", None, props)
    # print(dummy_html_node)

main()