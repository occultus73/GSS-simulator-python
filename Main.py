from data.ActualFertilityDataLoader import ActualFertilityDataLoader
from data.IdealFertilityDataLoader import IdealFertilityDataLoader
from data.SterileFertilityDataLoader import SterileFertilityDataLoader

TRAIT_TO_STUDY = "YEARS_IN_SCHOOL"
MIN_YEAR_OF_BIRTH = 1945
CURRENT_YEAR = 1963
DOOMSDAY = 2080

if __name__ == '__main__':
    actual_fertility_sample = ActualFertilityDataLoader(TRAIT_TO_STUDY, MIN_YEAR_OF_BIRTH).load_sample()
    ideal_fertility_sample = IdealFertilityDataLoader(TRAIT_TO_STUDY, MIN_YEAR_OF_BIRTH).load_sample()
    sterile_fertility_sample = SterileFertilityDataLoader(TRAIT_TO_STUDY, MIN_YEAR_OF_BIRTH).load_sample()
    print("pause here")
