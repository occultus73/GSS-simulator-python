import numpy as np

from analysis.demographic_information import get_segregated_populations
from analysis.graph_methods import graph_simulation_results
from analysis.iq_information import get_iq_segregated_populations
from analysis.meta_information import graph_meta_info

demographics = ["Whole", "White", "Black", "Male", "Female", "White_Male", "White_Female", "Black_Male", "Black_Female"]
iq_demographics = ["Above_Average_IQ", "Below_Average_IQ", "Q4_IQ", "Q3_IQ", "Q2_IQ", "Q1_IQ"]
iq_averages = ["Average_IQ", "Upper_Quartile_IQ", "Lower_Quartile_IQ"]


class InformationProcessor:
    def __init__(self, trait, max_trait, min_trait, directory, actual_results, ideal_results, sterile_results):
        self.__trait = trait
        self.__max_trt = max_trait
        self.__min_trt = min_trait
        self.__directory = directory
        self.__actual_rts = actual_results
        self.__ideal_rts = ideal_results
        self.__sterile_rts = sterile_results
        self.__draw_score_proportions = max_trait - min_trait <= 12

    def process_results(self):
        # Graph averages for whole population, and population broken down by demographic and/or IQ-demographic.
        demographic_pops = get_segregated_populations(self.__actual_rts, self.__ideal_rts, self.__sterile_rts)
        for demographic in demographics:
            self.__graph_averages(demographic, demographic_pops)
            if self.__draw_score_proportions:
                for score in range(self.__min_trt, self.__max_trt + 1):
                    self.__graph_score_proportion(demographic, demographic_pops, score)

    def __graph_averages(self, dem, dem_pop):
        # Configure directory
        directory_extension = "/Averages"
        if dem != "Whole":
            directory_extension = f"{directory_extension}/{dem}"

        # Graph average for specific demographic
        graph_simulation_results(f"{self.__directory}/{directory_extension}",
                                 f"Average_{self.__trait}_of_{dem}_Pop",
                                 f"Score({self.__min_trt}-{self.__max_trt})",
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in dem_pop[f"actual_{dem}_Population"] if len(year_pop) > 100],
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in dem_pop[f"ideal_{dem}_Population"] if len(year_pop) > 100],
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in dem_pop[f"sterile_{dem}_Population"] if len(year_pop) > 100])

        # Also graph further meta-information, for this demographic
        graph_meta_info(f"{self.__directory}/{directory_extension}/_Meta_Information", f"{dem}",
                        dem_pop[f"actual_{dem}_Population"],
                        dem_pop[f"ideal_{dem}_Population"],
                        dem_pop[f"sterile_{dem}_Population"])

        # Graph IQ sub-demographics
        iq_demographic_pops = get_iq_segregated_populations(dem_pop[f"actual_{dem}_Population"],
                                                            dem_pop[f"ideal_{dem}_Population"],
                                                            dem_pop[f"sterile_{dem}_Population"])

        subdirectory_extension = f"{directory_extension}/IQ_Demographics"
        for iq_demographic in iq_demographics:
            self.__graph_avg_trait_by_iq_demographic(subdirectory_extension, dem, iq_demographic, iq_demographic_pops)
        for iq_average in iq_averages:
            self.__graph_iq_averages(subdirectory_extension, dem, iq_average, iq_demographic_pops)

    def __graph_score_proportion(self, dem, dem_pop, score):
        # Configure directory
        directory_extension = f"/Score_Proportions/{score}"
        if dem != "Whole":
            directory_extension = f"{directory_extension}/{dem}"

        graph_simulation_results(f"{self.__directory}/{directory_extension}",
                                 f"{self.__trait}_{dem}_Population_scoring_{score}", f"% of {dem} Population",
                                 [(year, sum([1 for a in year_pop if a.trait == score]) * 100 / len(year_pop))
                                  for year, year_pop in dem_pop[f"actual_{dem}_Population"] if len(year_pop) > 100],
                                 [(year, sum([1 for a in year_pop if a.trait == score]) * 100 / len(year_pop))
                                  for year, year_pop in dem_pop[f"ideal_{dem}_Population"] if len(year_pop) > 100],
                                 [(year, sum([1 for a in year_pop if a.trait == score]) * 100 / len(year_pop))
                                  for year, year_pop in dem_pop[f"sterile_{dem}_Population"] if len(year_pop) > 100])

        # Also graph further meta-information, for this demographic score proportion
        graph_meta_info(f"{self.__directory}/{directory_extension}/_Meta_Information", f"{dem}_scoring_{score}",
                        [(year, [a for a in year_pop if a.trait == score])
                         for year, year_pop in dem_pop[f"actual_{dem}_Population"] if len(year_pop) > 100],
                        [(year, [a for a in year_pop if a.trait == score])
                         for year, year_pop in dem_pop[f"ideal_{dem}_Population"] if len(year_pop) > 100],
                        [(year, [a for a in year_pop if a.trait == score])
                         for year, year_pop in dem_pop[f"sterile_{dem}_Population"] if len(year_pop) > 100])

        # Graph IQ sub-demographics
        iq_demographic_pops = get_iq_segregated_populations(dem_pop[f"actual_{dem}_Population"],
                                                            dem_pop[f"ideal_{dem}_Population"],
                                                            dem_pop[f"sterile_{dem}_Population"])
        subdir_extension = f"{directory_extension}/IQ_Demographics"
        for iq_demographic in iq_demographics:
            self.__graph_proportion_by_iq_demographic(subdir_extension, dem, iq_demographic, iq_demographic_pops, score)
        for iq_average in iq_averages:
            self.__graph_iq_averages(subdir_extension, dem, iq_average, iq_demographic_pops)

    def __graph_avg_trait_by_iq_demographic(self, directory_extension, dem, iq_dem, iq_dem_pop):
        # Graph average for specific IQ demographic
        graph_simulation_results(f"{self.__directory}/{directory_extension}",
                                 f"Average_{self.__trait}_{dem}_{iq_dem}",
                                 f"Score({self.__min_trt}-{self.__max_trt})",
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in iq_dem_pop[f"actual_{iq_dem}"] if len(year_pop) > 100],
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in iq_dem_pop[f"ideal_{iq_dem}"] if len(year_pop) > 100],
                                 [(year, np.mean([a.trait for a in year_pop]))
                                  for year, year_pop in iq_dem_pop[f"sterile_{iq_dem}"] if len(year_pop) > 100])

        # Also graph further meta-information, for this IQ demographic
        graph_meta_info(f"{self.__directory}/{directory_extension}/_Meta_Information", f"{dem}_{iq_dem}",
                        iq_dem_pop[f"actual_{iq_dem}"],
                        iq_dem_pop[f"ideal_{iq_dem}"],
                        iq_dem_pop[f"sterile_{iq_dem}"])

    def __graph_proportion_by_iq_demographic(self, directory_extension, dem, iq_dem, iq_dem_pop, score):
        # Graph score population proportions for specific IQ demographic
        graph_simulation_results(f"{self.__directory}/{directory_extension}",
                                 f"Score_{score}_in_{self.__trait}_for_{dem}_{iq_dem}",
                                 f"% of {dem} {iq_dem} Population",
                                 [(year, sum([1 for a in year_pop if a.trait == score]) * 100 / len(year_pop))
                                  for year, year_pop in iq_dem_pop[f"actual_{iq_dem}"] if len(year_pop) > 100],
                                 [(year, sum([1 for a in year_pop if a.trait == score]) * 100 / len(year_pop))
                                  for year, year_pop in iq_dem_pop[f"ideal_{iq_dem}"] if len(year_pop) > 100],
                                 [(year, sum([1 for a in year_pop if a.trait == score]) * 100 / len(year_pop))
                                  for year, year_pop in iq_dem_pop[f"sterile_{iq_dem}"] if len(year_pop) > 100])

        # Also graph further meta-information, for this IQ demographic score proportion
        graph_meta_info(f"{self.__directory}/{directory_extension}/_Meta_Information",
                        f"{dem}_{iq_dem}_scoring_{score}",
                        [(year, [a for a in year_pop if a.trait == score])
                         for year, year_pop in iq_dem_pop[f"actual_{iq_dem}"] if len(year_pop) > 100],
                        [(year, [a for a in year_pop if a.trait == score])
                         for year, year_pop in iq_dem_pop[f"ideal_{iq_dem}"] if len(year_pop) > 100],
                        [(year, [a for a in year_pop if a.trait == score])
                         for year, year_pop in iq_dem_pop[f"sterile_{iq_dem}"] if len(year_pop) > 100])

    def __graph_iq_averages(self, directory_extension, dem, iq_average, iq_dem_pop):
        # Graph score population proportions for specific IQ demographic
        graph_simulation_results(f"{self.__directory}/{directory_extension}/_Meta_Information",
                                 f"{iq_average}_in_{self.__trait}_Sample for {dem}", "IQ",
                                 iq_dem_pop[f"actual_{iq_average}"].items(),
                                 iq_dem_pop[f"ideal_{iq_average}"].items(),
                                 iq_dem_pop[f"sterile_{iq_average}"].items())
