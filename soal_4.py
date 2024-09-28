from datetime import datetime, timedelta


class LeavePolicy:
    def __init__(self, annual_leave=14, max_consecutive_leave=3):
        self.annual_leave = annual_leave
        self.max_consecutive_leave = max_consecutive_leave

    def calculate_personal_leave_quota(self, public_holidays):
        """Calculate personal leave quota based on public holidays."""
        return self.annual_leave - public_holidays

    def calculate_prorated_leave(self, remaining_days, personal_leave_quota):
        """Calculate prorated leave for new employees in their first year."""
        prorated_leave = (remaining_days / 365) * personal_leave_quota
        return int(prorated_leave)  # Round down


class LeaveChecker:
    def __init__(self, leave_policy):
        self.leave_policy = leave_policy

    def is_eligible_for_leave(self, join_date, plan_leave_date):
        """Check if the employee is eligible for leave (after 180 days)."""
        eligibility_date = join_date + timedelta(days=180)
        return plan_leave_date >= eligibility_date, eligibility_date

    def can_take_leave(self, join_date, plan_leave_date, leave_duration, public_holidays):
        """
        Determine if an employee is allowed to take personal leave.
        """
        # Convert input dates to datetime objects
        join_date = datetime.strptime(join_date, "%Y-%m-%d")
        plan_leave_date = datetime.strptime(plan_leave_date, "%Y-%m-%d")

        # Check eligibility based on 180-day rule
        is_eligible, eligibility_date = self.is_eligible_for_leave(join_date, plan_leave_date)
        if not is_eligible:
            return False, "Belum 180 hari sejak tanggal join karyawan."

        # Calculate personal leave quota
        personal_leave_quota = self.leave_policy.calculate_personal_leave_quota(public_holidays)

        # Handle prorated leave for new employees
        if plan_leave_date.year == join_date.year:
            end_of_year = datetime(join_date.year, 12, 31)
            remaining_days = (end_of_year - eligibility_date).days
            available_personal_leave = self.leave_policy.calculate_prorated_leave(remaining_days, personal_leave_quota)
        else:
            available_personal_leave = personal_leave_quota

        # Check if requested leave exceeds the max consecutive leave limit
        if leave_duration > self.leave_policy.max_consecutive_leave:
            return False, f"Durasi cuti maksimal {self.leave_policy.max_consecutive_leave} hari berturut-turut."

        # Check if leave duration exceeds available personal leave
        if leave_duration > available_personal_leave:
            return False, f"Hanya boleh mengambil {available_personal_leave} hari cuti."

        return True, "Boleh mengambil cuti."


def get_user_input():
    """Helper function to get dynamic input from the user."""
    public_holidays = int(input("Jumlah Cuti Bersama = "))
    join_date = input("Tanggal join karyawan (YYYY-MM-DD) = ")
    plan_leave_date = input("Tanggal rencana cuti (YYYY-MM-DD) = ")
    leave_duration = int(input("Durasi cuti (hari) = "))
    return public_holidays, join_date, plan_leave_date, leave_duration


def dynamic_input():
    """Main function to handle dynamic input and checking leave eligibility."""
    leave_policy = LeavePolicy()  # Use default policy of 14 days and max 3 consecutive days
    leave_checker = LeaveChecker(leave_policy)

    public_holidays, join_date, plan_leave_date, leave_duration = get_user_input()

    can_take, reason = leave_checker.can_take_leave(join_date, plan_leave_date, leave_duration, public_holidays)
    print(f"\nOutput:\n• {can_take}\n• Alasan: {reason}")


# Run dynamic input
if __name__ == "__main__":
    dynamic_input()
