from talon import ui, Module, Context, registry, actions, imgui, cron, ctrl, clip
import time

mod = Module()
ctx = Context()

@mod.action_class
class Actions:
    def mouse_drag():
        """Start dragging"""
        ctrl.mouse_click(down=True)

    def mouse_release():
        """Release drag"""
        ctrl.mouse_click(up=True)
        current_exe = ui.active_app().exe.lower()

    def mouse_move_relative(x: int, y: int):
        """Move the mouse relative to its current position"""
        x_cur, y_cur = ctrl.mouse_pos()
        actions.mouse_move(x_cur+x, y_cur+y)

    def copy_mouse_position():
        """Copy the current mouse position coordinates"""
        position = ctrl.mouse_pos()
        clip.set_text((repr(position)))

    def copy_mouse_position_relative_window():
        """Copy the current mouse position coordinates"""
        x, y = ctrl.mouse_pos()
        rect = ui.active_window().rect
        clip.set_text((x - rect.left, y - rect.top))

    def mouse_move_relative_window(x: int, y: int):
        """Move the mouse to a point relative to the current window"""
        rect = ui.active_window().rect
        actions.mouse_move(x+rect.left, y+rect.top)

    def mouse_move_center_active_window():
        """move the mouse cursor to the center of the currently active window"""
        rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))

    def mouse_click_for_seconds(s: int):
        """Click the mouse, then click again after s seconds"""
        ctrl.mouse_click()
        cron.after(f"{s}s", lambda: ctrl.mouse_click())

    def mouse_click_for_minutes(s: int):
        """Click the mouse, then click again after s seconds"""
        ctrl.mouse_click()
        cron.after(f"{s*60}s", lambda: ctrl.mouse_click())
