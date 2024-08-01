
import requests
from keboola.component.base import ComponentBase
class Component(ComponentBase):
    def __init__(self):
        super().__init__()
    def run(self):       
        params = self.configuration.parameters
        Token = params['BearerToken']
        fileID=params['File_ID']
        url = "https://api.roe-ai.com/v1/datasets/files/{id}/download/".format(id=fileID)
        headers = {"Authorization": "Bearer {Token}".format(Token=Token)}

        response = requests.request("GET", url, headers=headers)

        print(response)

if __name__ == "__main__":
        comp = Component()
        # this triggers the run method by default and is controlled by the configuration.action parameter
        comp.execute_action()
    
