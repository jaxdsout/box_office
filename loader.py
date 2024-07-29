import os
import pandas as pd


def load_data(directory):
    data_frames = []

    for file_name in os.listdir(directory):
        if file_name.endswith(".csv"):
            file_path = os.path.join(directory, file_name)
            df = pd.read_csv(file_path)
            df['year'] = file_name.split('_')[-1].split('.')[0]
            data_frames.append(df)

    combined_data = pd.concat(data_frames, ignore_index=True)
    return combined_data
