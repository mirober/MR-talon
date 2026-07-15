from talon import Module, Context, actions
from talon.grammar import Phrase
from typing import Union

mod = Module()

def camel(text: str):
    if len(text) > 1:
        text = text.title()
        return text[0].lower() + text[1:]
    else:
        return text[0].lower()

def password(text: str):
    text = "".join(text.split(" "))
    text = text.lower()
    punc = "@1/4#9?5%,."
    result = []
    for i in range(len(text)):
        if i%2==0:
            result.append(punc[(i//2)%len(punc)])
        if i%3==0:
            result.append(text[i].upper())
        else:
            result.append(text[i])
    return "".join(result)

def dictation(text: str) -> str:
    text = text.lower()
    text = text.replace("- ", "-")
    text = text.replace(" i ", " I ")
    text = text.replace(" i'", " I'")
    if text.startswith("i "):
        text = "I " + text[2:]
    if text.endswith(" i"):
        text = text[:-2] + " I"
    text = text.replace(" id ", " ID ")
    return text

CAPITALISATIONS = {
    0: lambda text: text,
    1: lambda text: text.upper(),
    2: lambda text: text.title(),
    3: camel,
    4: lambda text: text.capitalize(),
    5: lambda text: text.lower(),
    6: password,
    7: dictation,
}

SPACINGS = {
    0: " ",
    1: "",
    2: "-",
    3: "_",
    4: ".",
    5: "/",
    6: "\\",
    7: ", ",
}

def format_text(text, capitalisation=0, spacing=0):
    if not text: return ""
    if capitalisation == 0:
        capitalisation = 5
    if spacing == 0 and capitalisation == 3:
        spacing = 1
    if spacing == 0 and capitalisation == 2:
        spacing = 1
    text = CAPITALISATIONS[capitalisation](text)
    text = SPACINGS[spacing].join(text.split(" "))
    return text

@mod.action_class
class Actions:
    def formatted_text(phrase: list[str], capitalisation: Union[str, int], spacing: Union[str, int]) -> str:
        """Formats a phrase according to formatters. formatters is a comma-separated string of formatters (e.g. 'CAPITALIZE_ALL_WORDS,DOUBLE_QUOTED_STRING')"""
        if not phrase:
            return ""
        capitalisation, spacing = int(capitalisation), int(spacing)
        words = " ".join(phrase)
        return format_text(words, capitalisation, spacing)

    def snake(phrase: Union[list[str], str]) -> str:
        """Return snake text"""
        return actions.user.formatted_text(phrase, 0, 3)

    def camel(phrase: Union[list[str], str]) -> str:
        """Return camel text"""
        return actions.user.formatted_text(phrase, 3, 1)

    def title(phrase: Union[list[str], str]) -> str:
        """Return title text"""
        return actions.user.formatted_text(phrase, 2, 1)

    def phrase_to_str(phrase: Union[list[str], str]) -> str:
        """Parse and join a phrase into a string"""
        words = " ".join(actions.dictate.parse_words(phrase))
        return words
