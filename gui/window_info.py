from talon import ui, Module, Context, registry, actions, imgui, cron
import time
mod = Module()

@imgui.open(x=0, y=30)
def window_info(gui: imgui.GUI):
    gui.text(f"{ui.active_app()}")
    gui.text(f"{ui.active_app().exe}")
    gui.text(f"{ui.active_window().title}")
    gui.text(f"")

    for c in reversed(registry.active_contexts()):
        if not c.path.startswith("user."): continue
        if not c.path.endswith(".talon"): continue
        p = c.path[5:-6]
        gui.text(f"- {p}")

    time.sleep(0.1)

@mod.action_class
class Actions:
    def window_info_toggle():
        """toggle window info imgui"""
        window_info.hide() if window_info.showing else window_info.show()
