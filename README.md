# Push2_MIDI_Scripts

MIDI Scripts included with Ableton Live are compiled and editing them is unsupported. Scripts are sometimes changed without notice, which can cause your edits to make the application unstable. Decompiling the scripts is simple and almost always works without issue. It is also unsupported and probably breaks license. However, placing .py files into Ableton directories will compile them on application start (no telling if this will be removed, but I doubt it). This allows to make simple or very complex edits to the functionality of your controllers.<br/><br/>
Push 2 is almost entirely controlled via sysex and python scripts, so it is possible to make it do some things a bit better or make your live performances safer. For the most part, you can use Max4Live to adjust the functionality, but it was quicker to edit the MIDI scripts in my use case.<br/><br/><br/>
Since scripts change from time to time, I do not comment the .py files at the moment. So here are the changes:<br/>

<b>Pushbase/push_base.py</b><br/>
Switched CUE and MASTER volume controls - prevents from accidentally turning down master volume. (LINE 795, 797)<br/>
Tap Tempo is disabled since it is very poor and will hiccup playback even from one press. (LINE 585)<br/><br/>

<b>Pushbase/quantization_component.py</b><br/>
Default Quantization is changed from 100% to 44%. (LINE 43)<br/><br/>

<b>Push2/Push2.py</b><br/>
Track Mix mode default is initially for the selected TRACK, not the entire SET. Quicker workflow imo. (LINE 620)<br/><br/>

<b>Push2/drum_group_component.py</b><br/>
Shade level of muted pads is darker. (LINE 223)<br/><br/>

<b>Push2/skin_default.py</b><br/>
Bunch of color changes that communicate if Automation is on/off, a drumrack pad is muted but selected, white midi keys on the pads are dimmer, Repeat causes unselected modes to flash in Amber color, some buttons flash faster or off beat so they are easier to notice.<br/><br/><br/>

If working on windows, you can mass rename a folder with the python files to txt files to quickly search the contents for needed keywords with the terminal command "ren *.py *.txt".<br/><br/>


