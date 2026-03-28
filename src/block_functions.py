import re
from enum import Enum
from config import HEADING_REGEX, CODE_REGEX, QUOTE_REGEX

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    split_markdown = markdown.split("\n\n")
    blocks = []
    for split in split_markdown:
        block = split.strip()
        if block != "":
            blocks.append(block)
    return blocks

# Use re.fullmatch ??

def block_to_block_type(block):
    if re.fullmatch(HEADING_REGEX, block):
        return BlockType.HEADING
    elif re.fullmatch(CODE_REGEX, block):
        return BlockType.CODE
    elif re.fullmatch(QUOTE_REGEX, block):
        return BlockType.QUOTE
    else:
        return BlockType.PARAGRAPH
    