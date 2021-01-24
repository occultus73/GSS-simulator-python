from datetime import datetime

from business.FertileSimulator import FertileSimulator
from business.SerileSimulator import SterileSimulator
from data.ActualFertilityDataLoader import ActualFertilityDataLoader
from data.IdealFertilityDataLoader import IdealFertilityDataLoader
from data.SterileFertilityDataLoader import SterileFertilityDataLoader

TRAIT_TO_STUDY = "CONSERVATIVE"
MIN_YEAR_OF_BIRTH = 1965
STARTING_YEAR = 1983
DOOMSDAY = datetime.now().year + 50

if __name__ == '__main__':
    # Load samples
    actual_fertility_sample = ActualFertilityDataLoader(TRAIT_TO_STUDY, MIN_YEAR_OF_BIRTH).load_sample()
    ideal_fertility_sample = IdealFertilityDataLoader(TRAIT_TO_STUDY, MIN_YEAR_OF_BIRTH).load_sample()
    sterile_fertility_sample = SterileFertilityDataLoader(TRAIT_TO_STUDY, MIN_YEAR_OF_BIRTH).load_sample()

    # Setup simulators
    actual_fertility_simulator = FertileSimulator(STARTING_YEAR, actual_fertility_sample)
    ideal_fertility_simulator = FertileSimulator(STARTING_YEAR, ideal_fertility_sample)
    sterile_fertility_simulator = SterileSimulator(STARTING_YEAR, sterile_fertility_sample)

    # Loop through results
    for year in range(STARTING_YEAR, DOOMSDAY):
        print("YEAR: ", year)
        print(actual_fertility_simulator.next_year().__len__())
        print(ideal_fertility_simulator.next_year().__len__())
        print(sterile_fertility_simulator.next_year().__len__())
