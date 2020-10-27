# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\track_frozen_mode.py
# Compiled at: 2020-06-19 15:18:06
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import listens
from ableton.v2.control_surface.mode import ModesComponent

class TrackFrozenModesComponent(ModesComponent):

    def __init__(self, default_mode=None, frozen_mode=None, *a, **k):
        super(TrackFrozenModesComponent, self).__init__(*a, **k)
        assert default_mode is not None
        assert frozen_mode is not None
        self.add_mode('default', default_mode)
        self.add_mode('frozen', frozen_mode)
        self._on_selected_track_is_frozen_changed.subject = self.song.view
        if self.is_enabled():
            self._update_selected_mode()
        return

    def _update_selected_mode(self):
        self.selected_mode = 'frozen' if self.song.view.selected_track.is_frozen else 'default'

    @listens('selected_track.is_frozen')
    def _on_selected_track_is_frozen_changed(self):
        self._update_selected_mode()

    def update(self):
        super(TrackFrozenModesComponent, self).update()
        if self.is_enabled():
            self._update_selected_mode()