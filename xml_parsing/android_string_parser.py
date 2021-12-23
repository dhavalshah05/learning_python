import xml.etree.ElementTree as ET

from android_string import AndroidString


class AndroidStringParser:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_android_strings(self) -> list[AndroidString]:
        android_strings = []

        with open(self.file_name, mode="r") as file:
            xml_data = file.read()
            root = ET.XML(xml_data)
            for item in root:
                android_strings.append(AndroidString(key=item.attrib['name'], value=item.text))

        return android_strings
