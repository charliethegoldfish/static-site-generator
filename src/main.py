import sys
from copy_functions import copy_directory_contents
from generate_functions import generate_pages_recursive
from config import BUILD_PATH, STATIC_PATH, CONTENT_PATH, TEMPLATE_PATH, TEST_PATH

def main():
	basepath = "/"
	exportPath = TEST_PATH
	if len(sys.argv) > 1:
		basepath = sys.argv[1]
		exportPath = BUILD_PATH

	
	copy_directory_contents(STATIC_PATH, exportPath)
	generate_pages_recursive(CONTENT_PATH, TEMPLATE_PATH, exportPath, basepath)


main()