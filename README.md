# glitch-scripts
Collection of Python scripts used to modify image/animation files. Most of these assume PNG image format


### two-img-glitcher.py
Given two images of identical size, shifts pixel rows/columns pseudorandomly (based on values) and reassembles them into one image.

### synfig-layer-opacity.py
Given a Synfig Studio animation file, parses through the file (XML style) and changes any layers with specific text in the description, in order, to display only one layer at a given frame.
simpler example: given 24 images (layers), this makes the file show 1 layer per frame duration (assuming default 24 FPS in this case)

### glitch-img-generator.py
Given a base image file, this generates glitched images utilizing the glitch_this and (optionally) glitchart Python modules.
Parameters: file name, location, number of images desired, whether to use the glitchart module
to-do: fix rotation parameter; currently not working

### image-modifier.py
Given a base image file, generates 100 image copies, each one with pixel positions (rows / columns) modified randomly (distorting the image)
to-do: allow for user to pass their own number values as parameters

### picture-resizer.py
Given a directory it resizes/rescales all images in said directory to the specified width/height in the script
to-do: more customization and flexibility regarding input

### synfig-glitcher.py
Given a Synfig Studio animation file, parses through the file (XML style) and changes any layers with specific text in the description (in this case, angles and offsets), distorting them for a given time period
to-do: clean this up - offsets are broken; remove dependency on synfig-layer-opacity

### glitch-multiples.py
Identical to glitch_img_generator.py but instead of creating copies of one image, parses through a directory and applies a randomized glitch effect to all images in the directory
