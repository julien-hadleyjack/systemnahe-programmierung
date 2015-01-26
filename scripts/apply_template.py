# -- coding: utf-8 --
# { %raw% }
"""
Usage:
    apply_template.py transform -i <input_dir>
    apply_template.py template -i <input_dir> (-t <template_file> <output_file>)...

Options:
    -i <input_dir> The directory with the latex files
    -t <template_file> <output_file>      transform the jinja2 template file and saves the output as the output_file
    -h, --help      Show this screen and exit.
"""
import re

from jinja2 import Environment, FileSystemLoader
from docopt import docopt
import os
import sys

# Add parent directory to the path.
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(PARENT_DIR)
from metadata import *

SPACE_AFTER_FIRST_BRACKET_REG = re.compile(r"({ [\d\D]*?})")
SPACE_BEFORE_LAST_BRACKET_REG = re.compile(r"({[\d\D]*? })")
SPACE_AROUND_BRACKETS_REG = re.compile(r"({ [\d\D]*? })")


def generate_metadata(input_dir):
    body = ""
    for file in os.listdir(input_dir):
        if file.endswith(".tex"):
            with open(os.path.join(input_dir, file), "r") as tex_file:
                body += tex_file.read()

    return {
        "files": [file[:-4] for file in os.listdir(input_dir) if file.endswith(".tex")],
        "citations_found": r"\cite{" in body,
        "code_blocks_found": r"\begin{minted}" in body,
        "page_layout": "top={0}, bottom={1}, left={2}, right={3}".format(top_margin, bot_margin, left_margin, right_margin)

    }


def process_chapter_files(input_dir):
    for file in os.listdir(input_dir):
        if file.endswith(".tex"):
            content = ""
            with open(os.path.join(input_dir, file), "r") as tex_file:
                #content = apply_minted(tex_file.read())
                content = apply_minted(tex_file.read())
            with open(os.path.join(input_dir, file), "w", encoding="utf-8") as tex_file:
                tex_file.write(content)

def process_tex_file(metadata, template_name):
    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template(template_name)
    templated_text = template.render(**dict(metadata, **globals()))

    return post_process_templated_text(templated_text)


def apply_minted(body):
    verbatim_regex = re.compile(r"(?s)(\\begin{verbatim}.*?\\end{verbatim})")

    # Finds the language and the code separatedly from a verbatim block.
    # More specifically: looks for '#!language\ncode' inside a verbatim block.
    language_hashtag_regex = re.compile(r"\\begin{verbatim}\n\#\!([\d\D]*?)\n([\d\D]*)\\end{verbatim}")

    search = verbatim_regex.findall(body)
    if search:
        for verbatim in search:
            code_search = language_hashtag_regex.findall(verbatim)
            if code_search:
                lang, code = code_search[0]
                latex_code = "\\begin{{minted}}{{lang}}\n{code}\\end{{minted}}".format(code=code)
                latex_code = latex_code.replace("{lang}", "{" + lang + "}")
                body = body.replace(verbatim, latex_code)

    return body


def post_process_templated_text(templated_text):
    return remove_spaces_around_brackets(templated_text)


def remove_spaces_around_brackets(text):
    text = remove_spaces_at_positions(text, SPACE_AFTER_FIRST_BRACKET_REG, [1])
    text = remove_spaces_at_positions(text, SPACE_BEFORE_LAST_BRACKET_REG, [-2])
    text = remove_spaces_at_positions(text, SPACE_AROUND_BRACKETS_REG, [1, -2])
    return text


def remove_spaces_at_positions(text, regex, positions):
    for group in regex.findall(text):
        new_group = group
        for displacement, position in enumerate(positions):
            new_group = new_group[:position] + new_group[position + 1:]
        text = text.replace(group, new_group)
    return text


if __name__ == "__main__":
    arguments = docopt(__doc__)

    if arguments["transform"]:
        process_chapter_files(arguments["-i"])
    
    if arguments["template"]:
        metadata = generate_metadata(arguments["-i"])

        for template, output in zip(arguments["-t"], arguments["<output_file>"]):            

            processed_tex_file = process_tex_file(metadata, template)

            with open(output, "w", encoding="utf-8") as output_file:
                output_file.write(processed_tex_file)


# { %endraw% }