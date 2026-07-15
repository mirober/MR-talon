from talon import Module, speech_system, ui

from .screen_text import ScreenText

mod = Module()

# Overlay showing the most recent recognised phrase.
_screen = ui.screens()[0]
recognitions = ScreenText(
    text_size=36,
    color="ffffffff",
    background="00000000",
    x=_screen.rect.width - 1200,
    y=_screen.rect.height - 50,
    font="Consolas",
)
recognitions.set_text("===")


@mod.action_class
class Actions:
    def recognitions_toggle():
        """Toggle the recognition monitor"""
        recognitions.toggle()


def f(o):
    if o["phrase"]:
        txt = " ".join(o["phrase"])
        if len(txt) > 40:
            txt = txt[:40] + "..."
        recognitions.set_text(txt)


speech_system.register("post:phrase", f)
recognitions.show()
