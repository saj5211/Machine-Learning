import numpy as np
import pandas as pd
from random import randint, uniform



def changetoNumbers():
    df = pd.read_csv('imports-85.data.txt', error_bad_lines=False).drop(
        ['normalized-losses', 'symboling', 'bore', 'stroke', 'compression-ratio'], axis=1)
    df.replace('?', 0, inplace=True)
    dict = {"fuel-type": ["diesel", "gas"],
            "aspiration": ["std", "turbo"],
            "make": ["alfa-romero", "audi", "bmw", "chevrolet", "dodge", "honda",
                     "isuzu", "jaguar", "mazda", "mercedes-benz", "mercury",
                     "mitsubishi", "nissan", "peugot", "plymouth", "porsche",
                     "renault", "saab", "subaru", "toyota", "volkswagen", "volvo"],

            "num-of-doors": ["four", "two"],
            "body-style": ["hardtop", "wagon", "sedan", "hatchback", "convertible"],
            "drive-wheels": ["4wd", "fwd", "rwd"],
            "engine-location": ["front", "rear"],
            "engine-type": ["dohc", "dohcv", "l", "ohc", "ohcf", "ohcv", "rotor"],
            "num-of-cylinders": ["eight", "five", "four", "six", "three", "twelve", "two"],
            "fuel-system": ["1bbl", "2bbl", "4bbl", "idi", "mfi", "mpfi", "spdi", "spfi"],
            }
    keys = list(dict.keys())

    for i in df.columns:

        if ((df[i].dtype != np.float64) & (df[i].dtype != np.int64)):
            df[i] = df[i].apply(str)
            row_num = 0
            for j in df[i]:
                row_num += 1

                for k in keys:

                    if str(df[i].name) == str(k):
                        for l in dict[k]:
                            if(str(j) == str(l)) :
                                    df.set_value((row_num-1),i, str(dict[k].index(l)))

                                    break


    df.apply(pd.to_numeric)
    return df

def Data():
    make = randint(0,21)
    fuel_type = randint(0,1)
    aspiration = randint(0,1)
    num_doors = randint(0,1)
    body_style = randint(0,3)
    drive_wheels = randint(0,2)
    engine_location = randint(0,1)
    wheel_base = int(uniform(0, 120.9))
    length = int(uniform(0, 208.1))
    width = int(uniform(0, 72.3))
    height = int(uniform(0, 59.8))
    curb_weight = int(uniform(0, 4066))
    engine_type = randint(0, 6)
    num_cylinders = randint(0, 6)
    engine_size = int(uniform(0, 326))
    fuel_system = randint(0, 7)
    horsepower = int(uniform(0, 288))
    peak_rpm = randint(0, 6600)
    city_mpg = int(uniform(0, 49))
    highway_mpg = int(uniform(0, 54))

    data = [make,fuel_type,aspiration,num_doors,body_style,drive_wheels,engine_location,wheel_base,length,width,height,curb_weight,engine_type,num_cylinders,engine_size,fuel_system,horsepower,peak_rpm,city_mpg,highway_mpg]
    return data