import re
from config import IMAGE_REGEX, LINK_REGEX, HEADING_HASH_REGEX, TITLE_REGEX

# Regex for this
# !\[([^\[\]]*)\]\(([^\(\)]*)\)
def extract_markdown_images(text):
    matches = re.findall(IMAGE_REGEX, text)
    # print(matches)
    return matches

# Regex for this with a negative lookbehind
# (?<!\!)\[(.*?)\]\((.*?)\)
def extract_markdown_links(text):
    matches = re.findall(LINK_REGEX, text)
    return matches

def extract_heading_level(block):
    matches = re.findall(HEADING_HASH_REGEX, block)
    if len(matches) > 0:
        return len(matches[0])
    return 0

def extract_title(markdown):
    matches = re.findall(TITLE_REGEX, markdown)
    if len(matches) == 0:
        raise RuntimeError("No h1 header found for the title")
    title = matches[0].lstrip("#")
    title = title.strip()
    return title