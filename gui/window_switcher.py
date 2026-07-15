from talon import ui, Module, Context, actions
from pyvda import get_apps_by_z_order

from .screen_text import ScreenText

mod = Module()
ctx = Context()
current_windows = []

mod.tag("window_switcher_showing", "Set when the window switcher is showing")

_screen = ui.screens()[0]
window_switcher = ScreenText(
    x=_screen.rect.center.x,
    y=_screen.rect.center.y,
    align="center",
    font="Consolas",
    text_size=36,
    color="ffffffaa",
    background="000000",
    padding=20,
    line_spacing=8,
)


def _build_windows():
    global current_windows
    current_windows = []
    windows = {w.id: w for w in ui.windows()}
    for a in get_apps_by_z_order():
        w = windows.get(a.hwnd)
        if w is not None:
            current_windows.append(w)

def _truncate(s: str, max_len: int) -> str:
    """Truncate a string to a maximum length, adding ellipsis if truncated."""
    if len(s) <= max_len:
        return s
    return s[:max_len - 3] + "..."

def _render():
    lines = [
        f"{i: >2}. {_truncate(w.app.name, 20): <20} {_truncate(w.title, 60)}"
        for i, w in enumerate(current_windows, 1)
    ]
    window_switcher.set_text("\n".join(lines))


@mod.action_class
class Actions:
    def window_switcher_toggle():
        """Toggle the window switcher UI"""
        global current_windows
        if window_switcher.showing:
            window_switcher.hide()
            ctx.tags = []
            current_windows = []
        else:
            _build_windows()
            _render()  # set_text shows the overlay
            ctx.tags = ["user.window_switcher_showing"]

    def window_switcher_focus(i: int):
        """Focus one of the windows in the window switcher list"""
        current_windows[i - 1].focus()
        actions.user.window_switcher_toggle()
