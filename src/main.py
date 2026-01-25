from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
    dummy_text_node = TextNode("Some anchor text", TextType.TEXT_LINK, "https://www.bootdev.com")
    print(dummy_text_node)

    # props = {}
    # props["href"] = "https://www.google.com"
    # props["target"] = "_blank"
    # dummy_html_node = HTMLNode("a", "something", None, props)
    # print(dummy_html_node)

main()