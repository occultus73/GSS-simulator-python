from random import random

from data.lazy_property import lazy_property


class American:
    def __init__(self, year_born, age_at_survey, iq, race, sex, number_of_children, age_at_first_child, trait):
        self.year_born = year_born
        self.age_at_survey = age_at_survey
        self.iq = iq
        self.race = race
        self.sex = sex
        self.number_of_children = number_of_children
        self.age_at_first_child = age_at_first_child
        self.trait = trait

    @lazy_property
    def children(self):
        return [American(
            year_born=self.year_born + self.age_at_first_child + birth_order * US_AVERAGE_AGE_GAP_NEXT_SIBLING,
            age_at_survey=self.age_at_survey,
            iq=self.iq,
            race=self.race,
            sex=self.sex,
            number_of_children=self.number_of_children,
            age_at_first_child=self.age_at_first_child,
            trait=self.trait
        ) for birth_order in range(self.__round_number_of_children())]

    def has_born(self, current_year):
        return self.age(current_year) >= 0

    def has_died(self, current_year):
        return self.age(current_year) >= US_LIFE_EXPECTANCY

    def is_adult(self, current_year):
        return self.age(current_year) >= US_VOTING_AGE

    def age(self, current_year):
        return current_year - self.year_born

    def __round_number_of_children(self):
        whole_number_of_children = int(self.number_of_children)
        remainder_number_of_children = self.number_of_children - whole_number_of_children
        if random() < remainder_number_of_children:
            return whole_number_of_children + 1
        else:
            return whole_number_of_children


US_LIFE_EXPECTANCY = 79
US_AVERAGE_AGE_GAP_NEXT_SIBLING = 2
US_VOTING_AGE = 18
