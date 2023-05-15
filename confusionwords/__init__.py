from .confusion_set import ConfusionSet, DEFAULT_LEMMA_CONFUSION_SET
import pkgutil
import json


ConfusionSets = {
    "da": ConfusionSet("danish")
}


# Example of getting and parsing the data in a json file found in the data folder for the package
# the documentation claims that "The resource argument should be in the form of a relative filename, using / as the path separator"
# so in principle you should not need to use the os.path.join anymore

raw_bytes = pkgutil.get_data(__name__, "data/da/da_small_confusion_set.json")
dict = json.loads(raw_bytes.decode('utf-8'))
ConfusionSets["da"].load_confusionset_from_dict(dict)