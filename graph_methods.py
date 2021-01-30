import os

import matplotlib.pyplot as plt


def graph_simulation_results(directory, name, unit, actual_data, ideal_data, sterile_data):

    # Plot Data
    if actual_data:
        actual_x, actual_y = zip(*actual_data)
        plt.plot(actual_x, actual_y, label="Actual")
    if ideal_data:
        ideal_x, ideal_y = zip(*ideal_data)
        plt.plot(ideal_x, ideal_y, label="Ideal")
    if sterile_data:
        sterile_x, sterile_y = zip(*sterile_data)
        plt.plot(sterile_x, sterile_y, label="Sterile")

    # Configure Graph
    plt.xlabel("Years")
    plt.ylabel(unit)
    plt.title(name)
    plt.legend(title="Fertility")
    plt.grid(True)
    plt.tight_layout()

    # Save and Close
    if not os.path.exists(directory):
        os.makedirs(directory)
    plt.savefig(f"{directory}/{name}.png")
    plt.close()
