from datetime import datetime

from data_loading.ActualFertilityDataLoader import ActualFertilityDataLoader
from data_loading.IdealFertilityDataLoader import IdealFertilityDataLoader
from data_loading.SterileFertilityDataLoader import SterileFertilityDataLoader
from information import InformationProcessor
from meta_information import graph_sample_meta_information
from simulation.FertileSimulator import FertileSimulator
from simulation.SerileSimulator import SterileSimulator

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
    max_trait_value = int(max([a.trait for a in sterile_fertility_sample]))
    min_trait_value = int(min([a.trait for a in sterile_fertility_sample]))

    InformationProcessor(TRAIT_TO_STUDY, max_trait_value, min_trait_value,
                         f"output/{MIN_YEAR_OF_BIRTH}/{TRAIT_TO_STUDY}",
                         actual_fertility_results,
                         ideal_fertility_results,
                         sterile_fertility_results).process_results()

    graph_sample_meta_information(f"output/{MIN_YEAR_OF_BIRTH}/{TRAIT_TO_STUDY}/sample_meta_information",
                                  actual_fertility_results,
                                  ideal_fertility_results,
                                  sterile_fertility_results)
