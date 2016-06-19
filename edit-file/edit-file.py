# -*- Mode: python; coding: utf-8; tab-width: 4; indent-tabs-mode: nil; -*-
#
#    edit-file.py
#
#    Adds an option to edit the file containing the selected track
#    to the right click context menu.
#    Based on code in 
#
#    Partly based on code in https://github.com/donaghhorgan/rhythmbox-plugins-open-containing-folder/blob/master/OpenContainingFolder.py

from gi.repository import Gio, GObject, Gtk, Peas, RB
import subprocess


class EditFile(GObject.Object, Peas.Activatable):

    """Adds an option to edit the file containing the selected track to
    the right click context menu."""

    object = GObject.property(type=GObject.Object)

    _action = 'edit-file'
    _locations = ['browser-popup',
                  'playlist-popup',
                  'podcast-episode-popup',
                  'queue-popup']

    def __init__(self):
        super(EditFile, self).__init__()
        self._app = Gio.Application.get_default()

    def edit_file(self, *args):
        """Open the given folder.

        Args:
            args: Additional arguments. These are ignored.
        """
        page = self.object.props.selected_page
        try:
            selected = page.get_entry_view().get_selected_entries()
            if selected:
                uri = selected[0].get_playback_uri()
                print('edit-file plugin: uri==<{}>'.format(uri))
                abspath = uri.replace("file://","")
                print('edit-file plugin: abspath==<{}>'.format(abspath))
                subprocess.check_call(['audacity', abspath])
        except:
            print('edit-file plugin: Could not edit file')

    def do_activate(self):
        """Activate the plugin."""
        print('edit-file plugin: Activating')

        action = Gio.SimpleAction(name=EditFile._action)
        action.connect('activate', self.edit_file)
        self._app.add_action(action)

        item = Gio.MenuItem()
        item.set_label('Edit file')
        item.set_detailed_action('app.%s' % EditFile._action)

        for location in EditFile._locations:
            self._app.add_plugin_menu_item(location,
                                           EditFile._action,
                                           item)

    def do_deactivate(self):
        """Deactivate the plugin."""
        print('edit-file plugin: Deactivating')

        for location in EditFile._locations:
            self._app.remove_plugin_menu_item(location,
                                              EditFile._action)
