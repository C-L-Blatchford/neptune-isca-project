import xarray as xr
import matplotlib.pyplot as plt

da = xr.open_dataarray("data/aerosol.nc")

field = da.isel(time=-1, pfull=0)

plt.figure(figsize=(8,4))

plt.imshow(field, cmap="Blues", origin="lower")

plt.axis("off")

plt.savefig("figures/neptune_observation.png", bbox_inches="tight")

print("Saved: figures/neptune_observation.png")
