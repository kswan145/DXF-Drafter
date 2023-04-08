import ezdxf
import csv
from fxl_file import layers

with open('ucad.csv', newline='') as csvfile:
    data = csv.reader(csvfile)
    rows = [row for row in data]

doc = ezdxf.new(dxfversion='R2010')
msp = doc.modelspace()

for i in range(len(rows) - 1):
    x1, y1, z1 = float(rows[i][1]), float(rows[i][2]), float(rows[i][3])
    x2, y2, z2 = float(rows[i + 1][1]), float(rows[i + 1][2]), float(rows[i + 1][3])
    line = msp.add_line((x1, y1, z1), (x2, y2, z2), dxfattribs={'color': 1})

    for row in rows:
        if row[4] == 'UCAD':
            line.set_dxf_attrib('layer', 'CABLE TV')
        else:
            layer_name = 'Unknown'

# This adds the layers to the dxf file
for layer in layers:
    doc.layers.add(layer)

doc.saveas('test2.dxf')




#TODO Now need to say that only draw lines for the same code i.e. UCAD, UCAD1 etc.


