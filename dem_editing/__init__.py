# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DEMediting
                                 A QGIS plugin
 The plugin edits parts of DEM interactively
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-02-07
        copyright            : (C) 2022 by Anastasia Igitova, Timofey Samsonov
        email                : nigitova2000@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load DEMediting class from file DEMediting.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .DEM_editing import DEMediting
    return DEMediting(iface)
