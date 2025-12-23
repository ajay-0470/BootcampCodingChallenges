from roles import Roles
class RoleBuilder:
    """
    Private data member
    """
    #ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    """
    Method to get role description for a given role id
    """
    @staticmethod
    def get_role_description(role_id):
        rid = int(role_id)
        mapping = {
            Roles.DEVELOPER: "DEVELOPER",
            Roles.TEST_ENGINEER: "TEST ENGINEER",
            Roles.SR_DEVELOPER: "SENIOR DEVELOPER",
            Roles.DESIGNER: "DESIGNER",
        }
        return mapping.get(rid, "UNDEFINED")