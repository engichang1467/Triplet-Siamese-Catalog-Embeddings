# Using Triplet Loss and Siamese Neural Networks to Train Catalog Item Embeddings

## Overview

## Dataset

Dataset contains the query text, positive wording of the text and negative wording of the text. The dataset is later extended by using Cohere API to help generate more data to train.

```csv
QUERY_TEXT,POSITIVE,NEGATIVE
desserts, shakes,veggie burger with cheeese
sushi, thai chef fresh rolls, meat lasagna
acai bowl, acai bowl delivered, mint chocolate chip polar pizza
cupcake, carrot, buffalo chicken
consultative approach, apple pie, broccoli
goat cheese, goat cheese salad, lamb biryani
```

- Checkout the data generator app here [![Hugging Face Spaces](https://img.shields.io/badge/🤗%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/mca183/data-generation-cohere)
- Checkout the source code of the data generator app [here](https://github.com/engichang1467/Data-Generator-Cohere)

## References

- [Doordash Engineering Blog: Using Triplet Loss and Siamese Neural Networks to Train Catalog Item Embeddings](https://doordash.engineering/2021/09/08/using-twin-neural-networks-to-train-catalog-item-embeddings/)
