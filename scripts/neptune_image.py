import xarray as xr
import matplotlib.pyplot as plt

da = xr.open_dataarray("data/aerosol.nc")

field = da.isel(time=-1,pfull=0)

plt.figure(figsize=(6,6))
plt.imshow(field)
plt.axis("off")
plt.savefig("figures/neptune_synthetic.png", bbox_inches="tight")
