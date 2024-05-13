# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mq2wgFpB0xQ2GItKvYa1Uko1X85o-9rO
"""

import pandas as pd
url='https://raw.githubusercontent.com/anvesh232/project/main/main_data.csv'
df=pd.read_csv(url)
df.head(2)
#The following are corresponding codes to their meaning of all columns
hefaminc_dict = {
    "16": "150,000 or More","15": "100,000 To 149,999","14": "75,000 To 99,999","13": "60,000 To 74,999","12": "50,000 To 59,999","11": "40,000 To 49,999","10": "35,000 To 39,999","9": "30,000 To 34,999","8": "25,000 To 29,999","7": "20,000 To 24,999","6": "15,000 To 19,999","5": "12,500 To 14,999","4": "10,000 To 12,499","3": "7,500 To 9,999","2": "5,000 To 7,499","1": "Less Than $5,000"
}
prcow1_dict = {"-1": "Met No Conditions To Assign","4": "Private ","1": "Federal government","6": "Without pay","2": "State government","5": "Self-Employed","3": "Local government"
}
pesex_dict = {"2": "Female","1": "Male"}
pemaritl_dict = {"4":"Divorced","2":"Married-Spouse Absent","1":"Married-Spouse Present","3":"Widowed","-1":"Not in Universe","6":"Never Married","5":"Separated"
}
peeduca_dict = {"46": "DOCTORATE DEGREE","41": "Associate Degree-Occupational/Vocationl","45": "Professional School Deg","43": "Bachelor's Degree","-1": "Not in Universe","42": "Associate Deg.-Academic Program","39": "High School Grad-Diploma","44": "MASTER'S DEGREE","33": "Below High School","31": "Below High School","38": "Below High School","40": "Below High School","32": "Below High School","37": "Below High School","36": "Below High School","35": "Below High School","34": "Below High School"
}
cbsa_dict = {
    "34740": "Muskegon, MI","34980": "Nashville-Davidson--Murfreesboro--Franklin, TN","39740": "Reading, PA","24020": "Glens Falls, NY","13460": "Bend-Redmond, OR","47900": "Washington-Arlington-Alexandria, DC-VA-MD-WV","43780": "South Bend-Mishawaka, IN-MI","22180": "Fayetteville, NC","26420": "Houston-The Woodlands-Sugar Land, TX","12940": "Baton Rouge, LA","40140": "Riverside-San Bernardino-Ontario, CA","45940": "Trenton, NJ","35980": "Norwich-New London, CT","00000": "Not Identified or Nonmetropolitan","14540": "Bowling Green, KY","39140": "Prescott, AZ","48620": "Wichita, KS","40900": "Sacramento--Roseville--Arden-Arcade, CA","11100": "Amarillo, TX","49020": "Winchester, VA-WV","17780": "College Station-Bryan, TX","29620": "Lansing-East Lansing, MI","14260": "Boise City, ID","41740": "San Diego-Carlsbad, CA","10580": "Albany-Schenectady-Troy, NY","45300": "Tampa-St. Petersburg-Clearwater, FL","46060": "Tucson, AZ","12620": "Bangor, ME","15540": "Burlington-South Burlington, VT","40980": "Saginaw, MI","22520": "Florence-Muscle Shoals, AL","36100": "Ocala, FL","19660": "Deltona-Daytona Beach-Ormond Beach, FL","49180": "Winston-Salem, NC","31540": "Madison, WI","36540": "Omaha-Council Bluffs, NE-IA","13780": "Binghamton, NY","21140": "Elkhart-Goshen, IN","39340": "Provo-Orem, UT","35660": "Niles-Benton Harbor, MI","27340": "Jacksonville, NC","44100": "Springfield, IL","21340": "El Paso, TX","38900": "Portland-Vancouver-Hillsboro, OR-WA","48140": "Wausau, WI","41620": "Salt Lake City, UT","31140": "Louisville/Jefferson County, KY-IN","41180": "St. Louis, MO-IL","13140": "Beaumont-Port Arthur, TX","32580": "McAllen-Edinburg-Mission, TX","37460": "Panama City, FL","37340": "Palm Bay-Melbourne-Titusville, FL","22420": "Flint, MI","26900": "Indianapolis-Carmel-Anderson, IN","37900": "Peoria, IL","42100": "Santa Cruz-Watsonville, CA","27500": "Janesville-Beloit, WI","36220": "Odessa, TX","27980": "Kahului-Wailuku-Lahaina, HI","16980": "Chicago-Naperville-Elgin, IL-IN-WI","22500": "Florence, SC","47580": "Warner Robins, GA","30460": "Lexington-Fayette, KY","40380": "Rochester, NY","31420": "Macon, GA","28020": "Kalamazoo-Portage, MI","49620": "York-Hanover, PA","49740": "Yuma, AZ","10740": "Albuquerque, NM","36420": "Oklahoma City, OK","42540": "Scranton--Wilkes-Barre--Hazleton, PA","27140": "Jackson, MS","23580": "Gainesville, GA","43620": "Sioux Falls, SD","12580": "Baltimore-Columbia-Towson, MD","47300": "Visalia-Porterville, CA","31080": "Los Angeles-Long Beach-Anaheim, CA","22020": "Fargo, ND-MN","12100": "Atlantic City-Hammonton, NJ","16700": "Charleston-North Charleston, SC","16820": "Charlottesville, VA","44700": "Stockton-Lodi, CA","11460": "Ann Arbor, MI","29540": "Lancaster, PA","25180": "Hagerstown-Martinsburg, MD-WV","14500": "Boulder, CO","13740": "Billings, MT","25260": "Hanford-Corcoran, CA","39540": "Racine, WI","39300": "Providence-Warwick, RI-MA","41500": "Salinas, CA","28420": "Kennewick-Richland, WA","42140": "Santa Fe, NM","26580": "Huntington-Ashland, WV-KY-OH","47260": "Virginia Beach-Norfolk-Newport News, VA-NC","24140": "Goldsboro, NC","32780": "Medford, OR","46140": "Tulsa, OK","16620": "Charleston, WV","33740": "Monroe, LA","21500": "Erie, PA","38860": "Portland-South Portland, ME","44060": "Spokane-Spokane Valley, WA","45820": "Topeka, KS","18580": "Corpus Christi, TX","28700": "Kingsport-Bristol-Bristol, TN-VA","39820": "Redding, CA","28140": "Kansas City, MO-KS","46340": "Tyler, TX","37980": "Philadelphia-Camden-Wilmington, PA-NJ-DE-MD","12220": "Auburn-Opelika, AL","48060": "Watertown-Fort Drum, NY","25860": "Hickory-Lenoir-Morganton, NC","20500": "Durham-Chapel Hill, NC","23420": "Fresno, CA","27100": "Jackson, MI","36740": "Orlando-Kissimmee-Sanford, FL","22900": "Fort Smith, AR-OK","26820": "Idaho Falls, ID","30980": "Longview, TX","29180": "Lafayette, LA","41860": "San Francisco-Oakland-Hayward, CA","31700": "Manchester-Nashua, NH","27780": "Johnstown, PA","13820": "Birmingham-Hoover, AL","12060": "Atlanta-Sandy Springs-Roswell, GA","37100": "Oxnard-Thousand Oaks-Ventura, CA","22660": "Fort Collins, CO","29820": "Las Vegas-Henderson-Paradise, NV","20100": "Dover, DE","41700": "San Antonio-New Braunfels, TX","49660": "Youngstown-Warren-Boardman, OH-PA","46700": "Vallejo-Fairfield, CA","17820": "Colorado Springs, CO","16860": "Chattanooga, TN-GA","12700": "Barnstable Town, MA","42200": "Santa Maria-Santa Barbara, CA","15980": "Cape Coral-Fort Myers, FL","34940": "Naples-Immokalee-Marco Island, FL","48660": "Wichita Falls, TX","28940": "Knoxville, TN","17460": "Cleveland-Elyria, OH","27260": "Jacksonville, FL","17900": "Columbia, SC","26980": "Iowa City, IA","34580": "Mount Vernon-Anacortes, WA","44140": "Springfield, MA","23540": "Gainesville, FL","12540": "Bakersfield, CA","10900": "Allentown-Bethlehem-Easton, PA-NJ","17980": "Columbus, GA-AL","33660": "Mobile, AL","47380": "Waco, TX","29700": "Laredo, TX","34060": "Morgantown, WV","40060": "Richmond, VA","14460": "Boston-Cambridge-Newton, MA-NH","35380": "New Orleans-Metairie, LA","17020": "Chico, CA","12020": "Athens-Clarke County, GA","16740": "Charlotte-Concord-Gastonia, NC-SC","47220": "Vineland-Bridgeton, NJ","19300": "Daphne-Fairhope-Foley, AL","34820": "Myrtle Beach-Conway-North Myrtle Beach, SC-NC","29340": "Lake Charles, LA","29460": "Lakeland-Winter Haven, FL","41100": "St. George, UT","24580": "Green Bay, WI","36780": "Oshkosh-Neenah, WI","26620": "Huntsville, AL","22140": "Farmington, NM","19740": "Denver-Aurora-Lakewood, CO","38940": "Port St. Lucie, FL","15940": "Canton-Massillon, OH","14860": "Bridgeport-Stamford-Norwalk, CT","24660": "Greensboro-High Point, NC","45460": "Terre Haute, IN","32820": "Memphis, TN-MS-AR","46540": "Utica-Rome, NY","33460": "Minneapolis-St. Paul-Bloomington, MN-WI","33340": "Milwaukee-Waukesha-West Allis, WI","19820": "Detroit-Warren-Dearborn, MI","14010": "Bloomington, IL","19380": "Dayton, OH","14020": "Bloomington, IN","45780": "Toledo, OH","49340": "Worcester, MA-CT","15680": "California-Lexington Park, MD","16540": "Chambersburg-Waynesboro, PA","33780": "Monroe, MI","12980": "Battle Creek, MI","38300": "Pittsburgh, PA","21780": "Evansville, IN-KY","10420": "Akron, OH","45060": "Syracuse, NY","42220": "Santa Rosa, CA","17140": "Cincinnati, OH-KY-IN","12260": "Augusta-Richmond County, GA-SC","16060": "Carbondale-Marion, IL","33860": "Montgomery, AL","19780": "Des Moines-West Des Moines, IA","15180": "Brownsville-Harlingen, TX","44180": "Springfield, MO","11700": "Asheville, NC","10180": "Abilene, TX","24340": "Grand Rapids-Wyoming, MI","29200": "Lafayette-West Lafayette, IN","37860": "Pensacola-Ferry Pass-Brent, FL","40220": "Roanoke, VA","30780": "Little Rock-North Little Rock-Conway, AR","41540": "Salisbury, MD-DE","31180": "Lubbock, TX","39580": "Raleigh, NC","24780": "Greenville, NC","35300": "New Haven-Milford, CT","45220": "Tallahassee, FL","17300": "Clarksville, TN-KY","17660": "Coeur d'Alene, ID","22220": "Fayetteville-Springdale-Rogers, AR-MO","33100": "Miami-Fort Lauderdale-West Palm Beach, FL","48700": "Williamsport, PA","40420": "Rockford, IL","29740": "Las Cruces, NM","24860": "Greenville-Anderson-Mauldin, SC","28660": "Killeen-Temple, TX","35620": "New York-Newark-Jersey City, NY-NJ-PA","23060": "Fort Wayne, IN","47940": "Waterloo-Cedar Falls, IA","16300": "Cedar Rapids, IA","35840": "North Port-Sarasota-Bradenton, FL","19100": "Dallas-Fort Worth-Arlington, TX","21660": "Eugene, OR","19340": "Davenport-Moline-Rock Island, IA-IL","18140": "Columbus, OH","41940": "San Jose-Sunnyvale-Santa Clara, CA","42340": "Savannah, GA","27740": "Johnson City, TN","43300": "Sherman-Denison, TX","38060": "Phoenix-Mesa-Scottsdale, AZ","25420": "Harrisburg-Carlisle, PA","25540": "Hartford-West Hartford-East Hartford, CT","30340": "Lewiston-Auburn, ME","15500": "Burlington, NC","42660": "Seattle-Tacoma-Bellevue, WA","33700": "Modesto, CA","15380": "Buffalo-Cheektowaga-Niagara Falls, NY","41420": "Salem, OR","24540": "Greeley, CO","17420": "Cleveland, TN","13980": "Blacksburg-Christiansburg-Radford, VA","16580": "Champaign-Urbana, IL","12420": "Austin-Round Rock, TX","38220": "Pine Bluff, AR","46520": "Urban Honolulu, HI","25940": "Hilton Head Island-Bluffton-Beaufort, SC","11540": "Appleton, WI","20700": "East Stroudsburg, PA","42020": "San Luis Obispo-Paso Robles-Arroyo Grande, CA","36260": "Ogden-Clearfield, UT","43340": "Shreveport-Bossier City, LA","43900": "Spartanburg, SC"
}
#i'm replacing the cbsa codes with their names here
# Iterate over each row in the DataFrame
for index, row in df.iterrows():
    # Extract CBSA code from the row
    cbsa_code = str(row['CBSA'])

    # Replace CBSA code with corresponding area name from cbsa_dict
    if cbsa_code in cbsa_dict:
        df.at[index, 'CBSA'] = cbsa_dict[cbsa_code]
    else:
        df.at[index, 'CBSA'] = "Unknown"  # Set to "Unknown" if CBSA code not found in cbsa_dict

hefaminc_dict1 = {"16","15","14","13","12","11","10","9","8","7","6","5","4","3","2","1"}
peeduca_dict1 = {"46","33","44","39","42","31","38","40","-1","32","43","37","45","36","35","34","41"}
pemaritl_dict1 = {"4","2","1","3","-1","6","5"}
pesex_dict1 = { "2","1"}
prcow1_dict1 = {"-1","4","1","6","2","5","3"}
hrnumhou_dict1 = {"14": "14","13": "13","12": "12","11": "11","10": "10","9": "9","8": "8","7": "7","6": "6","5": "5","4": "4","3": "3","2": "2","1": "1"}
cbsa_dict1={"34740","34980","39740","24020","13460","47900","43780","22180","26420","12940","40140","45940","14540","39140","48620","40900","11100","49020","17780","29620","14260","41740","10580","45300","46060","12620","15540","40980","22520","36100","19660","49180","31540","36540","13780","21140","39340","35660","27340","44100","21340","38900","48140","41620","31140","41180","13140","32580","37460","37340","22420","26900","37900","42100","27500","36220","27980","16980","22500","47580","30460","40380","31420","28020","49620","49740","10740","36420","42540","27140","23580","43620","12580","47300","31080","22020","12100","16700","16820","44700","11460","29540","25180","14500","13740","25260","39540","39300","41500","28420","42140","26580","47260","24140","32780","46140","16620","33740","21500","38860","00000","44060","45820","18580","28700","39820","28140","46340","37980","12220","48060","25860","20500","23420","27100","36740","22900","26820","30980","29180","41860","31700","27780","13820","12060","37100","22660","29820","20100","41700","49660","46700","17820","16860","12700","42200","15980","34940","48660","28940","17460","27260","17900","26980","34580","44140","23540","12540","35980","10900","17980","33660","47380","29700","34060","40060","14460","35380","17020","12020","16740","47220","19300","34820","29340","29460","41100","24580","36780","26620","22140","19740","38940","15940","14860","24660","45460","32820","46540","33460","33340","19820","14010","19380","14020","45780","49340","15680","16540","33780","12980","38300","21780","10420","45060","42220","17140","12260","16060","33860","19780","15180","44180","11700","10180","24340","29200","37860","40220","30780","41540","31180","39580","24780","35300","45220","17300","17660","22220","33100","48700","40420","29740","24860","28660","35620","23060","47940","16300","35840","19100","21660","19340","18140","41940","42340","27740","43300","38060","25420","25540","30340","15500","42660","33700","15380","41420","24540","17420","13980","16580","12420","38220","46520","25940","11540","20700","42020","36260","43340","43900"}
#There are too many labels for the education,so i did clubbed some together for good visualization in t
def combine_education_levels(labels, counts):
    combined_labels = []
    combined_counts = []
    below_high_school_labels = ["Below High School"]
    below_high_school_count = 0
    for label, count in zip(labels, counts):
        if label in below_high_school_labels:
            below_high_school_count += count
        else:
            combined_labels.append(label)
            combined_counts.append(count)
    combined_labels.append("Below High School")
    combined_counts.append(below_high_school_count)
    return combined_labels, combined_counts
#this is the main streamlit code where i created a us map to point all the metropolitean regions and different graphs for the variables.I made a year and cbsa selection dropbox so the corresponding graphs will be shown in the dashboard
import streamlit as st
import pandas as pd
import ast
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

# Function to plot HEFAMINC counts
def plot_hefaminc_counts(subset, cbsa, year, ax):
    hefaminc_counts_str = subset['HEFAMINC_counts'].iloc[0]
    hefaminc_counts = ast.literal_eval(hefaminc_counts_str)

    income_categories, counts = zip(*sorted([(hefaminc_dict[code], count) for code, count in hefaminc_counts.items()], key=lambda x: x[1], reverse=True))

    income_categories = list(income_categories)[::-1]
    counts = list(counts)[::-1]

    ax.barh(income_categories, counts)
    ax.set_xlabel('Count')
    ax.set_ylabel('Income Category(in $)')
    ax.set_title(f'HEFAMINC Counts for CBSA {cbsa} - Year {year}')

# Function to plot HRNUMHOU counts
def plot_hrnumhou_counts(subset, cbsa, year, ax):
    hrnumhou_counts_str = subset['HRNUMHOU_counts'].iloc[0]
    hrnumhou_counts = ast.literal_eval(hrnumhou_counts_str)

    sorted_counts = {k: v for k, v in sorted(hrnumhou_counts.items(), key=lambda item: item[1], reverse=True)}

    ax.bar(sorted_counts.keys(), sorted_counts.values())
    ax.set_xlabel('Number of Household People')
    ax.set_ylabel('Count')
    ax.set_title(f'HRNUMHOU Counts for CBSA {cbsa} - Year {year}')

# Function to plot PRCOW1 counts
def plot_prcow1_counts(subset, cbsa, year, ax):
    prcow1_counts_str = subset['PRCOW1_counts'].iloc[0]
    prcow1_counts = ast.literal_eval(prcow1_counts_str)

    non_zero_counts = {code: count for code, count in prcow1_counts.items() if count != 0}
    non_zero_labels = [prcow1_dict[code] for code in non_zero_counts if code in prcow1_dict]

    if non_zero_counts:
        ax.pie(non_zero_counts.values(), labels=non_zero_labels, autopct='%1.1f%%', startangle=140)
        ax.set_title(f'PRCOW1 Counts for CBSA {cbsa} - Year {year}')

# Function to plot PEMARITL counts
def plot_pemaritl_counts(subset, cbsa, year, ax):
    pemaritl_counts_str = subset['PEMARITL_counts'].iloc[0]
    pemaritl_counts = ast.literal_eval(pemaritl_counts_str)

    pemaritl_counts = {k: pemaritl_counts.get(k, 0) for k in pemaritl_dict1}

    sorted_counts = sorted(pemaritl_counts.items(), key=lambda item: item[1], reverse=True)

    sorted_labels, sorted_counts = zip(*sorted_counts)
    sorted_labels = [pemaritl_dict[code] for code in sorted_labels]

    # Create numerical x positions for the bars
    x_pos = range(len(sorted_labels))

    # Determine the width of each bar
    bar_width = 0.8

    # Add half-bar width to each x position
    x_pos_adjusted = [pos + bar_width / 2 for pos in x_pos]

    ax.bar(x_pos_adjusted, sorted_counts, align='center', width=bar_width)
    ax.set_xlabel('Marital Status')
    ax.set_ylabel('Count')
    ax.set_title(f'PEMARITL Counts for CBSA {cbsa} - Year {year}')
    ax.set_xticks(x_pos_adjusted)  # Set the tick positions
    ax.set_xticklabels(sorted_labels, rotation=45, ha='right')  # Set the tick labels with rotation



# Function to plot PEEDUCA counts
def plot_peeduca_counts(subset, cbsa, year, ax):
    peeduca_counts_str = subset['PEEDUCA_counts'].iloc[0]
    peeduca_counts = ast.literal_eval(peeduca_counts_str)

    peeduca_counts = {k: peeduca_counts.get(k, 0) for k in peeduca_dict1}

    sorted_counts = sorted(peeduca_counts.items(), key=lambda item: item[1], reverse=True)

    sorted_labels, sorted_counts = zip(*sorted_counts)
    sorted_labels = [peeduca_dict[code] for code in sorted_labels]

    combined_labels, combined_counts = combine_education_levels(sorted_labels, sorted_counts)

    ax.pie(combined_counts, labels=combined_labels, autopct='%1.1f%%', startangle=140)
    ax.set_title(f'PEEDUCA Distribution for CBSA {cbsa} - Year {year}')

# Function to plot PESEX counts
def plot_pesex_counts(subset, cbsa, year, ax):
    pesex_counts_str = subset['PESEX_counts'].iloc[0]
    pesex_counts = ast.literal_eval(pesex_counts_str)

    genders, counts = zip(*sorted([(pesex_dict[code], count) for code, count in pesex_counts.items()], key=lambda x: x[1], reverse=True))

    genders = list(genders)[::-1]
    counts = list(counts)[::-1]

    ax.bar(genders, counts)
    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')
    ax.set_title(f'PESEX Counts for CBSA {cbsa} - Year {year}')

selected_year = st.sidebar.selectbox('Select Year', sorted(df['YYYY'].unique()))

# Filter the dataset based on the selected year
filtered_df = df[df['YYYY'] == selected_year]

# Create Plotly scatter map
fig = px.scatter_mapbox(filtered_df, lat='Latitude', lon='Longitude', hover_name='CBSA')

# Update layout to use Mapbox
fig.update_layout(mapbox_style="open-street-map", mapbox_zoom=3, mapbox_center={"lat": 37.0902, "lon": -95.7129})

# Display the figure
st.plotly_chart(fig)

# Display the plots for the selected CBSA and year
selected_cbsa = st.sidebar.selectbox('Select CBSA', sorted(filtered_df['CBSA'].unique()))

subset = filtered_df[filtered_df['CBSA'] == selected_cbsa]
#this code is for the order of the graphs..so there will be 3 rows and 2 columns of graphs
if len(subset) > 0:
    fig, axes = plt.subplots(3, 2, figsize=(15, 15))
    plot_functions = [plot_hefaminc_counts, plot_hrnumhou_counts, plot_prcow1_counts, plot_pemaritl_counts, plot_peeduca_counts, plot_pesex_counts]
    titles = ['HEFAMINC', 'HRNUMHOU', 'PRCOW1', 'PEMARITL', 'PEEDUCA', 'PESEX']
    for i, plot_func in enumerate(plot_functions):
        row = i // 2
        col = i % 2
        plot_func(subset, selected_cbsa, selected_year, ax=axes[row, col])  # Pass 'ax' instead of 'axes'
        axes[row, col].set_title("")  # Clear any existing title
        axes[row, col].set_title(f"{titles[i]} Counts for {selected_cbsa} - Year {selected_year}")  # Set the new title
    plt.tight_layout()
    st.pyplot(fig)
else:
    st.write("No data available for the selected CBSA and year.")