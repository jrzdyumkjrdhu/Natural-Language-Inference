# Natural-Language-Inference

Kaggle submissions for the Natural Language Inference problem https://www.kaggle.com/c/contradictory-my-dear-watson.


* [lstm.ipynb](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/lstm.ipynb): our baseline LSTM submission. Kaggle score 0.44812

* [bert_milestone_version.ipynb](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/bert_milestone_version.ipynb): a basic working BERT model from the milestone presentation. Kaggle score 0.64581

* [roberta_version.ipynb](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/roberta_version.ipynb): an improved submission that uses tf-xlm-roberta-large. Kaggle score 0.80500

* [roberta_xnli_version.ipynb](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/roberta_xnli_version.ipynb): an attempt to use a model trained specifically for NLI. Kaggle score 92050

* [xnli_is_bad.ipynb](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/xnli_is_bad.ipynb): the script comparing the xnli dataset to the Kaggle datasets

* [distilbert.ipynb](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/distilbert.ipynb): all further experiments with distilbert. Notebook includes data augmentation (augmented dataset can be found [there](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/data) in .pkl files), SWA and Cyclic Learning Rate)

* [logistic regression](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/logistic_regression): experiments with most simple baseline -- tf-idf + logistic regression. Didn't achieve any results (0.33 accuracy on validation data), wasn't uploaded to Kaggle, wasn't mentioned in presentation

* [diff_pruning.ipynb](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/diff_pruning.ipynb): attempt to implement [diff pruning](https://arxiv.org/abs/2012.07463), didn't increase accuracy on Kaggle, wasn't mentioned in presentation

* [watson_presentation.pdf](https://github.com/jrzdyumkjrdhu/Natural-Language-Inference/blob/main/watson_presentation.pdf): presentation of our project

Launch: 
* better upload needed notebook to Kaggle and run it there since all experiments were conducted only on Kaggle
* for DistilBERT experiments, upload .pkl files to Kaggle or ask for access to private Kaggle dataset [there](t.me/kuzyaka)
