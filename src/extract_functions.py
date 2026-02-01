import re

# Regex for this
# !\[([^\[\]]*)\]\(([^\(\)]*)\)
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    # print(matches)
    return matches

# Regex for this with a negative lookbehind
# (?<!\!)\[(.*?)\]\((.*?)\)
def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches
