# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\device_decorator_factory.py
# Compiled at: 2018-06-05 08:04:21
from __future__ import absolute_import, print_function, unicode_literals
from pushbase.device_decorator_factory import DeviceDecoratorFactory as DeviceDecoratorFactoryBase
from .auto_filter import AutoFilterDeviceDecorator
from .compressor import CompressorDeviceDecorator
from .device_decoration import SamplerDeviceDecorator, PedalDeviceDecorator, DrumBussDeviceDecorator, UtilityDeviceDecorator
from .echo import EchoDeviceDecorator
from .eq8 import Eq8DeviceDecorator
from .operator import OperatorDeviceDecorator
from .simpler import SimplerDeviceDecorator
from .wavetable import WavetableDeviceDecorator

class DeviceDecoratorFactory(DeviceDecoratorFactoryBase):
    DECORATOR_CLASSES = {'OriginalSimpler': SimplerDeviceDecorator,
       'Operator': OperatorDeviceDecorator,
       'MultiSampler': SamplerDeviceDecorator,
       'AutoFilter': AutoFilterDeviceDecorator,
       'Eq8': Eq8DeviceDecorator,
       'Compressor2': CompressorDeviceDecorator,
       'Pedal': PedalDeviceDecorator,
       'DrumBuss': DrumBussDeviceDecorator,
       'Echo': EchoDeviceDecorator,
       'InstrumentVector': WavetableDeviceDecorator,
       'StereoGain': UtilityDeviceDecorator
       }