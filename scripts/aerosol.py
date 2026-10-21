import xarray as xr
import numpy as np

OUTPUT_FILE = "/home/blatc/isca_data/neptune_demo/run0012/atmos_monthly.nc"
ds = xr.open_dataset(OUTPUT_FILE)
print(ds)

temp = ds["temp"]

aerosol = np.exp(-(temp-temp.min())/(temp.max()-temp.min()))

aerosol.to_netcdf("data/aerosol.nc")
print("aerosol.nc created successfully")
