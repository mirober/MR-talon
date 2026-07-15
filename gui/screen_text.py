# A simple "draw this text on the screen" overlay, built on talon.canvas.
#
# Intended as a lighter, more controllable replacement for imgui-based text
# overlays: no window chrome, precise anchor-based positioning, and an
# optional background box behind the text. Modelled on the canvas lifecycle
# used by mouse_grid/mouse_grid.py.
from talon import canvas, ui
from talon.skia import Paint, Rect


class ScreenText:
    """Draws a (possibly multi-line) string on a screen overlay.

    Positioning is by anchor point: ``x``/``y`` give a point on the chosen
    screen, and ``align`` decides which part of the text box sits at that
    point (e.g. "top left", "center", "bottom right"). ``x``/``y`` default to
    the centre of the screen.
    """

    def __init__(
        self,
        *,
        screen=None,
        x=None,
        y=None,
        text_size=24,
        color="00ff00ff",
        background="000000aa",
        font=None,
        align="center",
        padding=12,
        line_spacing=4,
    ):
        self.screen = screen if screen is not None else ui.screens()[0]
        self.x = x if x is not None else self.screen.rect.center.x
        self.y = y if y is not None else self.screen.rect.center.y
        self.text_size = text_size
        # A font-family name (e.g. "monospace", "Consolas"); None uses the
        # canvas default. Must be applied before measuring so the box matches.
        self.font = font
        self.color = color
        self.background = background
        self.align = align
        self.padding = padding
        self.line_spacing = line_spacing

        self.text = ""
        self.canvas = None
        self.showing = False

    # -- public interface --------------------------------------------------

    def set_text(self, text):
        """Update the displayed text and repaint (shows the overlay if hidden)."""
        self.text = text or ""
        if not self.showing:
            self.show()
        else:
            self.canvas.freeze()

    def show(self):
        if self.showing:
            return
        if self.canvas is None:
            self.canvas = canvas.Canvas.from_screen(self.screen)
        self.canvas.register("draw", self.draw)
        self.canvas.freeze()
        self.showing = True

    def hide(self):
        if not self.showing:
            return
        self.canvas.unregister("draw", self.draw)
        self.canvas.hide()
        self.showing = False

    def toggle(self):
        self.hide() if self.showing else self.show()

    def close(self):
        """Tear down the canvas entirely (releases the overlay surface)."""
        if self.canvas is not None:
            if self.showing:
                self.canvas.unregister("draw", self.draw)
            self.canvas.close()
            self.canvas = None
        self.showing = False

    # -- drawing -----------------------------------------------------------

    def _measure(self, paint):
        """Return (lines, width, line_height, ascent, total_height, left_bearing).

        Line height and ascent come from a fixed reference string (with both
        ascenders and descenders) rather than each line's own tight bounding
        box, so every row advances by the same amount and spacing stays even.

        ``measure_text`` gives each line's tight *ink* bounds relative to the
        pen origin: ``rect.x`` is the left side bearing. We track the overall
        ink extent so the caller can offset the pen (by ``left_bearing``) and
        get equal padding on both sides.
        """
        lines = self.text.split("\n")
        ref = paint.measure_text("Ayg|")[1]
        line_height = ref.height
        ascent = -ref.y

        left_bearing = 0.0
        right_extent = 0.0
        for line in lines:
            rect = paint.measure_text(line or " ")[1]
            left_bearing = min(left_bearing, rect.x)
            right_extent = max(right_extent, rect.x + rect.width)
        width = right_extent - left_bearing

        total_height = line_height * len(lines) + self.line_spacing * max(len(lines) - 1, 0)
        return lines, width, line_height, ascent, total_height, left_bearing

    def _anchor_origin(self, width, height):
        """Top-left corner of the text box given the anchor point and alignment."""
        align = self.align.lower()
        if "left" in align:
            left = self.x
        elif "right" in align:
            left = self.x - width
        else:
            left = self.x - width / 2

        if "top" in align:
            top = self.y
        elif "bottom" in align:
            top = self.y - height
        else:
            top = self.y - height / 2
        return left, top

    def draw(self, canvas):
        paint = canvas.paint
        paint.textsize = self.text_size
        paint.text_align = paint.TextAlign.LEFT
        if self.font is not None:
            paint.typeface = self.font

        lines, width, line_height, ascent, total_height, left_bearing = self._measure(paint)
        if not self.text:
            return

        left, top = self._anchor_origin(width, total_height)
        # Shift the pen so the ink's left edge lands on the content-left,
        # giving equal padding on both sides.
        pen_x = left - left_bearing

        if self.background:
            bg = Rect(
                left - self.padding,
                top - self.padding,
                width + self.padding * 2,
                total_height + self.padding * 2,
            )
            paint.style = Paint.Style.FILL
            paint.color = self.background
            canvas.draw_rect(bg)

        paint.style = Paint.Style.FILL
        paint.color = self.color
        step = line_height + self.line_spacing
        for i, line in enumerate(lines):
            # Uniform per-line advance; baseline sits `ascent` below the row top.
            canvas.draw_text(line, pen_x, top + ascent + i * step)
