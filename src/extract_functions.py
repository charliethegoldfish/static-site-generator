import re
from config import IMAGE_REGEX, LINK_REGEX

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
