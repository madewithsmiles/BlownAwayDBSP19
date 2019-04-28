import sys
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def populate_gdp_data(gdp_dict, dataset, states_list, years, st_df, first_year_index_in_header, iId=1, debug=False):
    count = len(gdp_dict['GdpID'])
    
    count += 1
        
    for state in states_list:
        current_row = dataset[(dataset['GeoName']==state) & (dataset['IndustryId']==iId)].values.tolist()

        if debug:
            print(state)
            print(current_row)
                
        if current_row != []:
            
            assert len(current_row) == 1
            current_row = current_row[0]
            
            sId = st_df[st_df['StateName']==state].StateID.values.tolist()[0]
            
            if debug:
                print(sId)
                print(len(current_row[8:]))
            
            for year, value in zip(years,current_row[first_year_index_in_header:]):
                if debug:
                    print(f"YEAR: {year}, VALUE: {value}")
                else:
                    gdp_dict['GdpID'].append(count)
                    gdp_dict['GDP'].append(float(value))
                    gdp_dict['Yr'].append(year)
                    gdp_dict['StateID'].append(sId)
                    gdp_dict['IndustryID'].append(iId)
                    count += 1
    return gdp_dict