import numpy as np
from os.path import join
import cdsapi

'''
Script to download single-level ERA5 data from copernicus server. Server only allows one month of data to be downloaded at a time, so script loops through months requested.

TIMES: native resolution is hourly; change PERIOD to download at different interval
DAYS:  days of the month to download
MONTHS:months to download
YEARS: years to download  (available 1979-present)
VARIABLES: names of variables to retrieve (see https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview for a full list of variable names)
GRID : horizontal resolution of data, in degrees (native resolution is [.25,.25])
AREA : lat/lon boundaries in format of [max_lat, min_lon, min_lat, max_lon] (longitude is in [-180,180])
OUT_FNAME: prefix to the newly created file
SAVE_PATH: directory to save data in
'''

c = cdsapi.Client()

PERIOD = 3 # time interval in hours
TIMES  = [f'{i:02d}:00' for i in np.arange(0,24, PERIOD)]
DAYS   = [f'{i:02d}'    for i in np.arange(1,32)]
MONTHS = [f'{i:02d}'    for i in np.arange(12,0,-1)]
YEARS  = [f'{i:04d}'    for i in np.arange(1979,2021,1)]
GRID   = [1.,1.]
AREA   = [90, -180, -90, 180]

#VARIABLES = ['surface_pressure']
VARIABLES = ['10m_u_component_of_wind', '10m_v_component_of_wind']
#OUT_FNAME = 'sp'
OUT_FNAME = 'uv10m'

SAVE_PATH = '/vortexfs1/share/clidex/data/reanalysis/era5/single-levels'

for year in YEARS:
    for month in MONTHS:
        c.retrieve(
            'reanalysis-era5-single-levels',
            {
                'product_type': 'reanalysis',
                'format'      : 'netcdf',
                'variable'    : VARIABLES,
                'time'        : TIMES,
                'day'         : DAYS,
                'month'       : month,
                'year'        : year,
                'grid'        : GRID,
                'area'        : AREA
            },
            join(SAVE_PATH, f'{OUT_FNAME}_{year}-{month}.nc'))
