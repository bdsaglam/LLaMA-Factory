import argparse
from collections import defaultdict

import pandas as pd
from datasets import load_dataset
from transformers import AutoTokenizer


def get_token_counts(model_name_or_path: str, dataset_name: str, split: str = "train"):
    # Load the tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

    # Load the dataset
    dataset = load_dataset(dataset_name, split=split)

    # Initialize a dictionary to store token counts
    token_counts = []

    # Iterate through the dataset and count tokens
    for example in dataset:
        tokens = tokenizer.apply_chat_template(example["messages"], tokenize=True)
        token_counts.append(len(tokens))

    # Print the token count statistics
    print(pd.Series(token_counts).describe())


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Get token count statistics for a dataset using a specified tokenizer."
    )
    parser.add_argument("--model", type=str, required=True, help="HuggingFace model name or path")
    parser.add_argument("--dataset", type=str, required=True, help="HuggingFace dataset name")
    parser.add_argument("--split", type=str, default="train", help="Dataset split to use (default: train)")

    args = parser.parse_args()
    get_token_counts(args.model, args.dataset, args.split)
