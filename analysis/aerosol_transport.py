import xarray as xr
import numpy as np

INPUT_FILE = /home/blatc/isca_data/neptune_demo/run0012/atmos_monthly.nc
ds = xr.open_dataset(INPUT_FILE)

temp = ds.temp

omega = ds.omega

temp_norm = (temp.max()-temp)/(temp.max()-temp.min())

omega_norm = (-omega-(-omega).min())/((-omega).max()-(-omega).min())

aerosol = temp_norm * omega_norm

aerosol.to_netcdf("aerosol.nc")
