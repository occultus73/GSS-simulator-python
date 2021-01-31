from datetime import datetime

from data_loading.ActualFertilityDataLoader import ActualFertilityDataLoader
from data_loading.GSS_data_columns import gss_columns
from data_loading.IdealFertilityDataLoader import IdealFertilityDataLoader
from data_loading.SterileFertilityDataLoader import SterileFertilityDataLoader
from analysis.information import InformationProcessor
from analysis.meta_information import graph_sample_meta_information
from simulation.FertileSimulator import FertileSimulator
from simulation.SerileSimulator import SterileSimulator

GENERATIONS = {
    "Pre-Boomers": 1905,
    "Boomers": 1945,
    "GenX": 1965,
    "Millennials": 1981,
    "GenZ": 1996,
}


def run_simulation(trait_to_study, generation_name, minimum_year_of_birth):
    # Calculate time parameters
    starting_year = minimum_year_of_birth + 18
    doomsday = datetime.now().year + 50
    years = range(starting_year, doomsday)

    # Load samples
    actual_fertility_sample = ActualFertilityDataLoader(trait_to_study, minimum_year_of_birth).load_sample()
    ideal_fertility_sample = IdealFertilityDataLoader(trait_to_study, minimum_year_of_birth).load_sample()
    sterile_fertility_sample = SterileFertilityDataLoader(trait_to_study, minimum_year_of_birth).load_sample()

    # Skip trait_to_study on empty samples:
    if not sterile_fertility_sample:
        return

    # Setup simulators
    actual_fertility_simulator = FertileSimulator(starting_year, actual_fertility_sample)
    ideal_fertility_simulator = FertileSimulator(starting_year, ideal_fertility_sample)
    sterile_fertility_simulator = SterileSimulator(starting_year, sterile_fertility_sample)

    # Generate the results
    actual_fertility_results = [(year, actual_fertility_simulator.next_year()) for year in years]
    ideal_fertility_results = [(year, ideal_fertility_simulator.next_year()) for year in years]
    sterile_fertility_results = [(year, sterile_fertility_simulator.next_year()) for year in years]

    # Analyse the results
    max_trait_value = round(max([a.trait for a in sterile_fertility_sample]))
    min_trait_value = round(min([a.trait for a in sterile_fertility_sample]))

    InformationProcessor(trait_to_study, max_trait_value, min_trait_value,
                         f"output/{generation_name}/{trait_to_study}",
                         actual_fertility_results,
                         ideal_fertility_results,
                         sterile_fertility_results).process_results()

    graph_sample_meta_information(f"output/{generation_name}/{trait_to_study}/_Sample_Meta_Information",
                                  actual_fertility_results,
                                  ideal_fertility_results,
                                  sterile_fertility_results)


if __name__ == '__main__':
    for generation, min_year_of_birth in GENERATIONS.items():
        eligible_columns = [key for key, value in gss_columns.items() if 12 < value < 145]
        for eligible_column in eligible_columns:
            run_simulation(eligible_column, generation, min_year_of_birth)
