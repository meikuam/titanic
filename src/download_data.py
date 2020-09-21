from kaggle import KaggleApi

import os
import json
import zipfile

if __name__ == '__main__':
    config_path = "kaggle.json"
    data_path = 'data'
    print("auth")
    with open(config_path, 'r') as f:
        config_dict = json.load(f)

    api = KaggleApi()
    api._load_config(config_dict)
    print("download")
    api.competition_download_files(
        competition="titanic",
        path=data_path,
        quiet=False
    )
    print("extract")
    for file in os.listdir(data_path):
        if '.zip' in file:
            print(file)
            zip_ref = zipfile.ZipFile(os.path.join(data_path, file), 'r')
            zip_ref.extractall(data_path)
            zip_ref.close()
