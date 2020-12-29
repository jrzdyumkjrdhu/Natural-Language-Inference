import pickle

import scipy
from sklearn.feature_extraction.text import TfidfVectorizer


def TFIDF_features(premises, hypotheses, lang, mode):
    corpus = [prem + ' ' + hyp for (prem, hyp) in zip(premises, hypotheses)]

    if mode == "train":
        TFIDF_vect = TfidfVectorizer()
        TFIDF_vect.fit(corpus)

        with open('model/TFIDF_{}.pickle'.format(lang), "wb") as file:
            pickle.dump(TFIDF_vect, file)

    elif mode == "test":
        with open('model/TFIDF_{}.pickle'.format(lang), "rb") as file:
            TFIDF_vect = pickle.load(file)

    tfidf_premises = TFIDF_vect.transform(premises)
    tfidf_hypotheses = TFIDF_vect.transform(hypotheses)

    # tfidf_feature_array = scipy.sparse.hstack((tfidf_premises, tfidf_hypotheses))
    tfidf_feature_array = scipy.sparse.csc_matrix.multiply(tfidf_premises, tfidf_hypotheses)

    return tfidf_feature_array
