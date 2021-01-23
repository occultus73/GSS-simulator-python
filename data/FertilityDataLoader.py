import abc

from data.GSS_data_columns import gss_columns as col


class FertilityDataLoader(metaclass=abc.ABCMeta):
    def __init__(self, trait_to_study, minimum_year_of_birth):
        self._trait_to_study = trait_to_study
        self.__minimum_year_of_birth = minimum_year_of_birth

    @abc.abstractmethod
    def _verify_male_american_condition(self, data):
        pass

    @abc.abstractmethod
    def _verify_female_american_condition(self, data):
        pass

    @abc.abstractmethod
    def _get_male_american(self, data):
        pass

    @abc.abstractmethod
    def _get_female_american(self, data):
        pass

    def load_sample(self):
        americans = []
        print("Loading Sample For Trait:", self._trait_to_study)
        print("Minimum Year For Birth:", self.__minimum_year_of_birth)
        file_reader = open("GSS_fertility_data.csv", "r")
        for line in file_reader:
            data = line.rstrip().split(',')
            year_born = data[col["YEAR_BORN"]]
            if not (year_born.isdigit() and int(year_born) >= self.__minimum_year_of_birth):
                continue
            elif self._verify_male_american_condition(data):
                americans.append(self._get_male_american(data))
            elif self._verify_female_american_condition(data):
                americans.append(self._get_female_american(data))
        file_reader.close()
        return americans


def _get_race(data):
    if data[col["WHITE"]]:
        return 1
    elif data[col["BLACK"]]:
        return 2
    else:
        return 0


def _get_sex(data):
    if data[col["MALE"]]:
        return 1
    elif data[col["FEMALE"]]:
        return 2
    else:
        return IOError("Unknown sex encountered.")


def _get_age_at_first_child(data):
    age_at_first_child = data[col["AGE_AT_FIRST_CHILD"]]
    if age_at_first_child.isdigit():
        return int(age_at_first_child)
    else:
        return 0
