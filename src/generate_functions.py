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
	

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
	contents = os.listdir(dir_path_content)
	for content in contents:
		source_path = os.path.join(dir_path_content, content)
		
		if os.path.isfile(source_path):
			# Make sure we're a markdown file
			if content.endswith(".md"):
				stripped_name = content.strip(".md")
				new_name = stripped_name + ".html"
				dest_path = os.path.join(dest_dir_path, new_name)
				generate_page(source_path, template_path, dest_path)
		else:
			dest_path = os.path.join(dest_dir_path, content)
			generate_pages_recursive(source_path, template_path, dest_path)