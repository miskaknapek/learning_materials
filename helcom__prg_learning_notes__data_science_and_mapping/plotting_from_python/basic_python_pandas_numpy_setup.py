import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print( "\n > numpy (np), pandas (pd), matplotlib (plt), and searborn (sns) loaded")



###### loading functions

def load_helcom_shipping_data():
	print( ">>> loading helcom shipping data, returning as 'data' ")
	return pd.read_csv("/Users/miska/Documents/creative/backup_of_works/helcom_work/shipping_lists/data/compiled_shipping_list__via_python_01.csv", sep=";")


def load_pokemon_data():
	print(">>> loading the Pokemon data as 'data'")
	return pd.read_csv("/Users/miska/Documents/prg2/data_science/datascience__datasets/Pokemon.csv")

# data loading functions register

data_loading_functions = { 0 : "undefined",
							1 : load_helcom_shipping_data, 
							2 : load_pokemon_data }




####################

# load some data? 

print(" __ Load some |data|? ")
print("\t press 1 for ship listing data")
print("\t press 2 for Pokemon data")

# select
data_selection_i = input("\n - please select datasource to load : ")
# + do some loading 
data = data_loading_functions[ int( data_selection_i) ]()
