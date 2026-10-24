(() => {
  function range(start, end) {
    return [...Array(end - start).keys()].map((i) => start + i);
  }

  async function hash(text) {
    // https://zenn.dev/phpbeginners/articles/bbcf45686aa129
    const algorithm = "SHA-256";
    const uint8 = new TextEncoder().encode(text);
    const digest = await crypto.subtle.digest(algorithm, uint8);
    const hashed = Array.from(new Uint8Array(digest))
      .map((v) => v.toString(16).padStart(2, "0"))
      .join("");
    return hashed;
  }

  function convert_base(x, limited_characters) {
    const CHARS = (() => {
      if (limited_characters) {
        return (
          "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" +
          "_-".repeat(5)
        );
      } else {
        const START = 33,
          END = 127;
        return range(START, END)
          .map((x) => String.fromCharCode(x))
          .join("");
      }
    })();
    const BASE = CHARS.length;

    const result = [];
    while (true) {
      let r = x % BASE;
      x = Math.floor(x / BASE);
      result.push(CHARS[r]);
      if (x == 0) {
        break;
      }
    }
    return result.toReversed().join("");
  }

  async function pass_gen(p, max_len, limited_characters) {
    const hs = await hash(p);
    const hs_int = parseInt(hs, 16);
    const converted_pass = convert_base(hs_int, limited_characters);
    return converted_pass.slice(0, max_len);
  }

  function copy_to_clipboard(text) {
    if (navigator.clipboard) {
      navigator.clipboard.writeText(text);
      return true;
    }

    return false;
  }

  function display_message(message) {
    document.getElementById("message").innerHTML = message;
  }

  async function generate_pass() {
    const MAX_LEN = 16;
    const limited_characters =
      document.getElementById("limited_characters").checked;
    const p = await pass_gen(
      document.getElementById("input").value,
      MAX_LEN,
      limited_characters,
    );
    document.getElementById("output").value = p;

    copied = copy_to_clipboard(p);
    if (copied) {
      display_message("Copied!");
    }
  }

  window.onload = () => {
    document.getElementById("gen_btn_js").onclick = generate_pass;
  };
})();
