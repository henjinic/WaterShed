# -*- coding: utf-8 -*-
import subprocess


D8FD_PATH = r"D:\STRM_Ridge30\bin\D8FlowDirections.exe"
D8FA_PATH = r"D:\STRM_Ridge30\bin\D8FlowAccum.exe"
DW_PATH = r"D:\STRM_Ridge30\bin\DivideWatershed.exe"
FSPP_PATH = r"D:\STRM_Ridge30\bin\FindStreamPourPoint.exe"


def d8_flow_directions(**kwargs):
    """### parameters
    * dem: path
    * output: path
    """
    command = [D8FD_PATH] + kwargs_to_command(kwargs)
    subprocess.run(command)


def d8_flow_accum(**kwargs):
    """accum Map 파일 생성
    ### parameters
    * dem: path
    * pourPoint: path
    * output: path
    """
    command = [D8FA_PATH] + kwargs_to_command(kwargs)
    subprocess.run(command)


def divide_watershed(**kwargs):
    """div, rid, peak, WS(Watershed)
    ### parameters
    * dem: path
    * pourPoint: path
    * d8: path
    * pourPointCalcAccum: bool
    * accum: path
    * output: path
    """
    command = [DW_PATH] + kwargs_to_command(kwargs)
    subprocess.run(command)


def find_stream_pour_point(**kwargs):
    """flow, PP(내부 집수점) ,hp(highpoint), Ep(EndPoint), 생성
    ### parameters
    * pourPoint: path (전 단계 PourPoint)
    * prevMainStream: path (전 단계 st)
    * divide: path (이번 divide 바로 앞에서 나온 거)
    * d8: path
    * accum: path
    * nearPourPoint: bool
    * skipCurPourPoint: bool
    * output: path
    * minWatershed: int
    * minStreamDistance: int
    """
    command = [FSPP_PATH] + kwargs_to_command(kwargs)
    subprocess.run(command)


def kwargs_to_command(kwargs):
    result = []
    for param, arg in kwargs.items():
        if not arg:
            continue

        if isinstance(arg, bool):
            arg = str(arg).lower()
        else:
            arg = str(arg)
        result += ["-" + param, arg]
    return result
