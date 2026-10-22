import xarray as xr
import matplotlib.pyplot as plt

ds = xr.open_dataarray("/home/blatc/Projects/neptune_isca/data/aerosol.nc")

field = ds.mean("lon")

field.plot()

plt.title("Mean Aerosol Distribution")
plt.savefig("figures/aerosol_transport.png")
