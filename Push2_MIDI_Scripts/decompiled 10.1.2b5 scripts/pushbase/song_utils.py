# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\song_utils.py
# Compiled at: 2018-11-27 11:59:28
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.base import liveobj_valid

def is_return_track(song, track):
    return track in list(song.return_tracks)


def delete_track_or_return_track(song, track):
    tracks = list(song.tracks)
    if track in tracks:
        track_index = tracks.index(track)
        song.delete_track(track_index)
    else:
        track_index = list(song.return_tracks).index(track)
        song.delete_return_track(track_index)


def find_parent_track(live_object):
    u"""
    Returns either the parent track of a live object or None if one is not found.
    """
    track = live_object
    while liveobj_valid(track) and not isinstance(track, Live.Track.Track):
        track = getattr(track, 'canonical_parent', None)

    return track