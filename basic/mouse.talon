# mouse_click(button: int = 0, down: bool = None, up: bool = None, hold: int = None)
#   Click, hold, or release a mouse button
copy mouse position: user.copy_mouse_position()
copy mouse relative: user.copy_mouse_position_relative_window()

shifty:
    key(shift:down)
    mouse_click()
    key(shift:up)
    user.grid_close()
colic:
    key(ctrl:down)
    mouse_click()
    key(ctrl:up)
    user.grid_close()
mouse (alt|alternate) click:
    key(alt:down)
    mouse_click()
    key(alt:up)
    user.grid_close()
millick:
    mouse_click(2)
    user.grid_close()
kick:
    mouse_click()
    user.grid_close()
kick double:
    mouse_click()
    mouse_click()
    user.grid_close()
squat:
    user.mouse_drag()
    user.grid_close()
bench:
    user.mouse_release()
    user.grid_close()
kick for <number> seconds:
    user.mouse_click_for_seconds(number)
kick for <number> minutes:
    user.mouse_click_for_minutes(number)
