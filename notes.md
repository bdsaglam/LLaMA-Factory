## Install

```sh
uv sync --extra torch --extra metrics --prerelease=allow
```

## Token stats

```sh
python token_stats.py --model meta-llama/Meta-Llama-3-8B-Instruct --dataset bdsaglam/web_nlg-erx-concat-chat --split train
```

## SFT

```sh
export CUDA_VISIBLE_DEVICES=3
uv run --prerelease=allow llamafactory-cli train examples/train_lora/erx-llama-3-8b.yaml
```

## Chat

```sh
export CUDA_VISIBLE_DEVICES=3
llamafactory-cli chat examples/inference/erx-llama-3-8b.yaml
```

## Inference

```sh
export CUDA_VISIBLE_DEVICES=3
export API_PORT=8008
llamafactory-cli api examples/inference/erx-llama-3-8b.yaml
```

## Publish

```sh
huggingface-cli upload bdsaglam/erx-llama-3-8b saves/erx-llama-3-8b/sft
```

> [!WARNING]
> Merging with llama-factory didn't work.

```sh
export CUDA_VISIBLE_DEVICES=3
llamafactory-cli export examples/merge_lora/erx-llama-3-8b.yaml
```


## SFT Medium

```sh
export CUDA_VISIBLE_DEVICES=3
uv run --prerelease=allow llamafactory-cli train examples/train_lora/erx-llama-3-8b-medium.yaml
huggingface-cli upload bdsaglam/erx-llama-3-8b-medium saves/erx-llama-3-8b-medium/sft
```

## SFT High

```sh
export CUDA_VISIBLE_DEVICES=3
uv run --prerelease=allow llamafactory-cli train examples/train_lora/erx-llama-3-8b-high.yaml
huggingface-cli upload bdsaglam/erx-llama-3-8b-high saves/erx-llama-3-8b-high/sft
```
