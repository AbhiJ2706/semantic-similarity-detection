### Semantic Similarity Checker

Determines the semantic similarity between a ground truth input and an output from an LLM. 

The ground truth input can be supplied by file or through standard input.

The LLM output can be supplied by file, standard input, or through the OpenAI API which calls on ChatGPT with a user-supplied prompt.

### Usage:

```                        
$ python similarity.py

usage: SimilarityChecker [-h] [--ground-truth-filename GROUND_TRUTH_FILENAME] [--llm-output-filename LLM_OUTPUT_FILENAME]
                         [--llm-output-prompt LLM_OUTPUT_PROMPT] --ground-truth-input [{stdin,file}]) (--llm-input [{stdin,file,gpt}]
```

### Documentation:

```
python similarity.py -h

usage: SimilarityChecker [-h] [--ground-truth-filename GROUND_TRUTH_FILENAME] [--llm-output-filename LLM_OUTPUT_FILENAME]
                         [--llm-output-prompt LLM_OUTPUT_PROMPT] --ground-truth-input [{stdin,file}]) (--llm-input [{stdin,file,gpt}]

Determines the similairty between a ground truth passage and an LLM output

optional arguments:
  -h, --help            show this help message and exit
  --ground-truth-filename GROUND_TRUTH_FILENAME, -gtf GROUND_TRUTH_FILENAME
                        File name for ground truth input. Only required if file input type is selected.
  --llm-output-filename LLM_OUTPUT_FILENAME, -ltf LLM_OUTPUT_FILENAME
                        File name for LLM input. Only required if file input type is selected.
  --llm-output-prompt LLM_OUTPUT_PROMPT, -ltp LLM_OUTPUT_PROMPT
                        Prompt for LLM input. Only required if GPT input type is selected.
  --ground-truth-input [{stdin,file}]
                        Choice of input for ground truth.
  --llm-input [{stdin,file,gpt}]
                        Choice of input for LLM output.
```

