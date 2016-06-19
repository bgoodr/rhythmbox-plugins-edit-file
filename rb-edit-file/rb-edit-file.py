# -*- coding: utf8 -*-
#
# Copyright (C) 2009, 2011 Martin Vogel <mail@martinvogel.de>
# http://www.martinvogel.de
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301  USA.
#
# Thanks to http://live.gnome.org/RhythmboxPlugins/WritingGuide
#
# rb-edit-file is a modification of the plugin rb-open-folder 
#  
# rb-open-folder was written by
# Adolfo González Blázquez <code@infinicode.org>
# http://www.infinicode.org/code/rb/

import rhythmdb, rb
import gobject, gtk
from subprocess import Popen
from urllib import url2pathname

ui_str = """
<ui>
  <popup name="BrowserSourceViewPopup">
    <placeholder name="PluginPlaceholder">
      <menuitem name="EditFilePopup" action="EditFile"/>
    </placeholder>
  </popup>

  <popup name="PlaylistViewPopup">
    <placeholder name="PluginPlaceholder">
      <menuitem name="EditFilePopup" action="EditFile"/>
    </placeholder>
  </popup>

  <popup name="QueuePlaylistViewPopup">
    <placeholder name="PluginPlaceholder">
      <menuitem name="EditFilePopup" action="EditFile"/>
    </placeholder>
  </popup>

  <popup name="PodcastViewPopup">
    <placeholder name="PluginPlaceholder">
      <menuitem name="EditFilePopup" action="EditFile"/>
    </placeholder>
  </popup>
</ui>
"""

class EditFile(rb.Plugin):

	def __init__(self):
		rb.Plugin.__init__(self)
			
	def activate(self, shell):
		self.action = gtk.Action('EditFile', _('Edit file'),
					 _('Edit this song with Audacity'),
					 'rb-edit-file')
		self.activate_id = self.action.connect('activate', self.edit_file, shell)
		
		self.action_group = gtk.ActionGroup('EditFilePluginActions')
		self.action_group.add_action(self.action)
		
		uim = shell.get_ui_manager ()
		uim.insert_action_group(self.action_group, 0)
		self.ui_id = uim.add_ui_from_string(ui_str)
		uim.ensure_update()
	
	def edit_file(self, action, shell):
		source = shell.get_property("selected_page")
		entry = rb.Source.get_entry_view(source)
		selected = entry.get_selected_entries()
		if selected != []:
			Datei = url2pathname(selected[0].get_playback_uri().replace("file://", ""))
			Popen(["audacity", Datei])
	
	def deactivate(self, shell):
		uim = shell.get_ui_manager()
		uim.remove_ui (self.ui_id)
		uim.remove_action_group (self.action_group)

		self.action_group = None
		self.action = None
