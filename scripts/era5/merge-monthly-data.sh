#!/bin/bash
module load cdo

echo "Merging single-level fields"
cdo -b F64 -mergetime ecfwf_$1-*.nc $1-ecfwf.nc
cdo -b F64 -mergetime eclwf_$1-*.nc $1-eclwf.nc
cdo -b F64 -mergetime ewvf_$1-*.nc $1-ewvf.nc
cdo -b F64 -mergetime ncfwf_$1-*.nc $1-ncfwf.nc
cdo -b F64 -mergetime nclwf_$1-*.nc $1-nclwf.nc
cdo -b F64 -mergetime nwvf_$1-*.nc $1-nwvf.nc
cdo -b F64 -mergetime sp_$1-*.nc $1-sp.nc
cdo -b F64 -mergetime tcwv_$1-*.nc $1-tcwv.nc
cdo -b F64 -mergetime tcw_$1-*.nc $1-tcw.nc
cdo -b F64 -mergetime tp_$1-*.nc $1-tp.nc
cdo -b F64 -mergetime e_$1-*.nc $1-e.nc

#echo "Merging pressure-level fields..."
#cdo -b F64 -mergetime uvq-$1-*.nc $1-uvq.nc
echo "Done...finally"
