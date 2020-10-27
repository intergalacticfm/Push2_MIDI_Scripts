# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\settings.py
# Compiled at: 2020-10-13 19:08:18
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.setting import OnOffSetting

def create_settings(preferences=None):
    preferences = preferences if preferences is not None else {}
    return {'workflow': OnOffSetting(name='Workflow', value_labels=[
                  'Scene', 'Clip'], default_value=True, preferences=preferences)
       }