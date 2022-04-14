import os
import random
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ElementTree, Element

#base_dir = input("Give me a filepath: ")

#if os.path.isdir(base_dir):
#    os.chdir(base_dir)

animation = input("Enter the base animation: ")
tree = ET.parse(animation)
root = tree.getroot()

opacity_time = 0
angle_time = 0


# Layer Adjustments
for layer in root.findall("layer"):
    for element in layer:
        duration = round(random.uniform(0, 0.2), 8)

        # Transformations
        if element.attrib["name"] == "transformation":
            for sublayer in element:
                for subelement in sublayer:
                    RND_OFFSET_X = round(random.uniform(-0.2, 0.2), 10)
                    RND_OFFSET_Y = round(random.uniform(-0.1, 0.1), 10)

                    # Angle Adjustments
                    if subelement.tag == "angle":
                        RND_ANGLE = round(random.uniform(-2, 2), 6)
                        subelement.clear()
                        animated = ET.SubElement(subelement, "animated")
                        animated.attrib["type"] = "angle"

                        startpoint = ET.SubElement(animated, "waypoint")
                        startpoint.attrib["time"] = "0s"
                        startpoint.attrib["before"] = "constant"
                        startpoint.attrib["after"] = "constant"
                        angle = ET.SubElement(startpoint, "angle")
                        angle.attrib["value"] = "0.000000"

                        if opacity_time != 0:
                            firstpoint = ET.SubElement(animated, "waypoint")
                            firstpoint.attrib["time"] = f"{round(opacity_time, 8)}"
                            firstpoint.attrib["before"] = "linear"
                            firstpoint.attrib["after"] = "linear"
                            angle = ET.SubElement(firstpoint, "angle")
                            angle.attrib["value"] = f"{RND_ANGLE}"

                        angle_time = round(sum([float(opacity_time), duration]), 8)

                        secondpoint = ET.SubElement(animated, "waypoint")
                        secondpoint.attrib["time"] = f"{round(angle_time, 8)}s"
                        secondpoint.attrib["before"] = "linear"
                        secondpoint.attrib["after"] = "linear"
                        angle = ET.SubElement(secondpoint, "angle")
                        angle.attrib["value"] = f"{RND_ANGLE}"

                    # Offset Adjustments
                    if subelement.tag == "offset":
                        subelement.clear()
                        animated = ET.SubElement(subelement, "animated")
                        animated.attrib["type"] = "vector"

                        startpoint = ET.SubElement(animated, "waypoint")
                        startpoint.attrib["time"] = "0s"
                        startpoint.attrib["before"] = "constant"
                        startpoint.attrib["after"] = "constant"
                        vector = ET.SubElement(startpoint, "vector")
                        x = ET.SubElement(vector, "x")
                        y = ET.SubElement(vector, "y")
                        x.text = '0.0000000000'
                        y.text = '0.0000000000'

                        if opacity_time != 0:
                            firstpoint = ET.SubElement(animated, "waypoint")
                            firstpoint.attrib["time"] = f"{round(opacity_time, 8)}"
                            firstpoint.attrib["before"] = "linear"
                            firstpoint.attrib["after"] = "linear"
                            vector = ET.SubElement(firstpoint, "vector")
                            x = ET.SubElement(vector, "x")
                            y = ET.SubElement(vector, "y")
                            x.text = '0.0000000000'
                            y.text = '0.0000000000'

                        vector_time = round(sum([float(opacity_time), duration]), 8)

                        secondpoint = ET.SubElement(animated, "waypoint")
                        secondpoint.attrib["time"] = f"{vector_time}s"
                        secondpoint.attrib["before"] = "linear"
                        secondpoint.attrib["after"] = "linear"
                        vector = ET.SubElement(secondpoint, "vector")
                        x = ET.SubElement(vector, "x")
                        y = ET.SubElement(vector, "y")
                        x.text = f"{RND_OFFSET_X}"
                        y.text = f"{RND_OFFSET_Y}"

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

tree.write("TEST_EDIT.sif", encoding="UTF-8", xml_declaration=True)