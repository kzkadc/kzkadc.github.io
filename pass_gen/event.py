from pyscript import Element

from pass_gen import pass_gen

def generate_pass():
    Element("output").write(pass_gen(Element("input").value))
