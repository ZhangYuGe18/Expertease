from jinja2 import Environment, FileSystemLoader
import json


with open('.\config\config.json', 'r', encoding='utf-8') as file:
    items = json.load(file)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')


rendered_html = template.render(items=items)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(rendered_html)

print("HTML file generated successfully!")
