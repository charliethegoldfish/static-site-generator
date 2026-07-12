import os
import shutil

def copy_directory_contents(source: str, destination: str):
	if not os.path.exists(source):
		raise RuntimeError("Source directory needs to exist to copy from")
	
	if os.path.exists(destination):
		shutil.rmtree(destination)
	
	os.mkdir(destination)

	contents = os.listdir(source)
	for content in contents:
		path = os.path.join(source, content)
		if os.path.isfile(path):
			shutil.copy(path, destination)
		else:
			copy_directory_contents(path, os.path.join(destination, content))
	