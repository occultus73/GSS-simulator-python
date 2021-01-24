from business.Simulator import Simulator


class FertileSimulator(Simulator):
    def _apply_births(self):
        new_born_children = []
        for american in self._current_population:
            for child in set(filter(lambda a: a.has_born(self._current_year), american.children)):
                new_born_children.append(child)
        for child in new_born_children:
            self._current_population.add(child)
