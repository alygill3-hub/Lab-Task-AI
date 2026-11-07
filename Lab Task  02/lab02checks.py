# Lab 2 - Stateful Classroom Agent Model

class StatefulClassroomAgent:
    def __init__(self):
        # Track the last sent mode to implement statefulness
        self.last_mode = None   

    def decide(self, temperature, is_occupied):
        # Core decision logic based on temperature and occupancy
        if not is_occupied:
            return "ECO"
        if temperature > 26:
            return "COOL"
        if temperature < 20:
            return "WARM"
        return "IDLE"

    def act(self, temperature, is_occupied):
        target_mode = self.decide(temperature, is_occupied)
        # Send command only if the mode has changed from the previous state
        should_send = target_mode != self.last_mode
        self.last_mode = target_mode
        return target_mode, should_send


def run_trace(title, percept_sequence):
    agent = StatefulClassroomAgent()
    print("\n" + title)
    print(f"{'Step':<5}{'Previous':<10}{'Percept':<14}{'Target':<8}Outcome")
    
    for step, percept in enumerate(percept_sequence, 1):
        prev_state = agent.last_mode
        target_mode, should_send = agent.act(*percept)
        outcome_msg = "SEND COMMAND" if should_send else "no command"
        print(f"{step:<5}{str(prev_state):<10}{str(percept):<14}{target_mode:<8}{outcome_msg}")


if __name__ == "__main__":
    run_trace("A) Repeated percepts", [(29, True), (29, True), (29, True)])
    run_trace("B) Exact boundaries", [(20, True), (26, True)])
    run_trace("C) Mode transition", [(29, True), (24, True), (19, True), (29, True)])
    run_trace("D) Empty room", [(29, True), (29, False), (15, False), (29, True)])
    run_trace("E) Full required sequence", 
              [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)])
    run_trace("F) Noisy sequence around 26 (no hysteresis)", 
              [(26.2, True), (25.8, True), (26.3, True), (25.7, True)])