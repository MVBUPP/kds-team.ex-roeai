
import requests
import os
from keboola.component.base import ComponentBase
class Component(ComponentBase):
    def __init__(self):
        super().__init__()

    def run(self):       
        params = self.configuration.parameters
        Token = params['BearerToken']
        FileName=params['FileName']
        fileID=params['File_ID']
        OutFile=("out/files/{filename}").format(filename=FileName)
        url = "https://api.roe-ai.com/v1/datasets/files/{id}/download/".format(id=fileID)
        headers = {"Authorization": "Bearer {Token}".format(Token=Token)}
        
        response = requests.request("GET", url, headers=headers)

        # Save the content into out/files
        if response.status_code == 200:
            directory = os.path.dirname(OutFile)
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(OutFile, "wb") as fp:
                fp.write(response.content)
            print("Image downloaded successfully.")
        else:
            print(f"Failed to download the image. Status code: {response.status_code}")
       
        

        
if __name__ == "__main__":
        comp = Component()
        # this triggers the run method by default and is controlled by the configuration.action parameter
        comp.execute_action()
    
