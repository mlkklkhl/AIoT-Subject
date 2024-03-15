import json
import pandas as pd

jsonFilePath = 'aiot-405605-default-rtdb-Test-export.json'

with open(jsonFilePath) as jsonFile:
    data = json.load(jsonFile)
    keys = data.keys()

df = pd.read_json(jsonFilePath)
df = df.T

# df = df[df['IndoorTemperature'] > 1.0]
# df = df[df['OutdoorTemperature'] > 1.0]
# # # df = df[df['Current'] > 0.05]
# # # df = df[df['PM 10'] > 0.0]
# #
# df = df.fillna(df.mean())
#
# new_plot = df.resample('' + str(5) + 'Min').agg(
#             {'Battery-Mi-Device1': 'mean', 'IndoorHumidity-P2': 'mean',
#              'IndoorHumidity-P3': 'mean', 'IndoorTemperature-P2': 'mean',
#              'IndoorTemperature-P3': 'mean'
#              })
#

df['Timestamp'] = keys
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True, drop=True)
df = df.sort_values(by="Timestamp")

# DATE = "2023-10-27"
# minutes = 15
# var = "Humidity" # Temperature, Humidity
# considered_var = "Mean" # Mean or SD

# df = df[DATE + " 06:00:00": DATE + " 14:00:00"]

# df.replace('', np.nan, inplace=True)
# df.dropna()

df = df.reindex(sorted(df.columns), axis=1)
# df = df.resample('' + str(minutes) + 'Min').mean()

df.to_csv('human detection.csv', index=True)

print("Finish")