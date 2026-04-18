class Nose:
    """
    Creates a Nose which can smell. Might represent a Robot or Human nose.
    """

    def __init__(self, allergies=None, is_robot=False, air_tank_capacity_liters=20):
        self.smelled_smells = set()
        self.immune_response = False
        self.is_robot = is_robot
        self.allergies = allergies or []
        self.air_tank_capacity_liters = air_tank_capacity_liters
        self.current_air_tank_level = 0
        self.is_running = False

    def smell(self, odor):
        """
        Smell an odor.

        Robots must have capacity in their air tank to smell.
        Humans must not have an active immune response to smell.
        Cyborgs must have both capacity and no immune response to smell.
        """
        self._check_can_smell()

        if self.is_robot:
            self._smell_as_robot(odor)
        else:
            self._smell_as_human(odor)

    def _check_can_smell(self):
        if self.is_robot and self.current_air_tank_level >= self.air_tank_capacity_liters:
            raise RuntimeError("Robot nose cannot smell when air tank is full.")

        if not self.is_robot and self.immune_response:
            raise RuntimeError("Nose cannot smell when immune response is active.")

    def _smell_as_robot(self, odor):
        self.smelled_smells.add(odor)
        self.current_air_tank_level += 1

    def _smell_as_human(self, odor):
        if odor in self.allergies:
            self.immune_response = True
        else:
            self.smelled_smells.add(odor)

    def rest(self):
        """
        Rest the nose.

        This resets the immune response for humans and air tank for robots, and both for cyborgs.

        Does not reset the allergies list or set of past smells.
        """
        self.immune_response = False
        self.current_air_tank_level = 0
        self.is_running = False

    def get_smelled_smells(self):
        """
        Return a copy of the set of previously encountered odors.
        """
        return self.smelled_smells.copy()


if __name__ == "__main__":
    print("Run `pytest tests/smells2_test.py` instead.")