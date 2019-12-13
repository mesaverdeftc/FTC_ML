import os
import pandas as pd

data_folders = ['block', 'fakeskyblock', 'skyblock']

filenames = [os.listdir(f) for f in data_folders]
[print(f[1]) for f in filenames]
[len(f) for f in filenames]

files_dict = dict(zip(data_folders, filenames))
base_gcs_path = 'gs://cloudml-demo-vcm/ftc_ml/'

# What we want:
# gs://cloudml-demo-vcm/chairs_table_bike/chair_black/chair_black157.jpg, 'chair_black'
# base_gcs_path + dict_key + '/' + filename

data_array = []
train=.8
val = .9
for (dict_key, files_list) in files_dict.items():
    total = len(files_list)
    trainCnt = total * train
    valCnt = total * val
    i = 0;
    for filename in files_list:
        #         print(base_gcs_path + dict_key + '/' + filename)
        if '.jpg' not in filename:
            continue  # don't include non-photos

        label = dict_key
        #         label = 'chair' if 'chair' in dict_key else dict_key # for grouping all chairs as one label
        type = "TRAIN" if i < trainCnt else "VALIDATION" if i < valCnt else "TEST"
        i += 1
        data_array.append((type, base_gcs_path + dict_key + '/' + filename, label))

dataframe = pd.DataFrame(data_array)
dataframe.to_csv('all_data.csv', index=False, header=False)

#run following command
#gsutil cp all_data.csv gs://cloudml-demo-vcm/chairs_table_bike/