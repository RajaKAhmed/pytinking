from flask import Flask, render_template
import os

template_folder = "C:\\Users\\rajaa\\OneDrive\\DataScience\\Python\\llm\\openaiui\\templates" 
index_filename = "index.html"

template_path = os.path.abspath(template_folder)
index_path = os.path.join(template_path, index_filename)

app= Flask(__name__)
@app.route('/')
def home():
    rendered_template = render_template(index_filename)
    return rendered_template

if __name__ == '__main__':
    app.run()