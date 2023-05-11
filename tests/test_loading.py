from unittest import TestCase

from confusionwords import ConfusionSets 

class TestLoading(TestCase):
    def setUp(self):
        pass

    def test_words_get_loaded(self):
        assert ('autentiske' in ConfusionSets["da"].get_filter_dictionary()['ADJ']['autentisk'])