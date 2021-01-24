import abc


class Simulator(metaclass=abc.ABCMeta):
    def __init__(self, starting_year, starting_population):
        self._current_year = starting_year - 1
        self._current_population = set(starting_population)

    def next_year(self):
        self._current_year += 1
        self.__apply_deaths()
        self._apply_births()
        return self.__adult_working_population()

    def __adult_working_population(self):
        return list(filter(lambda a: a.is_adult(self._current_year) and not a.has_retired(self._current_year),
                           self._current_population))

    def __apply_deaths(self):
        self._current_population = set(filter(lambda a: not a.has_died(self._current_year),
                                              self._current_population))

    @abc.abstractmethod
    def _apply_births(self):
        pass
