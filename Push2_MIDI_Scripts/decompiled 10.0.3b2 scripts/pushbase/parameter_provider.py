# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\pushbase\parameter_provider.py
# Compiled at: 2018-06-05 08:04:22
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import liveobj_valid, NamedTuple, EventObject
DISCRETE_PARAMETERS_DICT = {'GlueCompressor': (u'Ratio', u'Attack', u'Release', u'Peak Clip In')
   }

def is_parameter_quantized(parameter, parent_device):
    is_quantized = False
    if liveobj_valid(parameter):
        device_class = getattr(parent_device, 'class_name', None)
        is_quantized = parameter.is_quantized or device_class in DISCRETE_PARAMETERS_DICT and parameter.name in DISCRETE_PARAMETERS_DICT[device_class]
    return is_quantized


class ParameterInfo(NamedTuple):
    parameter = None
    default_encoder_sensitivity = None
    fine_grain_encoder_sensitivity = None

    def __init__(self, name=None, *a, **k):
        super(ParameterInfo, self).__init__(_overriden_name=name, *a, **k)

    @property
    def name(self):
        actual_name = self.parameter.name if liveobj_valid(self.parameter) else ''
        return self._overriden_name or actual_name

    def __eq__(self, other_info):
        return super(ParameterInfo, self).__eq__(other_info) and self.name == other_info.name


class ParameterProvider(EventObject):
    __events__ = (u'parameters', )

    @property
    def parameters(self):
        return []