from js import document, navigator


def copy_to_clipboard(val: str) -> bool:
    if navigator.clipboard:
        navigator.clipboard.writeText(val)
        return True

    return False


def display_message(m: str):
    document.body.getElementById("message").innerHTML = m
