python3 translate_xlsx_heb_to_eng.py -i mmn11_data_mining.xlsx -o mmn11_data_mining_cleaned_db_en.xlsx

python3 make_csv.py mmn11_data_mining_cleaned_db_en.xlsx

python3 make_decision_tree.py --criterion=entropy --visualise --input mmn11_data_mining_cleaned_db_en.csv 