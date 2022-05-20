buffer = iface.activeLayer().selectedFeatures()[0].geometry().buffer(371.1188967223843065, 2)
iface.activeLayer().setGeometry(buffer)
