from talon import Module, ui

mod = Module()

@mod.action_class
class Actions:
    def window_maximise():
        """Maximise the current window"""
        ui.active_window().maximized = True

    def window_minimise():
        """Minimise the current window"""
        ui.active_window().minimized = True

    def window_close():
        """Close the current window"""
        ui.active_window().close()
