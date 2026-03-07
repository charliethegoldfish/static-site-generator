
def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    blocks = []
    for split in split_markdown:
        block = split.strip()
        if block != "":
            blocks.append(block)
    return blocks
