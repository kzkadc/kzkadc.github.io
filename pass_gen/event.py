from js import document

from pass_gen import pass_gen

def generate_pass():
    p = document.getElementById("input").value
    document.getElementById("output").value = pass_gen(p)
