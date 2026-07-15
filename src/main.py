from copy_functions import copy_directory_contents
from generate_functions import generate_page
from config import PUBLIC_PATH, STATIC_PATH

def main():
	copy_directory_contents(STATIC_PATH, PUBLIC_PATH)
	generate_page("content/index.md", "template.html", "public/index.html")


main()