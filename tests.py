import unittest
import common
# import idiom_savant

class TestDataProcessing(unittest.TestCase):
    # def test_get_puns(self):
    #     puns, taskID = common.get_puns()
    #     self.assertEqual(puns["hom_2250"], {'hom_2250_1': 'A', 'hom_2250_2': 'student', 'hom_2250_3': 'limped', 'hom_2250_4': 'into', 'hom_2250_5': 'class', 'hom_2250_6': 'with', 'hom_2250_7': 'a', 'hom_2250_8': 'lame', 'hom_2250_9': 'excuse', 'hom_2250_10': '.'} )

    # def test_remove_punctuation(self):
    #     puns, taskID = common.get_puns()
    #     p = common.remove_punctuation(puns)
    #     self.assertEqual(p["hom_2250"], {'hom_2250_1': 'A', 'hom_2250_2': 'student', 'hom_2250_3': 'limped', 'hom_2250_4': 'into', 'hom_2250_5': 'class', 'hom_2250_6': 'with', 'hom_2250_7': 'a', 'hom_2250_8': 'lame', 'hom_2250_9': 'excuse'})

    # def test_remove_stopwords(self):
    #     puns, taskID = common.get_puns()
    #     p = common.remove_stopwords(puns)
    #     self.assertEqual(p["hom_2250"], {'hom_2250_1': 'A', 'hom_2250_2': 'student', 'hom_2250_3': 'limped', 'hom_2250_5': 'class','hom_2250_8': 'lame', 'hom_2250_9': 'excuse', 'hom_2250_10': '.'} )

    # def test_lowercase(self):
    #     puns, taskID = common.get_puns()
    #     puns = common.truncate_puns(puns, keep=500)
    #     puns = common.add_pos_tags(puns)
    #     puns = common.remove_stopwords(puns)
    #     puns = common.only_content_words(puns)
    #     print(puns["hom_556"])
    #     print(puns["hom_631"])
    #     puns = common.lowercase(puns)
    #     print(puns["hom_556"])
    #     print(puns["hom_631"])

    # def test_get_pun_tokens(self):
    #     puns, taskID = common.get_puns()
    #     puns = common.add_pos_tags(puns)
    #     for punID, pun in puns.items():
    #         break
    #     print(common.get_pun_tokens(pun, exclude=[], exclude_stopwords=True, return_pos_tags=True))

# class TestIdiomSavant(unittest.TestCase):
    # def test_get_gloss(self):
    #     senses = idiom_savant.get_senses_of_word("sting")
    #     print(idiom_savant.get_gloss_set(senses[0]))

    # def test_word_vector(self):
    #     idiom_savant.word_vector("grey")

if __name__ == '__main__':
    unittest.main()