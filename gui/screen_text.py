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
        """Return (line_rects, total_width, total_height) for the current text."""
        lines = self.text.split("\n")
        line_rects = [paint.measure_text(line or " ")[1] for line in lines]
        width = max((r.width for r in line_rects), default=0)
        height = sum(r.height for r in line_rects)
        height += self.line_spacing * max(len(lines) - 1, 0)
        return lines, line_rects, width, height

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

        lines, line_rects, width, height = self._measure(paint)
        if not self.text:
            return

        left, top = self._anchor_origin(width, height)

        if self.background:
            bg = Rect(
                left - self.padding,
                top - self.padding,
                width + self.padding * 2,
                height + self.padding * 2,
            )
            paint.style = Paint.Style.FILL
            paint.color = self.background
            canvas.draw_rect(bg)

        paint.style = Paint.Style.FILL
        paint.color = self.color
        y = top
        for line, rect in zip(lines, line_rects):
            # rect.y is the (negative) ascent above the baseline, so the
            # baseline for this line sits at y - rect.y, seating the glyphs
            # inside the measured box rather than floating above it.
            canvas.draw_text(line, left, y - rect.y)
            y += rect.height + self.line_spacing
