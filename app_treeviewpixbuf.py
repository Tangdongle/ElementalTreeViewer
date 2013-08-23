#!/usr/bin/env python
from gi.repository import Gtk, GObject

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.connect("delete-event", Gtk.main_quit)

        self.set_default_size(200,200)

        self.liststore = Gtk.ListStore(str, str)
        self.liststore.append(["KK", Gtk.STOCK_NEW])
        self.liststore.append(["Slack", Gtk.STOCK_OPEN])
        self.liststore.append(["Lame", Gtk.STOCK_SAVE])

        treeview = Gtk.TreeView(model=self.liststore)

        renderer_text = Gtk.CellRendererText()
        column_text = Gtk.TreeViewColumn("Text", renderer_text, text=0)
        treeview.append_column(column_text)

        renderer_pixbuf = Gtk.CellRendererPixbuf()

        column_pixbuf = Gtk.TreeViewColumn("Image", renderer_pixbuf, stock_id=1)
        treeview.append_column(column_pixbuf)

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
