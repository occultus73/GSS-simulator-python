import numpy as np

from graph_methods import graph_simulation_results


def graph_sample_information(trait, max_trait, min_trait, directory, actual_results, ideal_results, sterile_results):
    graph_simulation_results(directory, f"Average {trait}", f"Score ({min_trait}-{max_trait})",
                             [(year, np.mean([a.trait for a in year_pop]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average {trait}, Whites", f"Score ({min_trait}-{max_trait})",
                             [(year, np.mean([a.trait for a in year_pop if a.race == 1]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 1]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 1]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average {trait}, Blacks", f"Score ({min_trait}-{max_trait})",
                             [(year, np.mean([a.trait for a in year_pop if a.race == 2]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 2]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 2]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average {trait}, Males", f"Score ({min_trait}-{max_trait})",
                             [(year, np.mean([a.trait for a in year_pop if a.sex == 1]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.sex == 1]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.sex == 1]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average {trait}, Females", f"Score ({min_trait}-{max_trait})",
                             [(year, np.mean([a.trait for a in year_pop if a.sex == 2]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.sex == 2]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.sex == 2]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average {trait}, White Males", f"Score ({min_trait}-{max_trait})",
                             [(year, np.mean([a.trait for a in year_pop if a.race == 1 and a.sex == 1]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 1 and a.sex == 1]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 1 and a.sex == 1]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average {trait}, White Females", f"Score ({min_trait}-{max_trait})",
                             [(year, np.mean([a.trait for a in year_pop if a.race == 1 and a.sex == 2]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 1 and a.sex == 2]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 1 and a.sex == 2]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average {trait}, Black Males", f"Score ({min_trait}-{max_trait})",
                             [(year, np.mean([a.trait for a in year_pop if a.race == 2 and a.sex == 1]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 2 and a.sex == 1]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 2 and a.sex == 1]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])

    graph_simulation_results(directory, f"Average {trait}, Black Females", f"Score ({min_trait}-{max_trait})",
                             [(year, np.mean([a.trait for a in year_pop if a.race == 2 and a.sex == 2]))
                              for year, year_pop in actual_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 2 and a.sex == 2]))
                              for year, year_pop in ideal_results if len(year_pop) > 100],
                             [(year, np.mean([a.trait for a in year_pop if a.race == 2 and a.sex == 2]))
                              for year, year_pop in sterile_results if len(year_pop) > 100])
