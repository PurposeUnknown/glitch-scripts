import os
import random
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element

# Input: a Synfig Studio .sif animation file with multiple images/layers
# Parses through the file and timeshifts/changes opacity of all layers with specific text in description
# this effectively makes it so 1 'image layer' is visible every frame duration (default 24 fps)

dir_start = os.getcwd()
directory = dir_start + "/" + input("Give me a folder: ") + "/"

if os.path.isdir(directory):
    os.chdir(directory)

animation = input("Enter the base animation: ")
layerdesc = input("Give me the layer description: ")
tree = ET.parse(f"{animation}.sif")
root = tree.getroot()

opacity_time = 0

# Layer Adjustments
for layer in root.iter("layer"):
    if (layer.attrib["type"] == "switch") and (layerdesc in layer.attrib["desc"]): 
        for element in layer:

            #duration = round(random.uniform(0, 0.18), 8)
            duration = round(0.03333333, 8)

            # Opacity
            if element.attrib["name"] == "amount":

                # Clear and reset the layer
                element.clear()
                element.attrib["name"] = "amount"

                # Create subelements; this assumes two timestamp waypoints
                animated = ET.SubElement(element, "animated")
                animated.attrib["type"] = "real"

                startpoint = ET.SubElement(animated, "waypoint")
                startpoint.attrib["time"] = "0s"
                startpoint.attrib["before"] = "constant"
                startpoint.attrib["after"] = "constant"
                real = ET.SubElement(startpoint, "real")
                real.attrib["value"] = "0.0000000000"
                if opacity_time == 0:
                    real.attrib["value"] = "1.0000000000"

                if opacity_time != 0:
                    firstpoint = ET.SubElement(animated, "waypoint")
                    firstpoint.attrib["time"] = f"{opacity_time}s"
                    firstpoint.attrib["before"] = "constant"
                    firstpoint.attrib["after"] = "constant"
                    real = ET.SubElement(firstpoint, "real")
                    real.attrib["value"] = "1.0000000000"

                opacity_time = round(sum([float(opacity_time), duration]), 8)

                secondpoint = ET.SubElement(animated, "waypoint")
                secondpoint.attrib["time"] = f"{opacity_time}s"
                secondpoint.attrib["before"] = "constant"
                secondpoint.attrib["after"] = "constant"
                real = ET.SubElement(secondpoint, "real")
                real.attrib["value"] = "0.0000000000"

runtime = int(opacity_time * float(root.attrib['fps']))
root.attrib['end-time'] = str(runtime) + "f"

tree.write(f"{animation}_edit.sif", encoding="UTF-8", xml_declaration=True)
