#!/usr/bin/env python
from gi.repository import Gtk, GObject
from gi.repository.GdkPixbuf import Pixbuf

icons = ["gtk-cut", "gtk-paste", "gtk-copy"]

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.connect("delete-event", Gtk.main_quit)

        self.set_default_size(200,200)

        liststore = Gtk.ListStore(Pixbuf, str)
        iconview = Gtk.IconView.new()
        iconview.set_model(liststore)
        iconview.set_pixbuf_column(0)
        iconview.set_text_column(1)

        for icon in icons:
            pixbuf = Gtk.IconTheme.get_default().load_icon(icon, 64, 0)
            liststore.append([pixbuf, "Label"])

        self.add(iconview)

win = MyWindow()
win.show_all()
Gtk.main()
