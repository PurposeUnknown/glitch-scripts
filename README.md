# glitch-scripts
Collection of Python scripts used to modify image/animation files.


### two-img-glitcher.py
Given two images of identical size, shifts pixel rows/columns pseudorandomly (based on values) and reassembles them into one image.

### synfig-layer-opacity.py
Given a Synfig Studio animation file, parses through the file (XML style) and changes any layers with specific text in the description, in order, to display only one layer at a given frame.
simpler example: given 24 images (layers), this makes the file show 1 layer per frame duration (assuming default 24 FPS in this case)
