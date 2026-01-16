from talon import ui, Module, Context, registry, actions, imgui, cron

mod = Module()
ctx = Context("JS")
ctx.matches = r"""
title: /.*\.jsx?$/
title: /.*\.tsx?$/
"""

mod.list("javascript_types")

@ctx.action_class("user")
class Actions:
    def lang_print(s: str):
        actions.insert(f'console.log({s});')


ctx.lists["user.functions"] = {
    "add event listener": "addEventListener",
    "add event listener click": 'addEventListener("click", (event) => {[|]})',
    "class list add": "classList.add",
    "create element": "createElement",
    "for each": "forEach((element) => {[|]})",
    "get element by I D": "getElementById",
    "get elements by tag": "getElementsByTagName",
    "get elements by tag name": "getElementsByTagName",
    "get elements by class": "getElementsByClassName",
    "get elements by class name": "getElementsByClassName",
    "has attribute": "hasAttribute",
    "print": "console.log",
    "query selector": "querySelector",
    "query selector all": "querySelectorAll",
    "map": "map",
    "forEach": "forEach",
    "is array": "Array.isArray",
}

ctx.lists["user.logicals"] = {
    "and": " && ",
    "or": " || ",
    "as": " as ",
    "not equal": " !== ",
    "equal": " === ",

}

ctx.lists["user.values"] = {
    "null": "null",
    "undefined": "undefined",
    "true": "true",
    "false": "false",
}

ctx.lists["user.javascript_types"] = {
    "string": "string",
    "number": "number",
    "boolean": "boolean",
    "any": "any",
    "void": "void",
    "unknown": "unknown",
    "never": "never",
    "object": "object",
}
