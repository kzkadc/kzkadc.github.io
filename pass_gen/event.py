from js import document

from pass_gen import pass_gen
from js_utils import copy_to_clipboard, display_message


def generate_pass(event):
    limited_characters = document.getElementById("limited_characters").checked
    p = pass_gen(document.getElementById("input").value,
                 limited_characters=limited_characters)
    document.getElementById("output").value = p

    copied = copy_to_clipboard(p)
    if copied:
        display_message("Copied!")
