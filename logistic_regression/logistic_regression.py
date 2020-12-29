import pickle

from sklearn.linear_model import LogisticRegression


def train(train_feature, train_label):
    LR_model = LogisticRegression(random_state=0, max_iter=1000, solver='lbfgs', multi_class='auto')
    LR_model.fit(train_feature, train_label)


    with open('model/LR.pickle', "wb") as file:
        pickle.dump(LR_model, file)

