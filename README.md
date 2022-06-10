# WaterShed
This repository contains a python module which wraps the watershed calculation programs and an example script to which user can refer. This programs were jointly written by Kim Hyeonjin and Chio Jaeyeon of University of Seoul.
## Getting started
1. Prepare the watershed calculation programs below.
    * D8FlowAccum.exe
    * D8FlowDirections.exe
    * DivideWatershed.exe
    * FindStreamPourPoint.exe
2. Download `WaterShed.py`. Replace the values of the variables in `WaterShed.py` with the appropriate paths.
    ```py
    D8FD_PATH = r"\path\to\D8FlowDirections.exe"
    D8FA_PATH = r"\path\to\D8FlowAccum.exe"
    DW_PATH = r"\path\to\DivideWatershed.exe"
    FSPP_PATH = r"\path\to\FindStreamPourPoint.exe"
    ```
3. Import the module in a new script.
    ```py
    import WaterShed
    ```
## Usage
Refer to the `WaterShed_iterEx.py`.
