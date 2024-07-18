"""
class Membership:
    def __init__(self, name, base_cost, additional_features=None, premium=False):
        self.name = name
        self.base_cost = base_cost
        self.additional_features = additional_features if additional_features else {}
        self.premium = premium

    def calculate_additional_cost(self, selected_features):
        additional_cost = sum(self.additional_features.get(feature, 0) for feature in selected_features)
        return additional_cost


class MembershipManagement:
    def __init__(self):
        self.memberships = [
            Membership("Basic", 50),
            Membership("Premium", 100, {"Personal Training": 30, "Group Classes": 20}, premium=True),
            Membership("Family", 150, {"Personal Training": 30, "Group Classes": 20})
        ]
        self.selected_membership = None
        self.selected_features = []
        self.number_of_members = 1
        self.total_discount = 0

    def show_plans(self):
        print("Membership Plans:")
        for i, membership in enumerate(self.memberships):
            print(f"{i + 1}. {membership.name} - ${membership.base_cost}")
            if membership.additional_features:
                for j, (feature, cost) in enumerate(membership.additional_features.items()):
                    print(f"   {j + 1}. {feature}: ${cost}")
            if membership.premium:
                print("   - Premium Features (+15% of the total cost)")

    def select_plan(self, index):
        if 0 <= index < len(self.memberships):
            self.selected_membership = self.memberships[index]
            print(f"You have selected the {self.selected_membership.name} plan")
            return 0
        else:
            print("Invalid selection.")
            return -1

    def add_features(self, indices):
        if self.selected_membership:
            for index in indices:
                index -= 1  # Adjust for 0-based index
                if 0 <= index < len(self.selected_membership.additional_features):
                    feature = list(self.selected_membership.additional_features.keys())[index]
                    self.selected_features.append(feature)
                else:
                    print(f"Feature with index {index + 1} not available.")
                    return -1
        else:
            print("No membership selected.")
            return -1
        return 0

    def set_number_of_members(self, number):
        if number > 0:
            self.number_of_members = number
            return 0
        else:
            print("Invalid number of members. Must be at least 1.")
            return -1

    def calculate_total_cost(self):
        if not self.selected_membership:
            return -1

        self.total_discount = 0
        base_cost = self.selected_membership.base_cost
        additional_cost = self.selected_membership.calculate_additional_cost(self.selected_features)
        total_cost = (base_cost + additional_cost) * self.number_of_members

        if self.selected_membership.premium:
            total_cost *= 1.15

        if self.number_of_members > 1:
            member_discount = total_cost * 0.10
            self.total_discount += member_discount
            total_cost -= member_discount

        if total_cost > 400:
            discount = 50
            total_cost -= discount
        elif total_cost > 200:
            discount = 20
            total_cost -= discount
        else:
            discount = 0

        self.total_discount += discount
        return round(total_cost)

    def confirm_membership(self, confirm_input):
        total_cost = self.calculate_total_cost()
        if total_cost == -1:
            print("Invalid input data.")
            return -1

        print(f"Membership Summary:")
        print(f"Plan: {self.selected_membership.name}")
        print(f"Additional Features: {', '.join(self.selected_features) if self.selected_features else 'None'}")
        print(f"Number of Members: {self.number_of_members}")
        print(f"Total Discount Applied: ${self.total_discount}")
        print(f"Total Cost: ${total_cost}")

        confirmation = confirm_input.strip().lower()
        if confirmation == "yes":
            print("Membership confirmed.")
            return total_cost
        else:
            print("Membership canceled.")
            return -1


if __name__ == "__main__":
    management = MembershipManagement()
    management.show_plans()
    try:
        plan = int(input("Select a plan (1, 2, or 3): ")) - 1
        if management.select_plan(plan) == -1:
            raise ValueError("Invalid plan selection.")
    except (ValueError, IndexError) as e:
        print(e)
        plan = -1

    if plan != -1 and management.selected_membership:
        if management.selected_membership.additional_features:
            features = input("Enter the numbers of the additional features separated by commas (e.g., 1, 2) or press enter for none: ")
            if features:
                try:
                    features_list = [int(f.strip()) for f in features.split(",")]
                    if management.add_features(features_list) == -1:
                        raise ValueError("Invalid additional features.")
                except ValueError as e:
                    print(e)
                    features_list = []

        print("Note: A 10% discount will be applied for multiple members.")
        try:
            members = int(input("Enter the number of members: "))
            if management.set_number_of_members(members) == -1:
                raise ValueError("Invalid number of members.")
        except ValueError as e:
            print(e)
            members = -1

        if members != -1:
            total = management.confirm_membership(input("Confirm membership? (yes/no): "))
        else:
            total = -1
    else:
        total = -1

    if total == -1:
        print("Registration could not be completed due to invalid data or cancellation.")
"""