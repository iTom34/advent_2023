
ACCELERATION_RATE: int = 1


class Race:
    def __init__(self, race_duration: int, previous_record: int):
        self.race_duration: int = race_duration
        self.previous_record: int = previous_record

    def get_all_distance(self) -> dict[int: int]:
        """
        Returns a dictionary {time_pressed: distance_made}
        """
        result = {}
        for button_pressed_duration in range(self.race_duration + 1):
            result[button_pressed_duration] = self.get_distance_made(button_pressed_duration)

        return result

    def get_all_beating_records(self) -> dict[int: int]:
        """
        Returns a dictionary containing the time pressed that beat the record
        {time_pressed: distance_made,...}
        """
        result = {}
        all_distance: dict = self.get_all_distance()

        for button_pressed_duration, distance in all_distance.items():
            if distance > self.previous_record:
                result[button_pressed_duration] = distance

        return result

    def get_number_of_ways_to_beat_record(self) -> int:
        """
        Return the number of ways to beat the record
        """
        return len(self.get_all_beating_records())

    def get_distance_made(self, button_pressed_duration: int) -> int:
        """
        Computes the distance made
        """
        if button_pressed_duration >= self.race_duration:
            return 0

        racing_time = self.race_duration - button_pressed_duration
        speed = button_pressed_duration * ACCELERATION_RATE

        return racing_time * speed


def puzzle_1(races: list[Race]):
    product = 1
    for race in races:
        product *= race.get_number_of_ways_to_beat_record()

    return product


def puzzle_2(race: Race):
    return race.get_number_of_ways_to_beat_record()

