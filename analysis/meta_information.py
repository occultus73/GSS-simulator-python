import numpy as np

from analysis.graph_methods import graph_simulation_results


def graph_meta_info(directory, demographic, actual_results, ideal_results, sterile_results):
    graph_simulation_results(directory, f"Size of {demographic} Population", "Number of Americans",
                             [(year, len(year_pop)) for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, len(year_pop)) for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, len(year_pop)) for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average Year Born in {demographic} Population", "Year",
                             [(year, np.mean([a.year_born for a in year_pop]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.year_born for a in year_pop]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.year_born for a in year_pop]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average Age at Survey in {demographic} Population", "Age",
                             [(year, np.mean([a.surveyee_age for a in year_pop]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.surveyee_age for a in year_pop]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.surveyee_age for a in year_pop]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average Number of Children in {demographic} Population", "No. of Children",
                             [(year, np.mean([a.number_of_children for a in year_pop]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.number_of_children for a in year_pop]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             None)

    graph_simulation_results(directory, f"Average Age at Birth of First Child in {demographic} Population", "Age",
                             [(year, np.mean([a.age_at_first_child for a in year_pop if a.age_at_first_child != 0]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.age_at_first_child for a in year_pop if a.age_at_first_child != 0]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             None)

    graph_simulation_results(directory, f"Proportion Married in {demographic} Population", "% of Population 'Married'",
                             [(year, sum([1 for a in year_pop if a.marriage == "MARRIED"]) * 100 / len(year_pop))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, sum([1 for a in year_pop if a.marriage == "MARRIED"]) * 100 / len(year_pop))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, sum([1 for a in year_pop if a.marriage == "MARRIED"]) * 100 / len(year_pop))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    if "White" not in demographic and "Black" not in demographic:
        graph_simulation_results(directory, f"Proportion White in {demographic} Population", "% of Population",
                                 [(year, sum([1 for a in year_pop if a.race == 1]) * 100 / len(year_pop))
                                  for year, year_pop in actual_results if len(year_pop) > 100],
                                 [(year, sum([1 for a in year_pop if a.race == 1]) * 100 / len(year_pop))
                                  for year, year_pop in ideal_results if len(year_pop) > 100],
                                 [(year, sum([1 for a in year_pop if a.race == 1]) * 100 / len(year_pop))
                                  for year, year_pop in sterile_results if len(year_pop) > 100])

    if "Male" not in demographic and "Female" not in demographic:
        graph_simulation_results(directory, f"Proportion Male in {demographic} Population", "% of Population",
                                 [(year, sum([1 for a in year_pop if a.sex == 1]) * 100 / len(year_pop))
                                  for year, year_pop in actual_results if len(year_pop) > 100],
                                 [(year, sum([1 for a in year_pop if a.sex == 1]) * 100 / len(year_pop))
                                  for year, year_pop in ideal_results if len(year_pop) > 100],
                                 [(year, sum([1 for a in year_pop if a.sex == 1]) * 100 / len(year_pop))
                                  for year, year_pop in sterile_results if len(year_pop) > 100])
