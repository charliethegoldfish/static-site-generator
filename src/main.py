from textnode import TextType, TextNode

def main():
    dummy_text_node = TextNode("Some anchor text", TextType.TEXT_LINK, "https://www.bootdev.com")
    print(dummy_text_node)

main()