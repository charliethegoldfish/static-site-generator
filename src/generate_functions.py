import os
from markdown_to_html_functions import markdown_to_html_node
from extract_functions import extract_title

def generate_page(from_path, template_path, dest_path):
	print(f"Generating page from {from_path} to {dest_path} using {template_path}")

	md = ""
	with open(from_path, 'r') as f:
		md = f.read()
	
	template = ""
	with open(template_path, 'r') as f:
		template = f.read()
	
	title = extract_title(md)
	htmlNode = markdown_to_html_node(md)
	htmlContent = htmlNode.to_html()

	template = template.replace("{{ Title }}", title)
	template = template.replace("{{ Content }}", htmlContent)

	dir_name = os.path.dirname(dest_path)
	os.makedirs(dir_name, exist_ok=True)

	with open(dest_path, 'x') as f:
		f.write(template)
	


