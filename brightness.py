import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import subprocess

class BrightnessSlider(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Brilho da Tela - brightnessctl")
        self.set_default_size(450, 250)
        self.set_border_width(10)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box)

        adjustment = Gtk.Adjustment(50, 0, 100, 1, 10, 0)
        self.scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=adjustment)
        self.scale.set_digits(0)
        self.scale.set_hexpand(True)
        self.scale.connect("value-changed", self.on_scale_changed)
        box.pack_start(self.scale, True, True, 0)

    def on_scale_changed(self, scale):
        value = int(scale.get_value())
        subprocess.run(["brightnessctl", "set", str(value) + "%"])

win = BrightnessSlider()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

