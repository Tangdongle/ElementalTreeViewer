#!/usr/bin/env python
from gi.repository import Gtk, GObject

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button("Click Me")
        button.connect("clicked", self.on_click_me_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("_Close", use_underline=True)
        button.connect("clicked", self.on_close_clicked)
        hbox.pack_end(button, True, True, 0)

        button = Gtk.Button(stock=Gtk.STOCK_OPEN)
        button.connect("clicked", self.on_open_clicked)
        hbox.pack_start(button, True, True, 0)

    def on_click_me_clicked(self, button):
        print "\"Click me\" button was clicked"

    def on_open_clicked(self, button):
        print "\"Open\" button was clicked"

    def on_close_clicked(self, button):
        print "Closing App"
        Gtk.main_quit()



win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
