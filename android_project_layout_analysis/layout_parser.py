import xml.etree.ElementTree as ET
import string


class LayoutParser:

    def __init__(self, file_path: string, counter: dict):
        self.counter = counter
        with open(file_path, mode="r") as xml_file:
            xml_data = xml_file.read()
            root = ET.XML(xml_data)

            self.increment_counter(tag=root.tag)
            self.parse(root)

    def parse(self, root: ET.Element):
        for item in root:
            self.increment_counter(tag=item.tag)
            self.parse(item)

    def increment_counter(self, tag: string):
        content = tag.split(".")
        key = content[len(content) - 1]

        if key in self.counter.keys():
            self.counter[key] += 1
        else:
            self.counter[key] = 1
