"""
Scientific Python Visualization
-------------------------------
A beginner-friendly example of creating and saving scientific plots
from synthetic (illustrative) atmospheric data.

The data in this script are synthetic and are not real solar observations
or radiative MHD simulation outputs.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = Path("figures")
OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    # Create a synthetic height grid (km) and illustrative physical profiles.
    height_km = np.linspace(0, 5_000, 250)
    temperature_k = 4_500 + 4_000 * (1 - np.exp(-height_km / 1_800))
    density_relative = np.exp(-height_km / 1_100)
    vertical_velocity_kms = 8 * np.sin(height_km / 650) * np.exp(-height_km / 5_500)

    # Plot 1: temperature versus height.
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(height_km, temperature_k, linewidth=2)
    ax.set_xlabel("Height (km)")
    ax.set_ylabel("Illustrative temperature (K)")
    ax.set_title("Synthetic Atmospheric Temperature Profile")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "temperature_profile.png", dpi=180)
    plt.close(fig)

    # Plot 2: relative density versus height on a logarithmic x-axis.
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(density_relative, height_km, linewidth=2)
    ax.set_xscale("log")
    ax.set_xlabel("Relative density (arbitrary units)")
    ax.set_ylabel("Height (km)")
    ax.set_title("Synthetic Relative Density Profile")
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "density_profile.png", dpi=180)
    plt.close(fig)

    # Plot 3: illustrative vertical velocity versus height.
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(vertical_velocity_kms, height_km, linewidth=2)
    ax.axvline(0, linewidth=1, alpha=0.5)
    ax.set_xlabel("Illustrative vertical velocity (km/s)")
    ax.set_ylabel("Height (km)")
    ax.set_title("Synthetic Vertical Velocity Profile")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUTPUT_DIR / "velocity_profile.png", dpi=180)
    plt.close(fig)

    print(f"Plots saved in: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
