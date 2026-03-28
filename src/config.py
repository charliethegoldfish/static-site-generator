IMAGE_REGEX = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
LINK_REGEX = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

SPLIT_IMAGE_REGEX = r"!\[[^\[\]]*\]\([^\(\)]*\)"
SPLIT_LINK_REGEX = r"(?<!!)\[[^\[\]]*\]\([^\(\)]*\)"

# Block type regex
HEADING_REGEX = r"#{1,6} .{1,}"
CODE_REGEX = r"`{3}\n(.*\n?){1,}`{3}"
QUOTE_REGEX = r"(> ?.*\n?){1,}"