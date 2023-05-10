from .confusion_set import ConfusionSet
import os
import pkgutil
import json


ConfusionSets = {
    "da": ConfusionSet("danish")
}


# Example of getting and parsing the data in a json file found in the data folder for the package
# the documentation claims that "The resource argument should be in the form of a relative filename, using / as the path separator"
# so in principle you should not need to use the os.path.join anymore
raw_bytes = pkgutil.get_data(__name__, "data/da/dk_small_sub_sample.json")
dict = json.loads(raw_bytes.decode('utf-8'))
print(dict.keys())

# exiting here because you'll have to redo the load_confusionset by using the same pattern as above

exit()


ConfusionSets["da"].load_confusionset_state(os.path.join("da", "dk_small_sub_sample.json"))