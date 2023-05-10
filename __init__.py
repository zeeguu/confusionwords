from .confusion_set import ConfusionSet
import os

ConfusionSets = {
    "da": ConfusionSet("danish")
}

ConfusionSets["da"].load_confusionset_state(os.path.join("da", "dk_small_sub_sample.json"))