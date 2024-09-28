from abc import ABC, abstractmethod


class ChangeCalculator(ABC):
    """
    Abstract base class for calculating change.
    This class ensures that different calculators can be implemented following the same interface.
    """

    @abstractmethod
    def calculate_change(self, total_cost, amount_paid):
        pass


class IndonesianChangeCalculator(ChangeCalculator):
    """
    Concrete implementation of ChangeCalculator for handling Indonesian currency denominations.
    """

    def __init__(self):
        # Pecahan uang yang tersedia
        self.denominations = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

    def calculate_change(self, total_cost, amount_paid):
        if amount_paid < total_cost:
            return False

        # Hitung kembalian dan bulatkan ke bawah ke kelipatan 100
        change = amount_paid - total_cost
        rounded_change = (change // 100) * 100

        # Dictionary untuk menyimpan pecahan uang yang harus diberikan
        change_details = {}

        # Hitung pecahan uang yang harus diberikan dengan divmod
        for denomination in self.denominations:
            count, rounded_change = divmod(rounded_change, denomination)
            if count > 0:
                change_details[denomination] = count

        return change, change_details


class ChangeDisplay:
    """
    Class responsible for displaying the change details to the user.
    """

    def display(self, total_cost, amount_paid, change_calculator: ChangeCalculator):
        result = change_calculator.calculate_change(total_cost, amount_paid)

        if not result:
            print("False, insufficient payment")
            return

        change, change_details = result

        # Output yang sesuai dengan format yang diinginkan
        print(f"Change to be returned by the cashier: Rp {change:,}, rounded to Rp {change // 100 * 100:,}")
        print("Denominations to be given:")
        for denomination, count in change_details.items():
            unit = "bill" if denomination >= 1000 else "coin"
            print(f"{count} {unit}(s) of Rp {denomination:,}")


class UserInteraction:
    """
    Class responsible for interacting with the user (input and output).
    """

    def __init__(self, change_display: ChangeDisplay):
        self.change_display = change_display

    def process_transaction(self, change_calculator: ChangeCalculator):
        try:
            total_cost = int(input("Total cost: Rp ").replace('.', ''))
            amount_paid = int(input("Amount paid: Rp ").replace('.', ''))
            self.change_display.display(total_cost, amount_paid, change_calculator)
        except ValueError:
            print("Invalid input, please enter valid numbers.")


# Menjalankan simulasi dengan pemisahan tanggung jawab
def main():
    change_calculator = IndonesianChangeCalculator()
    change_display = ChangeDisplay()
    user_interaction = UserInteraction(change_display)

    user_interaction.process_transaction(change_calculator)



if __name__ == "__main__":
    main()

