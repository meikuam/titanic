from kaggle import KaggleApi

import os
import json

if __name__ == '__main__':
    config_path = "kaggle.json"
    data_path = 'data'
    filename = 'submission.csv'

    print("auth")
    with open(config_path, 'r') as f:
        config_dict = json.load(f)

    api = KaggleApi()
    api._load_config(config_dict)
    print("submit")

    api.competition_submit(
        file_name=os.path.join(data_path, filename),
        competition="titanic",
        message="test submission",
        quiet=False
    )
