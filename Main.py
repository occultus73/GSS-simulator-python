from datetime import datetime

import matplotlib.pyplot as plt

from business.FertileSimulator import FertileSimulator
from business.SerileSimulator import SterileSimulator
from data.ActualFertilityDataLoader import ActualFertilityDataLoader
from data.IdealFertilityDataLoader import IdealFertilityDataLoader
from data.SterileFertilityDataLoader import SterileFertilityDataLoader

TRAIT_TO_STUDY = "CONSERVATIVE"
MIN_YEAR_OF_BIRTH = 1965
STARTING_YEAR = MIN_YEAR_OF_BIRTH + 18
DOOMSDAY = datetime.now().year + 50

years = range(STARTING_YEAR, DOOMSDAY)

if __name__ == '__main__':
    # Load samples
    actual_fertility_sample = ActualFertilityDataLoader(TRAIT_TO_STUDY, MIN_YEAR_OF_BIRTH).load_sample()
    ideal_fertility_sample = IdealFertilityDataLoader(TRAIT_TO_STUDY, MIN_YEAR_OF_BIRTH).load_sample()
    sterile_fertility_sample = SterileFertilityDataLoader(TRAIT_TO_STUDY, MIN_YEAR_OF_BIRTH).load_sample()

    # Setup simulators
    actual_fertility_simulator = FertileSimulator(STARTING_YEAR, actual_fertility_sample)
    ideal_fertility_simulator = FertileSimulator(STARTING_YEAR, ideal_fertility_sample)
    sterile_fertility_simulator = SterileSimulator(STARTING_YEAR, sterile_fertility_sample)

    # Generate the results
    actual_fertility_results = [actual_fertility_simulator.next_year() for year in years]
    ideal_fertility_results = [ideal_fertility_simulator.next_year() for year in years]
    sterile_fertility_results = [sterile_fertility_simulator.next_year() for year in years]

    # Analyse the data
    actual_fertility_population_size = [pop_year.__len__() for pop_year in actual_fertility_results]
    ideal_fertility_population_size = [pop_year.__len__() for pop_year in ideal_fertility_results]
    sterile_fertility_population_size = [pop_year.__len__() for pop_year in sterile_fertility_results]

    # Plot the data
    plt.plot(years, actual_fertility_population_size, label="Actual")
    plt.plot(years, ideal_fertility_population_size, label="Ideal")
    plt.plot(years, sterile_fertility_population_size, label="Sterile")
    plt.xlabel("Years")
    plt.ylabel("Number Of Americans")
    plt.title("Simulation Population Growth")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("output/Simulation_Populations.png")
    plt.close()
