import numpy as np
import pandas as pd
import random

# Currently non-functional
def table_formatter(url):
    
    hp = HTMLTableParser()
    table = hp.parse_url(url)[0][1] # Grabbing the table from the tuple
    table.astype(str)
    
    return table

# Version 0.1
def filterRarity(csv_name):

    # Import the data and separate it by rarity.

    full_loot_table = pd.read_csv(csv_name, dtype = str)
    full_loot_table.drop("Unnamed: 6", axis=1, inplace=True)
    full_loot_table.fillna('---', inplace=True)

    full_loot_table.columns = ['Item', 'Type', 'Rarity','Attunement','Additional','Source']


    # separate table by rarity
    common = (full_loot_table[full_loot_table["Rarity"] == "Common"])
    common.set_index(np.arange(len(common)), drop=False, append=False, inplace=True, verify_integrity=False)
    #common
    
    uncommon = (full_loot_table[full_loot_table["Rarity"] == "Uncommon"])
    uncommon.set_index(np.arange(len(uncommon)), drop=False, append=False, inplace=True, verify_integrity=False)
    #uncommon

    rare = (full_loot_table[full_loot_table["Rarity"] == "Rare"])
    rare.set_index(np.arange(len(rare)), drop=False, append=False, inplace=True, verify_integrity=False)
    #rare

    very_rare = (full_loot_table[full_loot_table["Rarity"] == "Very Rare"])
    very_rare.set_index(np.arange(len(very_rare)), drop=False, append=False, inplace=True, verify_integrity=False)
    #very_rare

    legendary = (full_loot_table[full_loot_table["Rarity"] == "Legendary"])
    legendary.set_index(np.arange(len(legendary)), drop=False, append=False, inplace=True, verify_integrity=False)
    #legendary
    
    all_tables = full_loot_table

    rarity_df_list = [common, uncommon, rare, very_rare, legendary, all_tables]
    
    return rarity_df_list

# Version 0.1
def randomSliceTable(rarity_table, number_of_rows, filterCol, filterTo):
    
    # Check to see if user wants to filter column
    if (filterCol != "none" and filterTo != "none"):
        random_table = (rarity_table[rarity_table[filterCol] == filterTo])
        random_table = random_table.sample(n = number_of_rows)
        random_table.set_index((np.arange(len(random_table)))+1, drop=False, append=False, inplace=True, verify_integrity=False)
    
    # Version 0.2
    else:
        # randomly choose n entries from the selected table
        random_table = rarity_table.sample(n = number_of_rows)
        random_table.set_index((np.arange(len(random_table)))+1, drop=False, append=False, inplace=True, verify_integrity=False)
    
    return random_table

# Version 0.3
def auto_roll(rollable_table, number_of_rolls):
    
    # 1. generate list of random roll numbers.
    # 2. select those numbers from the list as a dataframe
    # 3. return the df of loot
    
    rolls = []
    
    for r in range(number_of_rolls):
        roll = random.randint(1, len(rollable_table))
        rolls.append(roll)
    #print(rolls) # roll results
    
    rolled_loot_table = rollable_table.iloc[rolls]
    return rolled_loot_table
    #return
    
def main():
    loot_table_file = "Magic Items by Rarity - 5e Dungeon Master's Guide (DMG) & Encyclopedia Magica (EM).csv"
    tables = filterRarity(loot_table_file)
    
    # User input
    rarity_table = int(input("Select rarity (0 = common, 4 = legendary, 5 = All tables): "))
    number_of_rows = int(input("Select number of loot rows: "))
    filter_column = "Type"
    if (filter_column != "none"):
        filter_to = input("Select a type of item (Armor, Staff, Wonderous Item, Potion, Weapon, Ring, none): ")
    else:
        filter_to = "none"
        
    # Version 0.3
    auto_roll_YN = input("Do you want to auto-roll loot? (yes/no)")
    if (auto_roll_YN != "no"):
        rollable_table = randomSliceTable(tables[rarity_table], number_of_rows, filter_column, filter_to)
        number_of_rolls = int(input("How many items do you want to roll?"))
        
        rolled_loot_table = auto_roll(rollable_table, number_of_rolls)
        display(rolled_loot_table)
        
    else:
        rollable_table = randomSliceTable(tables[rarity_table], number_of_rows, filter_column, filter_to)
        
        # Display the table created
        display(rollable_table)
    
    

    
main()