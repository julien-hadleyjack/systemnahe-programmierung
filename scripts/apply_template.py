# -- coding: utf-8 --
#/usr/bin/env python3
"""
Usage:
    apply_template.py transform -o <output_dir>
    apply_template.py template -i <input_dir> -o <output_dir> (-t <template_file> <output_file>)...

Options:
    -i <input_dir>                      The directory with the markdown files
    -o <output_dir>                     The directory with the latex files
    -t <template_file> <output_file>    Transform the jinja2 template file and saves the output as the output_file
    -h, --help                          Show this screen and exit.
"""
import re

from jinja2 import Environment, FileSystemLoader
from docopt import docopt
import os
import sys
import textwrap

# Add parent directory to the path.
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(PARENT_DIR)
from metadata import *

SPACE_AFTER_FIRST_BRACKET_REG = re.compile(r"({ [\d\D]*?})")
SPACE_BEFORE_LAST_BRACKET_REG = re.compile(r"({[\d\D]*? })")
SPACE_AROUND_BRACKETS_REG = re.compile(r"({ [\d\D]*? })")


def generate_metadata(input_dir, output_dir):
    body = ""
    for file in os.listdir(output_dir):
        if file.endswith(".tex"):
            with open(os.path.join(output_dir, file), "r", encoding="utf-8") as tex_file:
                body += tex_file.read()

    return {
        "chapter_files": sorted(file[:-3] for file in os.listdir(input_dir) if file.endswith(".md") and file[0].isdigit()),
        "appendix_files": sorted(file[:-3] for file in os.listdir(input_dir) if file.endswith(".md") and file[0].isalpha()),
        "citations_found": "\\cite{" in body or "\\autocite{" in body,
        "code_block_found": "\\begin{minted}" in body,
        "code_found": "\\begin{minted}" in body or "\\mintinline" in body,
        "glossaries_found": "\\gls{" in body or "\\glspl{" in body or "\\glspl{" in body,
        "table_found": "\\begin{longtable}" in body,
        "page_layout": "top={0}, bottom={1}, left={2}, right={3}".format(top_margin, bot_margin, left_margin, right_margin)
    }


def process_chapter_files(output_dir):
    for file in os.listdir(output_dir):
        if file.endswith(".tex"):
            content = ""
            with open(os.path.join(output_dir, file), "r", encoding="utf-8") as tex_file:
                content = tex_file.read()
                content = apply_minted(content)
                #content = apply_longtable_caption(content)
            with open(os.path.join(output_dir, file), "w", encoding="utf-8") as tex_file:
                tex_file.write(content)

def process_tex_file(metadata, template_name):
    env = Environment(loader=FileSystemLoader("./templates"))
    template = env.get_template(template_name)
    templated_text = template.render(**dict(metadata, **globals()))

    return post_process_templated_text(templated_text)


def apply_minted(body):
    verbatim_regex = re.compile(r"(?s)(\\begin\{lstlisting\}\[)(.*?)(\])(.*?)(\\end\{lstlisting\})")

    for start, original_options, sep, content, end in verbatim_regex.findall(body):
        language_value = None
        caption_value = None

        options_split = original_options.split(", ")
        temp_option_split = []
        for option in options_split:
            if option.startswith("language"):
                language_value = option.split("=")[1]
                continue

            if option.startswith("caption"):
                caption_value = option.split("=")[1]
                continue

            temp_option_split.append(option)

        options_split = temp_option_split

        old_listing = "".join([start, original_options, sep, content, end])
        new_options = "[{}]".format(", ".join(options_split)) if options_split else ""
        minted_simple = """
        \\begin{{minted}}{options}{{{lang}}}
        {code}
        \\end{{minted}}
        """
        minted_output = textwrap.dedent(minted_simple).format(options=new_options, lang=language_value, code=content)

        if caption_value:
            minted_captioned = """
            \\begin{{listing}}[H]
            {minted}
            \\vspace{{-5pt}}
            \\caption{caption_short}{{{caption_text}}}
            \\end{{listing}}
            """
            caption_split = caption_value.split("\\autocite")
            if len(caption_split) == 2:
                caption_short = "[{}]".format(caption_split[0].strip())
            else:
                caption_short = ""
            minted_output = textwrap.dedent(minted_captioned).format(minted=minted_output, caption_text=caption_value, caption_short=caption_short)

        body = body.replace(old_listing, minted_output)

    inline_code_regex = re.compile(r"(\\lstinline!)(.*?)(!)")

    for start, content, end in inline_code_regex.findall(body):
        old_inline = "".join([start, content, end])
        new_inline = "\\mintinline{{text}}{{{content}}}".format(content=content)
        body = body.replace(old_inline, new_inline)

    return body

def apply_longtable_caption(body):
    verbatim_regex = re.compile(r"(?s)(?:\\begin\{longtable\}.*?\n)(\\caption\{)(.*?\})(\\tabularnewline)(.*?)(\\bottomrule)")

    for elements in verbatim_regex.findall(body):
        caption, caption_text, newline, content, bottomrule = elements

        caption_short = caption_text.split("\\autocite")
        if len(caption_short) == 2:
            caption = "\\caption[{}]{{".format(caption_short[0].strip())

        reordered_longtable = content, bottomrule, "\n", caption, caption_text, newline
        body = body.replace("".join(elements),"".join(reordered_longtable))

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
        process_chapter_files(arguments["-o"])
    
    if arguments["template"]:
        metadata = generate_metadata(arguments["-i"], arguments["-o"])

        for template, output in zip(arguments["-t"], arguments["<output_file>"]):            

            processed_tex_file = process_tex_file(metadata, template)

            with open(output, "w", encoding="utf-8") as output_file:
                output_file.write(processed_tex_file)