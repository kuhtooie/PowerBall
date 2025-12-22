import random

class PowerballTicket:
    def __init__(self):
        # Define the ranges as per official rules
        self.white_ball_range = range(1, 70) # 1 to 69
        self.red_ball_range = range(1, 27) # 1 to 26
        self.white_balls = []
        self.powerball = None

    def _get_random_from_range(self, r):
        """
        Uses two layers of randomization:
        1. randint to pick a random index within the range's length.
        2. Accessing the range object at that specific index.
        """
        random_index = random.randint(0, len(r) - 1)
        return r[random_index]

    def generate_numbers(self):
        # Generate 5 unique white balls
        selection = []
        while len(selection) < 5:
            number = self._get_random_from_range(self.white_ball_range)
            if number not in selection:
                selection.append(number)
        
        self.white_balls = sorted(selection)
        
        # Generate 1 red Powerball
        self.powerball = self._get_random_from_range(self.red_ball_range)

    def display_ticket(self):
        if not self.white_balls:
            print("No numbers generated yet!")
            return
            
        white_str = " ".join(f"[{n:02}]" for n in self.white_balls)
        print(f"White Balls: {white_str} | Powerball: ({self.powerball:02})")

# Example Usage
if __name__ == "__main__":
    ticket = PowerballTicket()
    ticket.generate_numbers()
    ticket.display_ticket()
