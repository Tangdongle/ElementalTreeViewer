#!/usr/bin/env python
from gi.repository import Gtk, GObject

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.connect("delete-event", Gtk.main_quit)

        self.set_default_size(200,200)

        self.liststore = Gtk.ListStore(str, bool, bool)
        self.liststore.append(["KK", False, True])
        self.liststore.append(["Slack", True, False])
        self.liststore.append(["Lame", False, False])

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled", self.on_cell_toggled)

        column_toggle = Gtk.TreeViewColumn("Toggle", renderer_toggle, active=1)
        treeview.append_column(column_toggle)

        renderer_radio = Gtk.CellRendererToggle()
        renderer_radio.set_radio(True)
        renderer_radio.connect("toggled", self.on_cell_radio_toggled)

        column_radio = Gtk.CellRendererToggle()
        renderer_radio.set_radio(True)
        renderer_radio.connect("toggled", self.on_cell_radio_toggled, active=2)
        treeview.append_column(column_radio)

        self.add(treeview)

    def on_cell_toggled(self, widget, path):
        self.liststore[path][1] = not self.liststore[path][1]

    def on_cell_radio_toggled(self, widget, path):
        selected_path = Gtk.TreePath(path)
        for row in self.liststore:
            row[2] = (row.path == selected_path)

win = MyWindow()
win.show_all()
Gtk.main()
