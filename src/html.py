def style(file: str) -> str:
    with open(file + ".css", "r") as f:
        fread = f.read()
        f.close()
    return fread

def script(file: str) -> str:
    with open(file + ".js", "r") as f:
        fread = f.read()
        f.close()
    return fread

def extern(file: str) -> str:
    with open(file + ".html", "r") as f:
        fread = f.read()
        f.close()
    return fread

def div(id: str, content: str) -> str:
    return f"<div id={id}>{content}</div>"

def rawhtml(content: str) -> str:
    return content
