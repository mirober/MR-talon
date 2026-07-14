from pathlib import Path
import re
from talon import ui, Module, Context, registry, actions, imgui, cron, resource
from typing import List, Optional, Dict

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def upper(s: str) -> str:
        """Uppercase"""
        return s.upper()

    def cat(l: List[str], sep: str = "") -> str:
        """Concatenate"""
        return sep.join(l)

    def first_letter_lowercase(s: str) -> str:
        """Return the first letter of the string, lowercased"""
        return "" if len(s) == 0 else s[0].lower()

    def replace(pat: str, rep: str, s: str) -> str:
        """Replace"""
        return re.sub(pat, rep, s)

    def slice(l: List[str], i1: Optional[int] = None, i2: Optional[int] = None) -> List[str]:
        """Slice"""
        if i1 is not None and i2 is None:
            return l[i1:]
        elif i1 is None and i2 is not None:
            return l[:i2]
        elif i1 is not None and i2 is not None:
            return l[i1:i2]
        else:
            return l


mod.list("extensions", desc="Common file extensions")
ctx.lists["user.extensions"] = {
    "markdown": "md",
    "PDF": "pdf",
    "jay peg": "jpg",
    "PNG": "png",
    "pie": "py",
    "rust": "rs",
    "sequel": "sql",
    "talon": "talon",
    "tech": "tex",
    "text": "txt",
}

#------------------------------------------------------

mod.list("alphabet", desc="Alphabet")

@mod.capture(rule="{user.alphabet}+")
def letters(m) -> str:
    "A series of letters"
    return "".join(m["alphabet_list"])

@mod.capture(rule="{user.alphabet}")
def letter(m) -> str:
    "A series of letters"
    return m["alphabet"]


mod.list("directions", desc="Directions")
ctx.lists["user.directions"] = {
    "lease": "left",
    "ross": "right",
    "sauce": "up",
    "dunce": "down",
}

mod.list("directions_extreme", desc="Directions extreme")
ctx.lists["user.directions_extreme"] = {
    "sauce": "ctrl-home",
    "lease": "home",
    "dunce": "ctrl-end",
    "ross": "end",
}

mod.list("direction_modifiers", desc="Direction modifiers")
ctx.lists["user.direction_modifiers"] = {
    "queue": "ctrl-shift-",
    "shin": "shift-",
    "fly": "ctrl-",
}

mod.list("capitalisation", desc="Capitalisation")
ctx.lists["user.capitalisation"] = {
    "yell": "1",
    "tie": "2",
    "camel": "3",
    "sing": "4",
    "laws": "5",
    "password": "6",
}
mod.list("spacing", desc="Spacings")
ctx.lists["user.spacing"] = {
    "gum": "1",
    "gun": "1",
    "spine": "2",
    "snake": "3",
    "pebble": "4",
}

punctuation = {
    "apostrophe": "'",
    "backslash": "\\",
    "backtick": "`",
    "caret": "^",
    "comma": ",",
    "coal gap": ": space",
    "boom": ", space",
    "boomer": ", space",
    "dollar": "$",
    "point": ".",
    "thin quotes": "'",
    "quote": '"',
    "quotes": '"',
    "hashtag": "#",
    "hyphen": "-",
    "semicolon": ";",
    "tilde": "~",
    "underscore": "_",
    "double equals": "space = = space",
    "angle": "< > left",
    "prekris": "( ) left",
    "prens": "( ) left",
    "brax": "[ ] left",
    "curly": "{ } left",
    "left paren": "(",
    "lenny": "(",
    "right paren": ")",
    "penny": ")",
    "left bracket": "[",
    "right bracket": "]",
    "left brace": "{",
    "right brace": "}",
}

punctuation_long = {
    "equals": "=",
    "ampersand": "&",
    "starling": "*",
    "at sign": "@",
    "pipe symbol": "|",
    "pipey": "|",
    "colon": ":",
    "clamor": "!",
    "minus": "-",
    "modulo": "%",
    "plus": "+",
    "questo": "?",
    "slash": "/",
    "greater than": ">",
    "greater equal": "> =",
    "less than": "<",
    "less equal": "< =",
}
mod.list("punctuation", desc="Punctuation")
ctx.lists["user.punctuation"] = {
    **punctuation,
    **punctuation_long
}

mod.list("punctuation_long", desc="Punctuation long")
ctx.lists["user.punctuation_long"] = punctuation_long
