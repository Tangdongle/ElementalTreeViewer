#!/usr/bin/env python
from gi.repository import Gtk, GObject

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.set_border_width(10)

        button = Gtk.LinkButton("http://www.gtk.org", "Visit GTK+ Homepage")
        self.add(button)

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
