import pandas as pd
import csv 

star_data = pd.read_csv("final_dataset.csv")

star_data["Mass"] = star_data["Mass"] * 1.989e+30

star_data["Radius"] = star_data["Radius"] * 6.957e+8

gravity = []

def calc_gravity(mass, radius):
    G = 6.674e-11
    return (G * mass) / (radius ** 2)

for i in range(len(star_data)):
    m = star_data.loc[i, "Mass"]
    r = star_data.loc[i, "Radius"]
    g = calc_gravity(m, r)
    gravity.append(g)

star_data["Gravity"] = gravity

star_data.to_csv("final_dataset_with_gravity.csv", index=False)
