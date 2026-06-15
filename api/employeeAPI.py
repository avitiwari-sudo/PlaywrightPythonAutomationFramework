class EmployeeAPI:

    def __init__(self, api_context):
        self.api_context = api_context

    def getEmployees(self):

        response = self.api_context.get(
            "/web/index.php/api/v2/pim/employees",
        )
        if response.ok:
            return response
        else:
            return None