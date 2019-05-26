from django.test import TestCase

from word_counter.word_counter_skeleton import WordCount

class TestWordCounter(TestCase):

    def test_to_lower(self):
        self.assertEqual(WordCount().to_lower("HeLlo wORLd"), "hello world")

    def test_to_lower_string_of_numbers(self):
        self.assertEqual(WordCount().to_lower("89 65"), "89 65")

    def test_to_lower_with_int(self):
        with self.assertRaises(AttributeError):
            WordCount().to_lower(89)

    def test_to_lower_empty_string(self):
        self.assertEqual(WordCount().to_lower(""), "")

    def test_remove_punctuation(self):
        self.assertEqual(WordCount().remove_punctuation("hello, my. name: is... Peter"), "hello my name is Peter")

    def test_remove_punctuation_with_int(self):
        with self.assertRaises(AttributeError):
            WordCount().remove_punctuation(89)

    def test_remove_punctuation_no_puctuation(self):
        self.assertEqual(WordCount().remove_punctuation("ñ j PO í"), "ñ j PO í")

    def test_remove_digits(self):
        self.assertEqual(WordCount().remove_digits("h3llo m8 i 345 you"), "hllo m i  you")

    def test_remove_digits_number(self):
        with self.assertRaises(TypeError):
            WordCount().remove_digits(89)

    def test_remove_digits_string_with_only_digits(self):
        self.assertEqual(WordCount().remove_digits("42764572572 237489728"), " ")

    def test_remove_stopwords(self):
        self.assertEqual(WordCount().remove_stopwords("el chico a la calle de siempre"), "chico calle siempre")

    def test_remove_stopwords_without_stopwords(self):
        self.assertEqual(WordCount().remove_stopwords("chico calle perro siempre"), "chico calle perro siempre")

    def test_word_counter(self):
        self.assertEqual(WordCount().word_counter(['dime', 'hola', 'que', 'tal', 'hola', 'que', 'que', 'me', 'dices']), [('que', 3), ('hola', 2), ('dices', 1), ('dime', 1), ('me', 1), ('tal', 1)])

    def test_word_counter_list_of_numbers(self):
        with self.assertRaises(AttributeError):
            WordCount().word_counter([6, 7, 98])

    def test_word_counter_string(self):
        with self.assertRaises(ValueError):
            WordCount().word_counter("hola que tal pepe")

    def test_word_counter_empty_array(self):
        with self.assertRaises(ValueError):
            WordCount().word_counter([])

    def test_cleaned_word_counter(self):
        self.assertEqual(WordCount().transform("3L niño 23 juega, niÑo bonito 432 ella salt0. Y niño salt3 juega baila"), [('niño', 33.33), ('juega', 22.22), ('salt', 22.22), ('baila', 11.11), ('bonito', 11.11)])

    def test_cleaned_word_counter_only_numbers(self):
        with self.assertRaises(ValueError):
            WordCount().transform("2323378264378 3084298239482")

    def test_cleaned_word_counter_numbers_with_words(self):
        self.assertEqual(WordCount().transform("2323pisto264378 30842a77878 3jamon482"), [('jamon', 50.0), ('pisto', 50.0)])

    def test_cleaned_word_counter_only_punctuation(self):
        with self.assertRaises(ValueError):
            WordCount().transform(".,..,:{}[]")

    def test_cleaned_word_counter_only_stopwords(self):
        with self.assertRaises(ValueError):
            WordCount().transform("a el entre contra de donde")
