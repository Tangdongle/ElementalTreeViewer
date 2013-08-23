#!/usr/bin/env python
from gi.repository import Gtk, GObject, Gdk
from gi.repository.GdkPixbuf import Pixbuf

class MyWindow(Gtk.Window):
    def __init__(self):
#setup
        Gtk.Window.__init__(self, title="Hello World")
        self.connect("delete-event", Gtk.main_quit)
        self.set_size_request(200, 400)
        self.model = Gtk.TreeStore(str)

        for parent in range(4):
            piter = self.model.append(None, ['parent %i' % parent])
            for child in range(3):
                self.model.append(piter, ['child %i of parent %i' % (child, parent)])

        self.treeview = Gtk.TreeView(self.model)
        self.tree_selection = self.treeview.get_selection()
        self.tree_selection.set_mode(Gtk.SelectionMode.SINGLE)
        self.tree_selection.connect("changed", self.on_tree_selection_changed)


        tvcolumn = Gtk.TreeViewColumn('Column 0')
        self.treeview.append_column(tvcolumn)

        cell = Gtk.CellRendererText()
        #cell.connect("clicked", self.did_click_element)
        tvcolumn.pack_start(cell, True)

        tvcolumn.add_attribute(cell, 'text', 0)

        self.treeview.set_search_column(0)

        tvcolumn.set_sort_column_id(0)

        self.treeview.set_reorderable(True)
        self.add(self.treeview)

    def on_tree_selection_changed(self, selection):
        model, treeiter = selection.get_selected()
        if treeiter:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, "You selected %s" % model[treeiter][0])
            dialog.run()

        dialog.destroy()

win = MyWindow()
win.show_all()
Gtk.main()
