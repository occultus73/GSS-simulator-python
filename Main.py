from datetime import datetime

from business.FertileSimulator import FertileSimulator
from business.SerileSimulator import SterileSimulator
from data.ActualFertilityDataLoader import ActualFertilityDataLoader
from data.IdealFertilityDataLoader import IdealFertilityDataLoader
from data.SterileFertilityDataLoader import SterileFertilityDataLoader
from meta_information import graph_sample_meta_information

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
    actual_fertility_results = [(year, actual_fertility_simulator.next_year()) for year in years]
    ideal_fertility_results = [(year, ideal_fertility_simulator.next_year()) for year in years]
    sterile_fertility_results = [(year, sterile_fertility_simulator.next_year()) for year in years]

    # Analyse the results
    graph_sample_meta_information(f"output-{MIN_YEAR_OF_BIRTH}/{TRAIT_TO_STUDY}/sample_meta_information",
                                  actual_fertility_results,
                                  ideal_fertility_results,
                                  sterile_fertility_results)
