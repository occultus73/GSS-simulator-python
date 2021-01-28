import numpy as np


def get_iq_segregated_populations(actual_results, ideal_results, sterile_results):
    actual_average_iq = {year: np.mean([a.iq for a in year_pop])
                         for year, year_pop in actual_results if len(year_pop) > 100}
    ideal_average_iq = {year: np.mean([a.iq for a in year_pop])
                        for year, year_pop in ideal_results if len(year_pop) > 100}
    sterile_average_iq = {year: np.mean([a.iq for a in year_pop])
                          for year, year_pop in sterile_results if len(year_pop) > 100}

    actual_above_average_iq = [(year, [a for a in year_pop if a.iq >= actual_average_iq[year]])
                               for year, year_pop in actual_results if len(year_pop) > 100]
    ideal_above_average_iq = [(year, [a for a in year_pop if a.iq >= ideal_average_iq[year]])
                              for year, year_pop in ideal_results if len(year_pop) > 100]
    sterile_above_average_iq = [(year, [a for a in year_pop if a.iq >= sterile_average_iq[year]])
                                for year, year_pop in sterile_results if len(year_pop) > 100]

    actual_below_average_iq = [(year, [a for a in year_pop if a.iq < actual_average_iq[year]])
                               for year, year_pop in actual_results if len(year_pop) > 100]
    ideal_below_average_iq = [(year, [a for a in year_pop if a.iq < ideal_average_iq[year]])
                              for year, year_pop in ideal_results if len(year_pop) > 100]
    sterile_below_average_iq = [(year, [a for a in year_pop if a.iq < sterile_average_iq[year]])
                                for year, year_pop in sterile_results if len(year_pop) > 100]

    actual_upper_quartile_iq = {year: np.mean([a.iq for a in year_pop])
                                for year, year_pop in actual_above_average_iq if len(year_pop) > 100}
    ideal_upper_quartile_iq = {year: np.mean([a.iq for a in year_pop])
                               for year, year_pop in ideal_above_average_iq if len(year_pop) > 100}
    sterile_upper_quartile_iq = {year: np.mean([a.iq for a in year_pop])
                                 for year, year_pop in sterile_above_average_iq if len(year_pop) > 100}

    actual_lower_quartile_iq = {year: np.mean([a.iq for a in year_pop])
                                for year, year_pop in actual_below_average_iq if len(year_pop) > 100}
    ideal_lower_quartile_iq = {year: np.mean([a.iq for a in year_pop])
                               for year, year_pop in ideal_below_average_iq if len(year_pop) > 100}
    sterile_lower_quartile_iq = {year: np.mean([a.iq for a in year_pop])
                                 for year, year_pop in sterile_below_average_iq if len(year_pop) > 100}

    actual_q4_iq = [(year, [a for a in year_pop if a.iq >= actual_upper_quartile_iq[year]])
                    for year, year_pop in actual_above_average_iq if len(year_pop) > 100]
    ideal_q4_iq = [(year, [a for a in year_pop if a.iq >= ideal_upper_quartile_iq[year]])
                   for year, year_pop in ideal_above_average_iq if len(year_pop) > 100]
    sterile_q4_iq = [(year, [a for a in year_pop if a.iq >= sterile_upper_quartile_iq[year]])
                     for year, year_pop in sterile_above_average_iq if len(year_pop) > 100]

    actual_q3_iq = [(year, [a for a in year_pop if a.iq < actual_upper_quartile_iq[year]])
                    for year, year_pop in actual_above_average_iq if len(year_pop) > 100]
    ideal_q3_iq = [(year, [a for a in year_pop if a.iq < ideal_upper_quartile_iq[year]])
                   for year, year_pop in ideal_above_average_iq if len(year_pop) > 100]
    sterile_q3_iq = [(year, [a for a in year_pop if a.iq < sterile_upper_quartile_iq[year]])
                     for year, year_pop in sterile_above_average_iq if len(year_pop) > 100]

    actual_q2_iq = [(year, [a for a in year_pop if a.iq >= actual_lower_quartile_iq[year]])
                    for year, year_pop in actual_below_average_iq if len(year_pop) > 100]
    ideal_q2_iq = [(year, [a for a in year_pop if a.iq >= ideal_lower_quartile_iq[year]])
                   for year, year_pop in ideal_below_average_iq if len(year_pop) > 100]
    sterile_q2_iq = [(year, [a for a in year_pop if a.iq >= sterile_lower_quartile_iq[year]])
                     for year, year_pop in sterile_below_average_iq if len(year_pop) > 100]

    actual_q1_iq = [(year, [a for a in year_pop if a.iq < actual_lower_quartile_iq[year]])
                    for year, year_pop in actual_below_average_iq if len(year_pop) > 100]
    ideal_q1_iq = [(year, [a for a in year_pop if a.iq < ideal_lower_quartile_iq[year]])
                   for year, year_pop in ideal_below_average_iq if len(year_pop) > 100]
    sterile_q1_iq = [(year, [a for a in year_pop if a.iq < sterile_lower_quartile_iq[year]])
                     for year, year_pop in sterile_below_average_iq if len(year_pop) > 100]

    return {
        "actual_Above_Average_IQ": actual_above_average_iq,
        "actual_Below_Average_IQ": actual_below_average_iq,
        "actual_Q4_IQ": actual_q4_iq,
        "actual_Q3_IQ": actual_q3_iq,
        "actual_Q2_IQ": actual_q2_iq,
        "actual_Q1_IQ": actual_q1_iq,

        "ideal_Above_Average_IQ": ideal_above_average_iq,
        "ideal_Below_Average_IQ": ideal_below_average_iq,
        "ideal_Q4_IQ": ideal_q4_iq,
        "ideal_Q3_IQ": ideal_q3_iq,
        "ideal_Q2_IQ": ideal_q2_iq,
        "ideal_Q1_IQ": ideal_q1_iq,

        "sterile_Above_Average_IQ": sterile_above_average_iq,
        "sterile_Below_Average_IQ": sterile_below_average_iq,
        "sterile_Q4_IQ": sterile_q4_iq,
        "sterile_Q3_IQ": sterile_q3_iq,
        "sterile_Q2_IQ": sterile_q2_iq,
        "sterile_Q1_IQ": sterile_q1_iq,
    }
