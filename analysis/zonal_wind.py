import xarray as xr
import matplotlib.pyplot as plt

INPUT_FILE = /home/blatc/isca_data/neptune_demo/run0012/atmos_monthly.nc
ds = xr.open_dataset(INPUT_FILE)

u = ds.ucomp

u.mean(("time","lon")).plot()

plt.title("Neptune Zonal Wind")
plt.savefig("figures/zonal_wind.png")
