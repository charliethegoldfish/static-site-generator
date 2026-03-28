import re
from enum import Enum
from config import HEADING_REGEX, CODE_REGEX, QUOTE_REGEX, UNORDERED_LIST_REGEX, ORDERED_LIST_REGEX, ORD_LIST_NUM_REGEX

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

# Checks to see if a list that has matched the ordered list pattern has numbers correctly incrementing
def is_list_ordered(block):
    # Extract the numbers
    matches = re.findall(ORD_LIST_NUM_REGEX, block, re.MULTILINE)

    # If we couldn't extract any numbers to check, it isn't a  valid ordered list
    if len(matches) < 1:
        return False

    # Check it starts at 1 and increments
    index = 1
    for match in matches:
        if int(match) == index:
            index += 1
        else:
            return False
    
    return True

def block_to_block_type(block):
    if re.fullmatch(HEADING_REGEX, block):
        return BlockType.HEADING
    elif re.fullmatch(CODE_REGEX, block):
        return BlockType.CODE
    elif re.fullmatch(QUOTE_REGEX, block):
        return BlockType.QUOTE
    elif re.fullmatch(UNORDERED_LIST_REGEX, block):
        return BlockType.UNORDERED_LIST
    elif re.fullmatch(ORDERED_LIST_REGEX, block) and is_list_ordered( block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    