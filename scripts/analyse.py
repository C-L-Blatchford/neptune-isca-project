import xarray as xr
import matplotlib.pyplot as plt

# Replace OUTPUT_FILE with any actual file name
OUTPUT_FILE = "/home/blatc/isca_data/neptune_demo/run0012/atmos_monthly.nc"

ds = xr.open_dataset(OUTPUT_FILE)

print(ds)
print(ds.data_vars)

temp = ds["temp"].isel(time=-1)

plt.figure(figsize=(8,4))
temp.mean("lon").plot()

plt.title("Zonal Mean Temperature")
plt.savefig("figures/zonal_temperature.png", dpi=300)

print("Saved figure successfully")


