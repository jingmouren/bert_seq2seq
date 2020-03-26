##通用配置
bert_chinese_model_path = "./state_dict/bert-base-chinese-pytorch_model.bin"
base_chinese_bert_vocab = "./state_dict/bert-base-chinese-vocab.txt"
## roberta 模型路径跟字典路径
roberta_chinese_model_path = "./state_dict/roberta_wwm_pytorch_model.bin"
roberta_chinese_vocab = "./state_dict/roberta_wwm_vocab.txt"
max_length=256


## 情感分析相关配置
sentiment_train_corpus_dir = "./corpus/sentiment_data"
sentiment_batch_size = 8
sentiment_lr = 1e-5

## 周公解梦数据路径
dream_train_corpus_path = "./corpus/dream/周公解梦数据.csv"

## 自动标题数据路径
auto_title_train_path = "./corpus/auto_title_data/data.txt"

## 对联数据文件夹路径
duilian_corpus_dir = "./corpus/对联"

## 古诗文件夹路径
poem_corpus_dir = "./corpus/Poetry"

## 藏头诗文件路径
poem_head_corpus_path = "./corpus/藏头诗/tang.npz"