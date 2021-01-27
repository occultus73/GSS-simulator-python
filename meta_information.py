import numpy as np

from graph_methods import graph_simulation_results


def graph_sample_meta_information(directory, actual_results, ideal_results, sterile_results):
    graph_simulation_results(directory, "Population Size", "Number of Americans",
                             [(year, len(year_pop)) for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, len(year_pop)) for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, len(year_pop)) for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, "Average Year Born", "Year",
                             [(year, np.mean([a.year_born for a in year_pop]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.year_born for a in year_pop]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.year_born for a in year_pop]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, "Average Age at Survey", "Age",
                             [(year, np.mean([a.age_at_survey for a in year_pop]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.age_at_survey for a in year_pop]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.age_at_survey for a in year_pop]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, "Average Number of Children", "No. of Children",
                             [(year, np.mean([a.number_of_children for a in year_pop]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.number_of_children for a in year_pop]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             None)

    graph_simulation_results(directory, "Average Age at Birth of First Child", "Age",
                             [(year, np.mean([a.age_at_first_child for a in year_pop if a.age_at_first_child != 0]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.age_at_first_child for a in year_pop if a.age_at_first_child != 0]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             None)

    graph_simulation_results(directory, "Average IQ", "IQ",
                             [(year, np.mean([a.iq for a in year_pop]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.iq for a in year_pop]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.iq for a in year_pop]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, "Proportion White", "% of Population",
                             [(year, sum([1 for a in year_pop if a.race == 1]) * 100 / len(year_pop))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, sum([1 for a in year_pop if a.race == 1]) * 100 / len(year_pop))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, sum([1 for a in year_pop if a.race == 1]) * 100 / len(year_pop))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, "Proportion Male", "% of Population",
                             [(year, sum([1 for a in year_pop if a.sex == 1]) * 100 / len(year_pop))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, sum([1 for a in year_pop if a.sex == 1]) * 100 / len(year_pop))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, sum([1 for a in year_pop if a.sex == 1]) * 100 / len(year_pop))
                              for year, year_pop in sterile_results if len(year_pop) > 100])
