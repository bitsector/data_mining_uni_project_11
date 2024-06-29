import argostranslate.package
import argostranslate.translate

from_code = "he"  # Language code for Hebrew
to_code = "en"  # Language code for English

# Download and install Argos Translate package
argostranslate.package.update_package_index()
available_packages = argostranslate.package.get_available_packages()
package_to_install = next(
    filter(lambda x: x.from_code == from_code and x.to_code == to_code, available_packages),
    None,  # Added None to handle the case where no package is found
)

if package_to_install is not None:
    argostranslate.package.install_from_path(package_to_install.download())
    # Translate
    translatedText = argostranslate.translate.translate("כן", from_code, to_code)
    print(translatedText)
    translatedText = argostranslate.translate.translate("לא", from_code, to_code)
    print(translatedText)
    translatedText = argostranslate.translate.translate("שחור", from_code, to_code)
    print(translatedText)
    translatedText = argostranslate.translate.translate("לבן", from_code, to_code)
    print(translatedText)
else:
    print(f"No available package for translating from {from_code} to {to_code}.")
