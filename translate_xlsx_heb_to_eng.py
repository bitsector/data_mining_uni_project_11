import argparse
import re

import argostranslate.package
import argostranslate.translate
import pandas as pd


class DataPreparer:
    def __init__(self, file_path, output_file):
        self.file_path = file_path
        self.output_file = output_file
        self.dataframe = pd.read_excel(self.file_path)
        print(f"Preparing translation packages")
        self.from_code = "he"  # Language code for Hebrew
        self.to_code = "en"  # Language code for English
        # Download and install Argos Translate package
        argostranslate.package.update_package_index()
        available_packages = argostranslate.package.get_available_packages()
        package_to_install = next(
            filter(lambda x: x.from_code == self.from_code and x.to_code == self.to_code, available_packages),
            None,  # Added None to handle the case where no package is found
        )

        if package_to_install is not None:
            argostranslate.package.install_from_path(package_to_install.download())
            # Translate something
            translatedText = argostranslate.translate.translate(
                "אחת שתיים אחת, היי היי, נסיון תרגום", self.from_code, self.to_code
            )
            print(translatedText)
        else:
            print(f"No available package for translating from {self.from_code} to {self.to_code}.")

    def print_dataframe(self):
        print(self.dataframe)

    def save_dataframe_to_excel(self):
        self.dataframe.to_excel(self.output_file, index=False)

    def check_for_hebrew(self):
        # Define a regex pattern for Hebrew characters
        # Define a regex pattern for Hebrew characters
        hebrew_pattern = re.compile(r"[\u0590-\u05FF]+")

        # Iterate through each element in the DataFrame
        for row in self.dataframe.itertuples(index=False):
            for element in row:
                # Convert the element to string to ensure regex can be applied
                element_str = str(element)
                # Search for Hebrew characters in the element
                if hebrew_pattern.search(element_str):
                    translation_suggestion = argostranslate.translate.translate(
                        element_str, self.from_code, self.to_code
                    )
                    print(f"Hebrew text detected: {element_str}, suggested translation: {translation_suggestion}")
                else:
                    print(f"No Hebrew text: {element_str}")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Process and print an Excel file.")
    parser.add_argument("-i", "--input", required=True, help="Input .xlsx file path")
    parser.add_argument("-o", "--output", required=True, help="Output .xlsx file path")
    args = parser.parse_args()
    args_dict = vars(args)
    return args_dict


if __name__ == "__main__":
    args = parse_arguments()
    data_preparer = DataPreparer(args["input"], args["output"])
    data_preparer.print_dataframe()
    data_preparer.save_dataframe_to_excel()
    data_preparer.check_for_hebrew()
