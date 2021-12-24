import xml.etree.ElementTree as ET
import string

from layout_counter import LayoutCounter


class LayoutParser:

    def __init__(self, file_path: string, counter: LayoutCounter):
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
        if "ConstraintLayout" in tag:
            self.counter.increment_constraint_layout_count()
        elif "RecyclerView" in tag:
            self.counter.increment_recycler_view_count()
