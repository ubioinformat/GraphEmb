import argparse
import logging
import os
import shutil
import subprocess  as sp
import re
import helper_functions_DTI2Vec as hf


######################################## START MAIN #########################################
#############################################################################################
def main():
	# get the parameters from the user
	parser = argparse.ArgumentParser()
	parser.add_argument("dbPath", help="Path to the database interaction lits",
						default = '/home/margaret/data/jfuente/DTI/Data/BIOSNAP/ChG-Miner_miner-chem-gene/ChG-Miner_miner-chem-gene.tsv',
						type=str)
	parser.add_argument("-v", "--verbose", dest="verbosity", action="count", default=3,
						help="Verbosity (between 1-4 occurrences with more leading to more "
							"verbose logging). CRITICAL=0, ERROR=1, WARN=2, INFO=3, "
							"DEBUG=4")
	args = parser.parse_args()
	# define logging level
	log_levels = {
		0: logging.CRITICAL,
		1: logging.ERROR,
		2: logging.WARN,
		3: logging.INFO,
		4: logging.DEBUG,
	}

	# set the logging info
	level= log_levels[args.verbosity]
	fmt = '[%(levelname)s] %(message)s'
	logging.basicConfig(format=fmt, level=level)

	# sanity check for the DB
	DB_PATH = args.dbPath
	JAR_PATH = '/home/margaret/data/gserranos/SMILESbasedSimilarityKernels/SMILESSimv2.jar'
	# DB_PATH =  './../../DB/Data/BindingDB/tdc_package_preprocessing/BindingDB_max_affinity.tsv'
	paper_cite = 'https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-016-0977-x#Sec19'
	logging.info(f'\n\n{paper_cite}\n')
	logging.info(f'Reading database from: {DB_PATH}')
	db_name = hf.get_DB_name(DB_PATH)

	# read the DB and keep the drugs
	drugs_smiles = hf.read_and_extract_BINDING_smiles(DB_PATH)
	logging.info(f'{len(drugs_smiles)} drugs found')
	
	# write the smiles per file to compute
	tmp_path = hf.write_smile_per_file(drugs_smiles, db_name)
	# compute the scores
	function_name = 'TFIDF'
	logging.info(f'Computing the scores\n This can take several minutes...')
	response = sp.check_call(['java', '-jar', JAR_PATH, tmp_path, function_name])
	if response == 0:
		logging.info('Great succes!\n moving the results to the right place')
		results_folder = os.path.join(os.getcwd() , 'simmatrix')
		destination_folder = './../Data/' + db_name + '/Drug_simmatrix'
		if not os.path.exists(destination_folder):
			os.mkdir(destination_folder)
		_ = shutil.move(results_folder, destination_folder)
		logging.info(f'The right place is: {destination_folder}')






#####+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if __name__ == "__main__":
    main()
#####-------------------------------------------------------------------------------------------------------------
####################### END OF THE CODE ##########################################################################