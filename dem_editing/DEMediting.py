from qgis.PyQt.QtCore import QRectF
from qgis.core import QgsRasterLayer, QgsProject, QgsRectangule, QgsRasteBlock, QgsRasterPipe
from qgis.gui import QgsLayerTreeView, QgsMapToolEmitPoint
import math

def __init__(self, layer, uc=None, debug=False):
    self.layer = layer
    self.provider = layer.dataProvider()
    self.pixsize = self.layer.rasterUnitsPerPixelX()
    self.raster_cols = self.layer.width()
    self.raster_rows = self.layer.height()
    self.min_x = self.layer_extent.xMinimum()
    self.min_y = self.layer_extent.yMinimum()
    self.max_x = self.layer_extent.xMaximum()
    self.max_y = self.layer_extent.yMaximum()


def canvasMoveEvent(self, event):
    x = event.pos().x()
    y = event.pos().y()
    point = self.canvas.getCoordinateTransform().toMapCoordinates(x, y)
    return point

def onValueChanged(self, newValue):
    self.value = newValue
    return

def applyValue(self, value, radius):
    canvas = iface.mapCanvas()
    pointTool = QgsMapToolEmitPoint(canvas) #?

    pointTool.canvasClicked.connect(canvasMoveEvent)

    canvas.setMapTool(pointTool)

    # get index
    row = math.floor((self.pointTool.y() - self.min_y)/self.pixsize)
    col = math.floor((self.pointTool.x() - self.min_x)/self.pixsize)

    pixel_x_max = row * self.pixsize
    pixel_x_min = (row - 1) * self.pixsize
    pixel_y_max = col * self.pixsize
    pixel_y_min = (col - 1) * self.pixsize

    block_x_max = pixel_x_max + radius * self.pixsize
    block_x_min = pixel_x_min - radius * self.pixsize
    block_y_max = pixel_y_max + radius * self.pixsize
    block_y_min = pixel_y_min - radius * self.pixsize

    value = self.

    block_box = QgsRectangule(block_x_min, block_y_min, block_x_max, block_y_max)
    block = self.provider.block(1, block_box, 1, 1)
    self.provider.setEditable(True)
    block.setValue(row, col, value)

    self.provider.writeBlock(block, 1)












