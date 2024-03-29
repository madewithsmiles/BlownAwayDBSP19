import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import read_csv
from pathlib import Path
from collections import namedtuple
from helpers import states, populate_gdp_data


# --------------------------- Global Declarations #
dataset = namedtuple('dataset', 'tornados, states, industries, gdp')

# --------------------------------- Main function to be exported #
def get_dataset(debug=False):

    cwd = Path.cwd().parent
    
    if not cwd / Path('data/') in [x for x in cwd.iterdir() if x.is_dir()]:
        cwd /= Path('BlownAwayDBSP19')

    data_folder = cwd / Path('data/')
    n1 = 'SAGDP2S__ALL_AREAS_1963_1997.csv'
    n2 = 'SAGDP2N__ALL_AREAS_1997_2017.csv'
    n3 = 'Tornados.csv'

    sagdp2s = data_folder / Path(n1)
    sagdp2n = data_folder / Path(n2)
    tornado = data_folder / Path(n3)

    assert sagdp2n.exists() and sagdp2s.exists() and tornado.exists()

    # ------------------- Read data #
    data_63 = read_csv(sagdp2s)
    data_97 = read_csv(sagdp2n)
    data_t = read_csv(tornado)

    # -------------------- Rename column names for tornados (data_t) #
    data_t.rename(columns={'Year':'Yr',\
                           'Month':'Mo',\
                           'Day': 'Dy'}, inplace=True)

    # ------------------- State data (states_data, st_df)#
    states_data = {'StateID':[], 'StatePostalCode':[] ,'StateName':[]}
    cnt = 1
    for i,j in states.items():
        states_data['StateID'].append(cnt)
        states_data['StatePostalCode'].append(i)
        states_data['StateName'].append(j)
        cnt += 1

    st_df = pd.DataFrame.from_dict(states_data)
    # ------------------- Update the foreign key for Tornados
    data_t = pd.merge(
        data_t, 
        st_df[['StateID', 'StatePostalCode']], 
        on='StatePostalCode', how='inner')\
        .drop(
            ['StatePostalCode'], 
            axis = 1
            )

    # ------------------ Industry Data (industry_data, ind_df) #

    industry_data = {'IndustryID':[], 'IndustryName':[]}

    assert len(data_97.IndustryId.unique()) == len(data_97.Description.unique())

    industry_data['IndustryID'].extend(data_97.IndustryId.unique())
    industry_data['IndustryName'].extend(data_97.Description.unique())

    ind_df = pd.DataFrame.from_dict(industry_data)

    # ------------------ Gdp #
    gdp_data = {'GdpID':[], 'GDP':[], 'Yr':[], 'StateID':[], 'IndustryID':[]}

    sagdp2s_years = list(range(1963,1997))
    sagdp2s_years_starting_index = 9
    sagdp2n_years = list(range(1997,2017))
    sagdp2n_years_starting_index = 8

    # ------------------- States data #
    states_list = st_df.StateName.tolist()

    gdp_data = populate_gdp_data(gdp_data, data_63, states_list, sagdp2s_years, st_df, sagdp2s_years_starting_index, debug=debug)
    gdp_data = populate_gdp_data(gdp_data, data_97, states_list, sagdp2n_years, st_df, sagdp2n_years_starting_index, debug=debug)

    gdp_df = pd.DataFrame.from_dict(gdp_data)

    assert len(gdp_df[gdp_df['Yr']==2016].StateID) == len(gdp_df[gdp_df['Yr']==2016].StateID.unique())

    # -------------------- Return #
    # return dataset(tornados=data_t, states=states_data, industries=industry_data, gdp=gdp_data)
    return dataset(tornados=data_t, states=st_df, industries=ind_df, gdp=gdp_df)