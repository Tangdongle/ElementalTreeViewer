#!/usr/bin/env python
from gi.repository import Gtk, GObject, Gdk
from gi.repository.GdkPixbuf import Pixbuf

class DialogExample(Gtk.Dialog):
    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "My Dialog", parent, 0, (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(150,100)

        label = Gtk.Label("This is a dialog to display additional information")

        box = self.get_content_area()
        box.add(label)
        self.show_all()

class MyWindow(Gtk.Window):
    def __init__(self):
#setup
        Gtk.Window.__init__(self, title="Hello World")
        self.connect("delete-event", Gtk.main_quit)
        self.set_border_width(6)

        button = Gtk.Button("Open Dialog")
        button.connect("clicked", self.on_button_clicked)
        self.add(button)

    def on_button_clicked(self, widget):
        dialog = DialogExample(self)
        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print "OK Pressed"
        elif response == Gtk.ResponseType.CANCEL:
            print "Cancel Pressed"

        dialog.destroy()


win = MyWindow()
win.show_all()
Gtk.main()
