class AutomaticSprinkler:
    def __init__(self):
        self.soil_moister = 0
        self.wheather_condition = "sunny"  # sunny, rainy, cloudy
        self.time_of_day = "day"  # day, night

    def set_soil_moister(self, moister_level):
        self.soil_moister = moister_level

    def set_wheather_condition(self, condition):
        self.wheather_condition = condition

    def set_time_of_day(self, time_of_day):
        self.time_of_day = time_of_day

    def decide_sprinkler_action(self):
        if self.wheather_condition == "rainy":
            print("No need for water, it's already rainy.")
            return "No action needed"

        if self.wheather_condition == "cloudy":
            if self.soil_moister < 50:  # Fixed condition
                print("It is cloudy, but soil is dry. Sprinkler activated.")
                return "Sprinkler ON"
            else:
                print("It is cloudy, soil moisture is sufficient. No need to water.")
                return "No action needed"

        if self.wheather_condition == "sunny":
            if self.soil_moister < 30 and self.time_of_day == "day":
                print("It is sunny, soil is dry. Sprinkler activated.")
                return "Sprinkler ON"
            elif self.soil_moister > 30 and self.time_of_day == "day":
                print("Soil moisture is sufficient. No need to water.")
                return "No action needed"

        if self.time_of_day == "night":
            print("It's night, no need to water.")
            return "No action needed"

        return "No action needed"

# Example usage:
sprinkler = AutomaticSprinkler()
sprinkler.set_soil_moister(25)
sprinkler.set_wheather_condition("sunny")
sprinkler.set_time_of_day("day")

result = sprinkler.decide_sprinkler_action()
print(f"Sprinkler action: {result}")
