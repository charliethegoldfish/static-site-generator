from copy_functions import copy_directory_contents
from generate_functions import generate_pages_recursive
from config import PUBLIC_PATH, STATIC_PATH, CONTENT_PATH, TEMPLATE_PATH

def main():
	copy_directory_contents(STATIC_PATH, PUBLIC_PATH)
	generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH, PUBLIC_PATH)


main()