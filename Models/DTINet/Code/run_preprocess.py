import argparse
import logging
import subprocess as sp



######################################## START MAIN #########################################
#############################################################################################

def main():
    '''
    run get_coord
    run DTI_{DB} if needed
    run get_all matrix
    '''
    parser = argparse.ArgumentParser() 
    parser.add_argument("-v", "--verbose", dest="verbosity", action="count", default=3,
                    help="Verbosity (between 1-4 occurrences with more leading to more "
                        "verbose logging). CRITICAL=0, ERROR=1, WARN=2, INFO=3, "
                        "DEBUG=4")
    parser.add_argument("dbPath", help="Path to the database output", type=str)
    args = parser.parse_args()
    DB_PATH = args.dbPath
    
    #
    list_of_pys = ['get_edgelists.py']
    if DB_PATH in ['E', 'GPCR', 'IC', 'NR']:
        list_of_pys.append(f'DTI_Yamanishi.py')
    elif DB_PATH in ['BindingDB', 'Davis_et_al']:
        list_of_pys.append(f'DTI_{DB_PATH}.py')
    list_of_pys.append('get_all_matrix.py')
    

    for script in list_of_pys:
        try:
            logging.info(f'Running {script}')
            return_code = sp.check_call(['python3', script, DB_PATH])
            if return_code ==0: 
                logging.info('EXIT CODE 0')
        except sp.CalledProcessError as e:
            logging.info(e.output)
            break


#####+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

if __name__ == "__main__":
    main()
#####-------------------------------------------------------------------------------------------------------------
####################### END OF THE CODE ##########################################################################

