from tmpl import *
import html

gst: str = ""
glc: str = ""

def ghtml(content: str):
    glc += content

def style(file: str):
    gst = html.style(file)

def script(file: str):
    return html.script(file)

def extern(file: str):
    return html.extern(file)

def div(id: str, content: str):
    return html.div(id, content)

def rawhtml(content: str):
    return = html.rawhtml(content)

def compile(file: str) -> None:
    content = tmpl("../base.html", file, glc, gst)
    with open(file + ".html", "w+") as f:
        f.write(content)
        f.close()
