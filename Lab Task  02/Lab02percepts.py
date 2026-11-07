# Lab 02 - smart classroom reflex agent (no memory)
# Run: python lab2_percepts.py

class RoomController:
    MIN_TEMP = 20
    MAX_TEMP = 26

    def act(self, temperature, occupied):
        if not occupied:
            return "ECO"
        if temperature > self.MAX_TEMP:
            return "COOL"
        if temperature < self.MIN_TEMP:
            return "WARM"
        return "IDLE"


if __name__ == "__main__":
    controller = RoomController()
    readings = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)]
    for number, reading in enumerate(readings, start=1):
        mode = controller.act(*reading)
        print(number, reading, "target mode", mode)