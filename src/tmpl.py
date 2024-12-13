#!/usr/bin/python3

from string import Template
from sys import argv

def tmpl(file: str, title: str, html: str, style: str) -> str:
    with open(file, "r") as f:
        buf = f.read()
        f.close()
    strtmpl: any = Template(buf)
    res: str = strtmpl.substitute({
        "title" : title,
        "html" : html,
        "style" : style
    })
    return res
