from subprocess import Popen
from talon import ui, Module, Context, registry, actions, imgui, cron
from talon import imgui
import os
import time

mod = Module()
ctx = Context("mute")

@imgui.open(x=1300, y=1045)
def gui_mute(gui: imgui.GUI):
    if gui.button("Mute"):
        actions.key("alt-a")
        speech_system.engine_mimic("wake up")

@mod.action_class
class Actions:
    def mute_show():
        """Show the mute button"""
        gui_mute.hide() if gui_mute.showing else gui_mute.show()
