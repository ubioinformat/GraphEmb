import argparse
import logging
import os, sys
from re import search
import pandas as pd
from tqdm import tqdm
from GetDrugsAndGenes import check_drug_in_kegg, getdrug_drugbank


def get_DB_name(path):
	"""
	This function returns the name of the DB.
	"""
	DB_NAMES = ['BIOSNAP', 'BindingDB', 'Davis_et_al', 'DrugBank_FDA', 'E', 'GPCR', 'IC', 'NR']
	for db in DB_NAMES:
		if search(db, path):
			logging.info(f'Database: {db}')
			if db in ['E', 'GPCR', 'IC', 'NR']:
				db = os.path.join('Yamanashi_et_al_GoldStandard', db)
				return db
			else:
				return db
	logging.error(f'Database: {db} not found')
	sys.exit('Please provide a valid database')

def read_and_extract_drugs(path):
	drugs = []
	with open(path, 'r') as f:
		for line in f:
			if not line.startswith('#'):
				drug, _ = line.split('\t')
				drugs.append(drug)
	return drugs

def check_and_create_folder(db_name):
	if not os.path.exists(os.path.join('/home/margaret/data/jfuente/DTI/InputData/DTI2Vec/', db_name)):
		os.mkdir(os.path.join('/home/margaret/data/jfuente/DTI/InputData/DTI2Vec/', db_name))


######################################## START MAIN #########################################
#############################################################################################
def main():
	# define logging level

	# get the parameters from the user
	parser = argparse.ArgumentParser()
	parser.add_argument("dbPath", help="Path to the database interaction lits",
						type=str)
	parser.add_argument("-v", "--verbose", dest="verbosity", action="count", default=3,
						help="Verbosity (between 1-4 occurrences with more leading to more "
							"verbose logging). CRITICAL=0, ERROR=1, WARN=2, INFO=3, "
							"DEBUG=4")
	args = parser.parse_args()
	log_levels = {
		0: logging.CRITICAL,
		1: logging.ERROR,
		2: logging.WARN,
		3: logging.INFO,
		4: logging.DEBUG,
	}
	# set the logging info
	level= log_levels[args.verbose]
	fmt = '[%(levelname)s] %(message)s'
	logging.basicConfig(format=fmt, level=level)

	# sanity check for the DB
	DB_PATH = args.dbPath
	logging.info(f'Reading database from: {DB_PATH}')
	db_name = get_DB_name(DB_PATH)
	
	# read the DB and keep the drugs
	drugs = read_and_extract_drugs(DB_PATH)

	drugs = list(set(drugs))
	logging.info(f'{len(drugs)} drugs found')
	# test if the drugs are on KEGG format/database
	converted_drugs = []
	for drug in tqdm(drugs):
		converted_drugs.append((drug, check_drug_in_kegg(drug)))
		getdrug_drugbank(drug)
	converted_drugs = pd.DataFrame(converted_drugs, columns=['KEGG_ID', 'DrugBank_ID'])
	check_and_create_folder(db_name)
	file_path = os.path.join('/home/margaret/data/jfuente/DTI/InputData/DTI2Vec/', db_name, 'Drugs_Renamed.tsv')
	converted_drugs.to_csv(file_path, sep='\t')