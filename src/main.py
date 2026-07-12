from copy_functions import copy_directory_contents
from config import PUBLIC_PATH, STATIC_PATH

def main():
	copy_directory_contents(STATIC_PATH, PUBLIC_PATH)


main()