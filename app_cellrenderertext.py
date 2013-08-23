#!/usr/bin/env python
from gi.repository import Gtk, GObject

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.connect("delete-event", Gtk.main_quit)

        self.set_default_size(200,200)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["KK","http://www.google.com"])
        self.liststore.append(["Slack","http://www.windows.com"])
        self.liststore.append(["Lame","http://www.apple.com"])

        treeview = Gtk.TreeView(model=self.liststore)
        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_editabletext = Gtk.CellRendererText()
        renderer_editabletext.set_property("editable",True)

        column_editabletext = Gtk.TreeViewColumn("Editable Text", renderer_editabletext, text=1)
        treeview.append_column(column_editabletext)

        renderer_editabletext.connect("edited", self.text_edited)

        self.add(treeview)

    def text_edited(self, widget, path, text):
        self.liststore[path][1] = text

win = MyWindow()
win.show_all()
Gtk.main()
