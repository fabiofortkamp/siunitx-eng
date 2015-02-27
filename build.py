#!/usr/bin/env python
#encoding=utf-8

import os, sys, csv
import pathlib
import jinja2

def wrapper(*args):
    """CLI wrapper"""
    opts = [i for i in args]
    cmd = [] + opts
    process = Popen(cmd, stdout=PIPE)
    process.communicate()[0]
    return process

if __name__ == '__main__':
    # change the default delimiters used by Jinja
    # (prevent JinJa from interferring with LaTeX macros)
    dtx_renderer = jinja2.Environment(
      block_start_string = '((*',
        block_end_string = '*))',
      variable_start_string = '(((',
        variable_end_string = ')))',
        comment_start_string = '((=',
        comment_end_string = '=))',
        loader = jinja2.FileSystemLoader('templates'))

    template = dtx_renderer.get_template('siunitx-eng-template.dtx')

    curdir = pathlib.Path('.')
    tabledir = curdir / 'tables'

    non_si_file = tabledir / 'non-si.txt'

    output_file = curdir / 'output.dtx'

    
    with non_si_file.open() as infile:
        reader = csv.DictReader(infile,fieldnames=['name','definition'])

        non_si_macros = []
        for row in reader:
           non_si_macros.append(row)
