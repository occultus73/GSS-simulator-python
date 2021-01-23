from data.American import American
from data.FertilityDataLoader import FertilityDataLoader, _get_race, _get_sex, _get_age_at_first_child
from data.GSS_data_columns import gss_columns as col


class IdealFertilityDataLoader(FertilityDataLoader):
    def _verify_male_american_condition(self, data):
        return self.__verify_any_condition(data)

    def _verify_female_american_condition(self, data):
        return self.__verify_any_condition(data)

    def _get_male_american(self, data):
        return self.__get_any_american(data)

    def _get_female_american(self, data):
        return self.__get_any_american(data)

    def __verify_any_condition(self, data):
        has_ideal_fertility = data[col["IDEAL_NUMBER_OF_CHILDREN"]] != ''
        has_age = data[col["AGE"]] != ''
        has_iq = data[col["IQ"]] != ''
        has_age_at_first_child = data[col["AGE_AT_FIRST_CHILD"]] != '' or data[col["IDEAL_NUMBER_OF_CHILDREN"]] == '0'
        has_trait_to_study = data[col[self._trait_to_study]] != ''
        return has_ideal_fertility and has_age and has_iq and has_age_at_first_child and has_trait_to_study

    def __get_any_american(self, data):
        return American(
            year_born=int(data[col["YEAR_BORN"]]),
            age_at_survey=int(data[col["AGE"]]),
            iq=float(data[col["IQ"]]),
            race=_get_race(data),
            sex=_get_sex(data),
            number_of_children=float(data[col["IDEAL_NUMBER_OF_CHILDREN"]]) / 2.0,
            age_at_first_child=_get_age_at_first_child(data),
            trait=float(data[col[self._trait_to_study]])
        )
