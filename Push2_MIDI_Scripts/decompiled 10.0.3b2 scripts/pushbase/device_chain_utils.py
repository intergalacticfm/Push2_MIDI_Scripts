# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\device_chain_utils.py
# Compiled at: 2018-06-05 08:04:22
from __future__ import absolute_import, print_function, unicode_literals
import Live
from itertools import imap, chain
from functools import partial
from ableton.v2.base import find_if, liveobj_valid

def is_empty_drum_pad(drum_pad):
    return isinstance(drum_pad, Live.DrumPad.DrumPad) and (not drum_pad.chains or not drum_pad.chains[0].devices)


def is_first_device_on_pad(device, drum_pad):
    return find_if(lambda pad: pad.chains and pad.chains[0].devices and pad.chains[0].devices[0] == device, drum_pad.canonical_parent.drum_pads)


def is_simpler(device):
    return device and device.class_name == 'OriginalSimpler'