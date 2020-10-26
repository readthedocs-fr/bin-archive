#!/usr/bin/env python3

import hashlib
import pathlib
from bottle import (
    route, request, run, template, redirect, HTTPError, static_file
)

root = pathlib.Path(__file__).parent
html = root.joinpath('bin.html').read_text()
lang_aliases = {
    "py": "python",
    "js": "javascript",
    "md": "markdown",
    "cs": "csharp",
    "sh": "shell",
    "kts": "kotlin",
    "h": "objectivec",
    "hpp": "cpp",
    "rb": "ruby",
    "rs": "rust",
    "ts": "typescript",
    "yml": "yaml",
}

database = {}


@route("/assets/<filepath:path>")
def assets(filepath):
    return static_file(filepath, root=str(root.joinpath("assets")))


@route("/")
def newbin():
    return template(html, code=None)


@route("/", method="POST")
def paste():
    code = request.forms.get("code")
    hexhash = hashlib.md5(code.encode()).hexdigest()[:8]
    database[hexhash] = code
    return redirect(f"/{hexhash}")


@route("/<hexhash>")
def bin(hexhash, lang=None):
    hexhash, _, ext = hexhash.partition(".")
    lang = (request.query.get('lang') or ext).lower()
    lang = lang_aliases.get(lang, lang) or "plaintext"
    code = database.get(hexhash, "").encode("latin-1").decode("utf-8")
    if not code:
        raise HTTPError(status=404)
    return template(html, code=code, lang=lang)


run(host='localhost', port=8080)
