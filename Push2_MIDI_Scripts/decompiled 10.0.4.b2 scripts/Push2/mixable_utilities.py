# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\mixable_utilities.py
# Compiled at: 2018-07-05 11:42:58
from __future__ import absolute_import, print_function, unicode_literals
import Live
from ableton.v2.control_surface import find_instrument_meeting_requirement

def is_chain(track_or_chain):
    return isinstance(getattr(track_or_chain, 'proxied_object', track_or_chain), Live.Chain.Chain)


def is_midi_track(track):
    return getattr(track, 'has_midi_input', False) and not is_chain(track)


def is_audio_track(track):
    return getattr(track, 'has_audio_input', False) and not is_chain(track)


def can_play_clips(mixable):
    return hasattr(mixable, 'fired_slot_index')


def find_drum_rack_instrument(track):
    return find_instrument_meeting_requirement(lambda i: i.can_have_drum_pads, track)


def find_simpler(track_or_chain):
    return find_instrument_meeting_requirement(lambda i: hasattr(i, 'playback_mode'), track_or_chain)