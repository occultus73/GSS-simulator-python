import numpy as np


def get_segregated_populations(actual_results, ideal_results, sterile_results):
    actual_white_population = [(year, [a for a in year_pop if a.race == 1])
                               for year, year_pop in actual_results if len(year_pop) > 100]
    ideal_white_population = [(year, [a for a in year_pop if a.race == 1])
                              for year, year_pop in ideal_results if len(year_pop) > 100]
    sterile_white_population = [(year, [a for a in year_pop if a.race == 1])
                                for year, year_pop in sterile_results if len(year_pop) > 100]

    actual_black_population = [(year, [a for a in year_pop if a.race == 2])
                               for year, year_pop in actual_results if len(year_pop) > 100]
    ideal_black_population = [(year, [a for a in year_pop if a.race == 2])
                              for year, year_pop in ideal_results if len(year_pop) > 100]
    sterile_black_population = [(year, [a for a in year_pop if a.race == 2])
                                for year, year_pop in sterile_results if len(year_pop) > 100]

    actual_male_population = [(year, [a for a in year_pop if a.sex == 1])
                              for year, year_pop in actual_results if len(year_pop) > 100]
    ideal_male_population = [(year, [a for a in year_pop if a.sex == 1])
                             for year, year_pop in ideal_results if len(year_pop) > 100]
    sterile_male_population = [(year, [a for a in year_pop if a.sex == 1])
                               for year, year_pop in sterile_results if len(year_pop) > 100]

    actual_female_population = [(year, [a for a in year_pop if a.sex == 2])
                                for year, year_pop in actual_results if len(year_pop) > 100]
    ideal_female_population = [(year, [a for a in year_pop if a.sex == 2])
                               for year, year_pop in ideal_results if len(year_pop) > 100]
    sterile_female_population = [(year, [a for a in year_pop if a.sex == 2])
                                 for year, year_pop in sterile_results if len(year_pop) > 100]

    actual_white_male_population = [(year, [a for a in year_pop if a.sex == 1])
                                    for year, year_pop in actual_white_population if len(year_pop) > 100]
    ideal_white_male_population = [(year, [a for a in year_pop if a.sex == 1])
                                   for year, year_pop in ideal_white_population if len(year_pop) > 100]
    sterile_white_male_population = [(year, [a for a in year_pop if a.sex == 1])
                                     for year, year_pop in sterile_white_population if len(year_pop) > 100]

    actual_white_female_population = [(year, [a for a in year_pop if a.sex == 2])
                                      for year, year_pop in actual_white_population if len(year_pop) > 100]
    ideal_white_female_population = [(year, [a for a in year_pop if a.sex == 2])
                                     for year, year_pop in ideal_white_population if len(year_pop) > 100]
    sterile_white_female_population = [(year, [a for a in year_pop if a.sex == 2])
                                       for year, year_pop in sterile_white_population if len(year_pop) > 100]

    actual_black_male_population = [(year, [a for a in year_pop if a.sex == 1])
                                    for year, year_pop in actual_black_population if len(year_pop) > 100]
    ideal_black_male_population = [(year, [a for a in year_pop if a.sex == 1])
                                   for year, year_pop in ideal_black_population if len(year_pop) > 100]
    sterile_black_male_population = [(year, [a for a in year_pop if a.sex == 1])
                                     for year, year_pop in sterile_black_population if len(year_pop) > 100]

    actual_black_female_population = [(year, [a for a in year_pop if a.sex == 2])
                                      for year, year_pop in actual_black_population if len(year_pop) > 100]
    ideal_black_female_population = [(year, [a for a in year_pop if a.sex == 2])
                                     for year, year_pop in ideal_black_population if len(year_pop) > 100]
    sterile_black_female_population = [(year, [a for a in year_pop if a.sex == 2])
                                       for year, year_pop in sterile_black_population if len(year_pop) > 100]
    
    return {
        "actual_Whole_Population": actual_results,
        "actual_White_Population": actual_white_population,
        "actual_Black_Population": actual_black_population,
        "actual_Male_Population": actual_male_population,
        "actual_Female_Population": actual_female_population,
        "actual_White_Male_Population": actual_white_male_population,
        "actual_White_Female_Population": actual_white_female_population,
        "actual_Black_Male_Population": actual_black_male_population,
        "actual_Black_Female_Population": actual_black_female_population,

        "ideal_Whole_Population": ideal_results,
        "ideal_White_Population": ideal_white_population,
        "ideal_Black_Population": ideal_black_population,
        "ideal_Male_Population": ideal_male_population,
        "ideal_Female_Population": ideal_female_population,
        "ideal_White_Male_Population": ideal_white_male_population,
        "ideal_White_Female_Population": ideal_white_female_population,
        "ideal_Black_Male_Population": ideal_black_male_population,
        "ideal_Black_Female_Population": ideal_black_female_population,

        "sterile_Whole_Population": sterile_results,
        "sterile_White_Population": sterile_white_population,
        "sterile_Black_Population": sterile_black_population,
        "sterile_Male_Population": sterile_male_population,
        "sterile_Female_Population": sterile_female_population,
        "sterile_White_Male_Population": sterile_white_male_population,
        "sterile_White_Female_Population": sterile_white_female_population,
        "sterile_Black_Male_Population": sterile_black_male_population,
        "sterile_Black_Female_Population": sterile_black_female_population
    }
