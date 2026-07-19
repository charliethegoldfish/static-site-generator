import sys
from copy_functions import copy_directory_contents
from generate_functions import generate_pages_recursive
from config import BUILD_PATH, STATIC_PATH, CONTENT_PATH, TEMPLATE_PATH

def main():
	basepath = "/"
	if len(sys.argv) > 1:
		basepath = sys.argv[1]

	
	copy_directory_contents(STATIC_PATH, BUILD_PATH)
	generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH, BUILD_PATH, basepath)


main()