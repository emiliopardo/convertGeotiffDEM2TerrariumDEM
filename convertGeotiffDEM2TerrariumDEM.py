#!/usr/bin/python
# coding=utf-8

import rasterio
import numpy as np

np.seterr(all='ignore')

with rasterio.open('/home/epardo/Descargas/Datos_Granada/mdt_tif_granada/mdt_granada_3857_clip.tif') as src:
    dem = src.read(1)

    r = np.zeros(dem.shape)
    g = np.zeros(dem.shape)
    b = np.zeros(dem.shape)

    r += np.floor_divide((100000 + dem * 10), 65536)
    g += np.floor_divide((100000 + dem * 10), 256) - r * 256
    b += np.floor(100000 + dem * 10) - r * 65536 - g * 256

    # meta = src.meta
    # meta(driver='GTiff', dtype=rasterio.uint8,nodata=0,count=3)

    #with rasterio.open('/home/epardo/Descargas/Datos_Granada/mdt_3857/mdt_granada_epsg_3857_output.tif', 'w', **meta) as dst:
    with rasterio.open('/home/epardo/Descargas/Datos_Granada/mdt_tif_granada/mdt_granada_3857_clip_output.tif', 'w', transform=src.transform, driver='GTiff',  height=r.shape[0], width=r.shape[1] ,dtype=rasterio.uint8,nodata=0,count=3) as dst:    
        dst.write_band(1, r.astype(rasterio.uint8))
        dst.write_band(2, g.astype(rasterio.uint8))
        dst.write_band(3, b.astype(rasterio.uint8))
