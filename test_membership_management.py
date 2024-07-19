import unittest
from membership_management import MembershipManagement

class TestMembershipManagement(unittest.TestCase):

    def setUp(self):
        self.management = MembershipManagement()

    def test_show_plans(self):
        self.management.show_plans()

    def test_select_plan_valid(self):
        self.assertEqual(self.management.select_plan(0), 0)
        self.assertEqual(self.management.selected_membership.name, "Basic")
        self.assertEqual(self.management.select_plan(2), 0)
        self.assertEqual(self.management.selected_membership.name, "Family")

    def test_select_plan_invalid(self):
        self.assertEqual(self.management.select_plan(3), -1)
        self.assertEqual(self.management.select_plan(-1), -1)

    def test_add_features_valid(self):
        self.management.select_plan(1)  # Premium plan
        self.assertEqual(self.management.add_features([1]), 0)
        self.assertIn("Personal Training", self.management.selected_features)

    def test_add_features_invalid(self):
        self.management.select_plan(1)  # Premium plan
        self.assertEqual(self.management.add_features([3]), -1)  # Invalid feature index

    def test_set_number_of_members_valid(self):
        self.assertEqual(self.management.set_number_of_members(5), 0)
        self.assertEqual(self.management.number_of_members, 5)

    def test_set_number_of_members_invalid(self):
        self.assertEqual(self.management.set_number_of_members(0), -1)
        self.assertEqual(self.management.set_number_of_members(-3), -1)

    def test_calculate_total_cost_basic(self):
        self.management.select_plan(0)  # Basic plan
        self.management.set_number_of_members(1)
        self.assertEqual(self.management.calculate_total_cost(), 50)

    def test_calculate_total_cost_premium(self):
        self.management.select_plan(1)  # Premium plan
        self.management.set_number_of_members(1)
        self.assertEqual(self.management.calculate_total_cost(), 115)  # Premium 15% surcharge

    def test_calculate_total_cost_multiple_members(self):
        self.management.select_plan(0)  # Basic plan
        self.management.set_number_of_members(5)
        self.assertEqual(self.management.calculate_total_cost(), 205)  # 5 members with 10% discount

    def test_calculate_total_cost_discounts(self):
        self.management.select_plan(2)  
        self.management.set_number_of_members(3)
        self.management.add_features([1, 2]) 
        self.assertEqual(self.management.calculate_total_cost(), 490) 

    def test_confirm_membership(self):
        self.management.select_plan(1)  # Premium plan 
        self.management.set_number_of_members(1)
        self.assertEqual(self.management.confirm_membership("yes"), 115)
        self.management.set_number_of_members(2)
        self.assertEqual(self.management.confirm_membership("yes"), 187)  # 10% discount applied
        self.assertEqual(self.management.confirm_membership("no"), -1)  # Cancel membership

if __name__ == '__main__':
    unittest.main()
