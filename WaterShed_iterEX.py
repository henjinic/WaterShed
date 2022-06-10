# -*- coding: utf-8 -*-
"""
Created on Mon May  2 09:56:08 2022

@author: univSEOULGIS
"""
## 패키지 정리
from WBT.whitebox_tools import WhiteboxTools
from WaterShed import d8_flow_directions, d8_flow_accum, divide_watershed, find_stream_pour_point

wbt = WhiteboxTools()


## 데이터 이름 정리
NAME = "Min50ha_Srtm30"

RawDEM = r"D:\80_GISDATA\Korea_SRTM30.tif"
ModifiedDEM = r"D:\STRM_Ridge30\Breach_%s.tif" % (NAME)
DEM_FLT = r"D:\STRM_Ridge30\grid\Breach_%s.FLT" % (NAME)


## DEM 전처리
wbt.breach_depressions(
    RawDEM,
    ModifiedDEM,
    max_depth=None,
    max_length=None,
    flat_increment=None,
    fill_pits=False,
    )
arcpy.conversion.RasterToFloat(ModifiedDEM, DEM_FLT)


#### 유역도출프로세스  ####
##########################


# Options of Output (사용하지 않을 때 None으로 설정)
MIN_WATERSHED = 50
MIN_STREAM_DISTANCE = None

D8_FLT = r"D:\STRM_Ridge30\init\%s_d8.flt" % (NAME)
ACCUM_FLT = r"D:\STRM_Ridge30\init\%s_acccum.flt" % (NAME)
D8_PIT_SHP = r"D:\STRM_Ridge30\init\%s_d8_pit.shp" % (NAME)
OUTPUT = r"D:\STRM_Ridge30\output\%s" % (NAME)
OUTPUT_FLT = r"D:\STRM_Ridge30\output\%s.flt" % (NAME)


#### Initialization
d8_flow_directions(dem=DEM_FLT,
                   output=D8_FLT)

d8_flow_accum(dem=DEM_FLT,
              pourPoint=D8_PIT_SHP,
              output=ACCUM_FLT)

divide_watershed(dem=DEM_FLT,
                 pourPoint=D8_PIT_SHP,
                 d8=D8_FLT,
                 output=OUTPUT)

find_stream_pour_point(pourPoint=D8_PIT_SHP,
                       divide=r"D:\STRM_Ridge30\output\%s_div_0.flt" % (NAME),
                       d8=D8_FLT,
                       accum=ACCUM_FLT,
                       output=OUTPUT_FLT,
                       minWatershed=MIN_WATERSHED,
                       minStreamDistance=MIN_STREAM_DISTANCE)


#### Iteration
for i in range(1, 4):
    divide_watershed(dem=DEM_FLT,
                     pourPoint=r"D:\STRM_Ridge30\output\%s_pp_%d.shp" % (NAME, i),
                     d8=D8_FLT,
                     pourPointCalcAccum=True if i == 1 else False, # 첫 번째 iteration에서 True, 나머지 False
                     accum=ACCUM_FLT,
                     output=OUTPUT)

    find_stream_pour_point(pourPoint=r"D:\STRM_Ridge30\output\%s_pp_%d.shp" % (NAME, i),
                           prevMainStream=r"D:\STRM_Ridge30\output\%s_st_%d.flt" % (NAME, i - 1),
                           divide=r"D:\STRM_Ridge30\output\%s_div_%d.flt" % (NAME, i),
                           accum=ACCUM_FLT,
                           d8=D8_FLT,
                           nearPourPoint=True,
                           skipCurPourPoint=True,
                           output=OUTPUT_FLT,
                           minWatershed=MIN_WATERSHED,
                           minStreamDistance=MIN_STREAM_DISTANCE)
