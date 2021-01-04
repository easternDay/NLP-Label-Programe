from gensim.models import word2vec
from gensim.models import KeyedVectors
import logging
import os

# 主函数
if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence(u'./待标注分词字典.txt')
    model = word2vec.Word2Vec(
        sentences, size=200, window=10, min_count=6, sg=1, hs=1, iter=10, workers=25)
    model.save(u'./词向量模型.word2vec')
    """
    if os.path.exists("词向量模型.word2vec"):
        # 增量更新
        model = word2vec.Word2Vec.load("./词向量模型.word2vec")
        model.train(sentences, total_examples=model.corpus_count,
                    epochs=model.epochs)
        model.init_sims(replace=True)
        model.save("词向量模型.word2vec")
    else:
        # 初始化
        model = word2vec.Word2Vec(
            sentences, size=200, window=10, min_count=6, sg=1, hs=1, iter=10, workers=25)
        model.save(u'./词向量模型.word2vec')
    """
