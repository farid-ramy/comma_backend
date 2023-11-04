from django.test import TestCase
from django.test import TestCase
from .models import User, Branch

class BranchUserRelationshipTestCase(TestCase):
    def test_branch_employee_relationship(self):
        # Create a user
        user = User.objects.create(username="test_user", first_name="John", last_name="Doe")

        # Create a branch with the user as the employee
        branch = Branch.objects.create(name="Test Branch", employee_id=user)

        # Query the branch to get the associated user
        branch_user = branch.employee_id

        # Assert that the branch's employee is the same as the created user
        self.assertEqual(branch_user, user)


# Create your tests here.
