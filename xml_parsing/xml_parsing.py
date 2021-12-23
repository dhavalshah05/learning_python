from android_string_parser import AndroidStringParser
from android_string_creator import AndroidStringCreator

# Reading key and values from xml
parser = AndroidStringParser(file_name='strings.xml')
android_strings = parser.read_android_strings()


creator = AndroidStringCreator(file_name='strings_generated.xml')
creator.generate_file(android_strings)




