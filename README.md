# Tweet NER

## Objective:
- Detect Brand Entities from Tweets

## Datasets:
Found a few open source datasets that we may use to experiment. They are mainly labeled in the BIO format
1. WNUT16 [[Link]](https://noisy-text.github.io/2016/ner-shared-task.html)
2. WNUT17 [[Link]](http://noisy-text.github.io/2017/files/wnut17train.conll)
3. Broad Twitter Corpus [[Link]](https://github.com/GateNLP/broad_twitter_corpus) [[Paper]](https://www.aclweb.org/anthology/C16-1111.pdf)
    
## Approaches
1. [Spacy pretrained model](https://spacy.io/usage/spacy-101#annotations-ner)
2. [Huggingface NER pipeline](https://huggingface.co/transformers/task_summary.html#named-entity-recognition)
3. [Bidirectional LSTM-CRF Models for Sequence Tagging](https://arxiv.org/pdf/1508.01991.pdf)
4. [Token Classification with BERTweet](https://arxiv.org/pdf/2005.10200.pdf)

## Prelim results
1. [Spacy pretrained model](https://spacy.io/usage/spacy-101#annotations-ner)

2. [Huggingface NER pipeline](https://huggingface.co/transformers/task_summary.html#named-entity-recognition)

3. Bidirectional LSTM-CRF Models for Sequence Tagging [[Paper]](https://arxiv.org/pdf/1508.01991.pdf) [[Notebook]](notebooks/03_bi_lstm_crf.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github.com/stephenleo/twitter-ner/blob/main/notebooks/03_bi_lstm_crf.ipynb)

| Dataset | RNN Layer | Hidden Units |  LR  | Overall F1 | Company Precision | Company Recall | Company F1 |
|---------|:---------:|:------------:|:----:|:----------:|:-----------------:|:--------------:|:----------:|
| WNUT16  |  Bi-LSTM  |      64      | 0.01 |    0.36    |        0.50       |      0.42      |    0.45    |
| WNUT16  |  Bi-LSTM  |      128     | 0.01 |    0.35    |        0.52       |      0.39      |    0.45    |
| WNUT16  |   Bi-GRU  |      64      | 0.01 |    0.35    |        0.56       |      0.37      |    0.45    |

4. [Token Classification with BERTweet](https://arxiv.org/pdf/2005.10200.pdf)
