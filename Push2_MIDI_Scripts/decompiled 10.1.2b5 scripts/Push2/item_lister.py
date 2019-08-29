# uncompyle6 version 3.0.1
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.13 (default, Jan 19 2017, 14:48:08) 
# [GCC 6.3.0 20170118]
# Embedded file name: c:\Jenkins\live\output\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push2\item_lister.py
# Compiled at: 2019-04-23 10:50:00
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.components import ItemListerComponent as ItemListerComponentBase, ItemSlot, SimpleItemSlot

class IconItemSlot(SimpleItemSlot):

    def __init__(self, icon='', *a, **k):
        super(IconItemSlot, self).__init__(*a, **k)
        self._icon = icon

    @property
    def icon(self):
        return self._icon


class ItemListerComponent(ItemListerComponentBase):

    def _create_slot(self, index, item, nesting_level):
        items = self._item_provider.items[self.item_offset:]
        num_slots = min(self._num_visible_items, len(items))
        slot = None
        if index == 0 and self.can_scroll_left():
            slot = IconItemSlot(icon='page_left.svg')
            slot.is_scrolling_indicator = True
        else:
            if index == num_slots - 1 and self.can_scroll_right():
                slot = IconItemSlot(icon='page_right.svg')
                slot.is_scrolling_indicator = True
            else:
                slot = ItemSlot(item=item, nesting_level=nesting_level)
                slot.is_scrolling_indicator = False
        return slot