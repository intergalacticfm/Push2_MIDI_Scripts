# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\note_editor.py
# Compiled at: 2018-06-05 08:04:21
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.note_editor_component import NoteEditorComponent

class Push2NoteEditorComponent(NoteEditorComponent):
    __events__ = (u'mute_solo_stop_cancel_action_performed', )

    def _on_pad_pressed(self, coordinate):
        super(Push2NoteEditorComponent, self)._on_pad_pressed(coordinate)
        self.notify_mute_solo_stop_cancel_action_performed()