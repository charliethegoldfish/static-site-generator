IMAGE_REGEX = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
LINK_REGEX = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"

SPLIT_IMAGE_REGEX = r"!\[[^\[\]]*\]\([^\(\)]*\)"
SPLIT_LINK_REGEX = r"(?<!!)\[[^\[\]]*\]\([^\(\)]*\)"

# Block type regex
HEADING_REGEX = r"#{1,6} .{1,}"
CODE_REGEX = r"`{3}\n(.*\n?){1,}`{3}"
QUOTE_REGEX = r"(> ?.*\n?){1,}"
UNORDERED_LIST_REGEX = r"(- .*\n?){1,}"
ORDERED_LIST_REGEX = r"^(\d\. .*\n?){1,}"

ORD_LIST_NUM_REGEX = r"^\d(?=\.)"

HEADING_HASH_REGEX = r"^#{1,6}(?= )"
ORD_LIST_REMOVE_REGEX = r"(^\d\. )"
UNORD_LIST_REMOVE_REGEX = r"(^- )"