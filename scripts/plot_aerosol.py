import xarray as xr
import matplotlib.pyplot as plt

da = xr.open_dataarray("data/aerosol.nc")

field = da.isel(time=-1, pfull=0)

plt.figure(figsize=(10,5))
field.plot()
plt.savefig("figures/aerosol_map.png")
print("aerosol_map.png created successfully")
