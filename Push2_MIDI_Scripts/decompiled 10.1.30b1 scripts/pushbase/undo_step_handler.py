# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\undo_step_handler.py
# Compiled at: 2020-06-19 15:18:06
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid

class UndoStepHandler(object):
    u"""
        Class that keeps a set of clients for the current undo step.
        The first client to ask for an undo step will trigger a new step;
        subsequent clients are just added to the stack. The step is only
        ended when all client have asked for it to be ended.
    """

    def __init__(self, song=None):
        assert liveobj_valid(song)
        self._song = song
        self._clients = set()

    def _begin_step_with_client(self, client):
        if client not in self._clients:
            self._clients.add(client)
            if len(self._clients) == 1:
                self._song.begin_undo_step()

    def _end_step_with_client(self, client):
        if client in self._clients:
            self._clients.remove(client)
            if len(self._clients) == 0:
                self._song.end_undo_step()

    def begin_undo_step(self, client=None):
        if client:
            self._begin_step_with_client(client)
        else:
            self._song.begin_undo_step()

    def end_undo_step(self, client=None):
        if client:
            self._end_step_with_client(client)
        else:
            self._song.end_undo_step()
            if len(self._clients) > 0:
                self._song.begin_undo_step()