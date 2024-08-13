
import requests
import os
from keboola.component.base import ComponentBase
import csv
class Component(ComponentBase):
    def __init__(self):
        super().__init__()

    def run(self):       
        params = self.configuration.parameters
        Token = params['BearerToken']
        FileName=params['FileName']
        fileID=params['File_ID']
        OutFile=("out/tables/{filename}").format(filename=FileName)
        # url = "https://api.roe-ai.com/v1/datasets/files/{id}/download/".format(id=fileID)
        # url = "https://api.roe-ai.com/v1/datasets/files/".format(id=fileID)
        url = "https://api.roe-ai.com/v1/database/query/"

        payload = {"query": "SELECT name, file FROM dataset_examples"}
        headers = {"Authorization": "Bearer {Token}".format(Token=Token)}

        response = requests.request("POST", url, json=payload, headers=headers)
       
        print(response.content)
        # response = requests.request("GET", url, headers=headers)
        JSON_response=response.json()
        # Save the content into out/files
        if response.status_code == 200:
            directory = os.path.dirname(OutFile)
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open(OutFile, "w") as fp:
                csvwriter=csv.writer(fp)
                csvwriter.writerow(['FileName','FileID'])
                rows=(JSON_response[0]["result_rows"])
                
                for row in rows:
                    #API call
                    fileid=row[1].split("_")
                    fileid=fileid[1]
                    writerow=[row[0],fileid]
                    # url = "https://api.roe-ai.com/v1/datasets/files/{id}/download/".format(id=fileid)
                    # headers = {"Authorization": "Bearer {Token}".format(Token=Token)}
                    # response = requests.request("GET", url, headers=headers)
                
                    # fp.write("{row}".format(row=row))
                    # print(response.content)
                    # fp.write(response.content)
                    csvwriter.writerow(writerow)
            print("Image(s) downloaded successfully.")
        else:
            print(f"Failed to download the image. Status code: {response.status_code}")
       
        #api call for each file
        
        
if __name__ == "__main__":
        comp = Component()
        # this triggers the run method by default and is controlled by the configuration.action parameter
        comp.execute_action()