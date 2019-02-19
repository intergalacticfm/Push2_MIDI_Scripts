# Push2_MIDI_Scripts

MIDI Scripts included with Ableton Live are compiled and editing them is unsupported. Scripts are sometimes changed without notice, which can cause your edits to make the application unstable. Decompiling the scripts is simple and almost always works without issue. It is also unsupported and probably breaks license. However, placing .py files into Ableton directories will compile them on application start (no telling if this will be removed, but I doubt it). This allows to make simple or very complex edits to the functionality of your controllers.<br/><br/>
Push 2 is almost entirely controlled via sysex and python scripts, so it is possible to make it do some things a bit better or make your live performances safer. For the most part, you can use Max4Live to adjust the functionality, but it was quicker to edit the MIDI scripts in my use case.<br/><br/><br/>
Since scripts change from time to time, I do not comment the .py files at the moment. So here are the changes:<br/>

<b>Pushbase/push_base.py</b><br/>
Switched CUE and MASTER volume controls - prevents from accidentally turning down master volume. (LINE 808)<br/>
Tap Tempo is disabled since it is very poor and will hiccup playback even from one press. (LINE 592)<br/><br/>

<b>Push2/Push2.py</b><br/>
Track Mix mode default is initially for the selected TRACK, not the entire SET. Quicker workflow imo. (LINE 637)<br/><br/>

<b>Push2/drum_group_component.py</b><br/>
Shade level of muted pads is darker. (LINE 223)<br/><br/>

<b>Push2/skin_default.py</b><br/>
Color changes that communicate if Automation is on/off, a drumrack pad is muted (LINE 47) but selected (LINE 48) pulsates, dramrack pad is soloed (LINE 50) pulses,  white midi keys on the pads are dimmer (LINE 34), Repeat causes unselected modes to flash in Amber color, mute off is Amber color (LINE 131), locked mute (LINE 134) and locked solo modes (LINE 135) flash offbeat to be more noticeable, Metronome button is dimmed (LINE 226), Fixed Length button is dimmer but flashes faster when active to be more noticeable (LINE 229-), Accent button is dimmer but flashes faster when active to be more noticeable (LINE 235-), Automation button is blue when off (LINE 194).

