import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import string



class WordCount(object):
    def __init__(self, language="spanish"):
        if isinstance(language, str):
            self.language=language
        else:
            raise TypeError("Language must be a str object.")

    def remove_ampersand(self, input_text):
        return re.sub(r'&amp;','', input_text)

    def remove_punctuation(self, input_text):
        # Make translation table, remove punctuation
        return input_text.translate(str.maketrans('', '', string.punctuation))

    def remove_urls(self, input_text):
        return re.sub(r'http.?://[^\s]+[\s]?','', input_text)

    def remove_mentions(self, input_text):
        return re.sub(r'@\w+','', input_text)

    def remove_hashtags(self, input_text):
        return re.sub(r'#\w+','', input_text)

    def remove_rt(self, input_text):
        return re.sub(r'\brt\b','', input_text)

    def remove_digits(self, input_text):
        return re.sub(r'\d+','', input_text)

    def to_lower(self, input_text):
        return input_text.lower()

    def remove_stopwords(self, input_text):
        #Add stopwords in spanish from nltk
        stopwords_list = set(stopwords.words(self.language))
        words = word_tokenize(input_text)
        clean_words = [w for w in words if w not in  stopwords_list and len(w)>1]
        return ' '.join(clean_words)

    def get_number_of_words(self, input_text):
        return len(str(input_text).split())

    def word_counter(self, list_of_words):
        count_vectorizer = CountVectorizer()
        vectorized_words= count_vectorizer.fit_transform(list_of_words)
        #Create a list with the word and the frecuency
        word_counted=list(zip(count_vectorizer.get_feature_names(),vectorized_words.toarray().sum(axis=0)))
        word_counted.sort(key=lambda x: x[1], reverse = True)
        return word_counted

    def transform(self, input_text, number_of_words=20):
        if not isinstance(input_text, str):
            raise TypeError("input_text must be a str object.")

        else:
            input_text=self.remove_ampersand(input_text)
            input_text=self.remove_mentions(input_text)
            input_text=self.remove_hashtags(input_text)
            input_text=self.remove_urls(input_text)
            input_text=self.remove_digits(input_text)
            input_text=self.remove_punctuation(input_text)
            input_text=self.to_lower(input_text)
            input_text=self.remove_rt(input_text)
            clean_text=self.remove_stopwords(input_text)
            words_number=self.get_number_of_words(clean_text)
            list_words=word_tokenize(clean_text)
            k_repeated_words=self.word_counter(list_words)[0:number_of_words]
            #get the frequency in %
            return [(i[0],round((i[1]/words_number)*100,2)) for i in k_repeated_words]
