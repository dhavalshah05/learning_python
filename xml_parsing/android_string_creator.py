from xml.dom import minidom

from android_string import AndroidString


class AndroidStringCreator:

    def __init__(self, file_name):
        self.file_name = file_name

    def generate_file(self, android_strings: list[AndroidString]):
        root = minidom.Document()
        xml = root.createElement("resources")
        root.appendChild(xml)

        for item in android_strings:
            el_string = root.createElement("string")
            el_string.setAttribute('name', item.key)

            el_value = root.createTextNode(item.value)
            el_string.appendChild(el_value)

            xml.appendChild(el_string)

        xml_str = root.toprettyxml(indent="\t")
        with open(self.file_name, "w") as f:
            f.write(xml_str)