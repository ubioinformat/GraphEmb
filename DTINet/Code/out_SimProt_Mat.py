[INFO] 
		This script needs:
			- all .tsv files
		
		Returns:
			- mat*.txt
			- Similarity_Matrix_Drugs.txt
		
[INFO] Working in output folder for: DrugBank
[INFO] Database: DrugBank
[INFO] Loadding Data from tsv files....
[INFO] ------------------------------
[INFO] Gettin Data from tsv files...
[INFO] Reading from existing files...
[INFO] This network has 8712 drug nodes
[INFO] This network has 12097 protein nodes
[INFO] This network has 7229 disease nodes
[INFO] This network has 5526 side-effect nodes
[INFO] This network has 33564 nodes in total
[INFO] ------------------------------
[INFO] Getting matrix....
[INFO]    - Drug Disease Matrix
[INFO]         * # unique diseases in drugs 7072 from 7229 total nodes
[INFO]         * matrix shape (8712, 7229)
[INFO]         * # drug-disease assoc edges 876655
[INFO]    - Drug Side Effect Matrix
[INFO]         * # unique side effects 5526
[INFO]         * Matrix shape (8712, 5526)
[INFO]         * # drug-side effect assoc edges 117600
[INFO]    - Drug Drug Matrix
[INFO]         * # unique drugs * that interact 4418
[INFO]         * matrix shape (8712, 8712)
[INFO]         * # drug-drug interaction edges 1151193.0
[INFO]    - Protein Protein Matrix
[INFO]         * # unique proteins that interact (in HPRD) 9183; using prot nodes: 12097
[INFO]         * matrix shape (12097, 12097)
[INFO]         * # protein-protein edges 36401.0
[INFO]    - Protein Disease Matrix
[INFO]         * # unique drugs * that interact 6071
[INFO]         * matrix shape (12097, 7229)
[INFO]         * # protein-disease edges 12384997
[INFO]    - Protein Drug Interaction Matrix (DTIs)
[INFO]         * # unique drugs in DTI info 8042; # unique drugs in DTI info 5141
[INFO]         * matrix shape (8712, 12097)
[INFO]         * # drug-protein edges 25912
[INFO] ------------------------------
[INFO] Drug Similarity matrix....
[INFO] Matrix already in folder
[INFO] ------------------------------
[INFO] Protein Similarity Matrix....
[INFO] Calculating SW
[INFO] Creating tmp folder: /tmp/SmithWaterman/DrugBank
