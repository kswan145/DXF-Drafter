import re
import xml.etree.ElementTree as ET
with open('Version 3.43.fxl', 'r') as file:
    codelist = file.read()

code = codelist.split()
    # Filter the words to those that start with "Name="
layer_words = [word for word in code if word.startswith("Layer=")]


# This removes the word layer, layer=0 and the double quotes around the words
new_list = [s.replace('Layer="0"', '').replace('Layer=', '').replace('"', '') for s in layer_words]

# This removes the empty strings located within new_list
code_layers = [element for element in new_list if element != '']

# This below removes the duplicated layers
layers = list(set(code_layers))

# This below filters down all the codes
code_words = [word for word in code if word.startswith("Code=")]

controller_codes = [s.replace('Code="0"', '').replace('Code=', '').replace('"', '') for s in code_words]

#print(codelist)

# Use a regular expression to find all the text between the <LayerDefinitions> tag
layer_definition_pattern = re.compile(r'<LayerDefinitions>(.*?)</LayerDefinitions>', re.DOTALL)
layerDefinitions = re.findall(layer_definition_pattern, codelist)

# Print the matches
#for layerDefinition in layerDefinitions:
    #print(layerDefinition)

# Define the XML data as a string
layer_property_pattern = '<LayerDefinition><Name>Z-GRID</Name><Color>FFFF00FF</Color><LineStyleName>CENTER</LineStyleName><LineWeight>0</LineWeight><ProtectLayer>false</ProtectLayer><LayerGroup>&lt;&lt;None&gt;&gt;</LayerGroup><DisplayPriority>64</DisplayPriority><Print>true</Print></LayerDefinition>'

# Parse the XML data into an ElementTree object
root = ET.fromstring(layer_property_pattern)

# Create an empty dictionary
layer_dict = {}

# Loop through each child element of the root element and extract the text
for child in root:
    key = child.tag
    value = child.text
    layer_dict[key] = value

print(layer_dict)




# TODO Add a list of the codes that represent each layer and then assign layers to codes