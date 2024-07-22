# Semantic Similarity Checker

This program determines the semantic similarity between a ground truth input and an output from an LLM. The semantic similarity is a measure of how well the meanings of two texts match. When comparing a ground truth text and the output of an LLM, the semantic similarity can provide an indication of how truthful an LLM's output is. By measuring this, we can determine how well the LLM can understand user prompts and how accurate its responses are. This allows us limit LLM hallucinations and inprove the LLM's ability to serve users.

## Usage:

The user must supply the ground truth input, and the output from an LLM. This is done throught the command line.

The ground truth input can be supplied by file or through standard input.

The LLM output can be supplied by file, standard input, or through the OpenAI API which calls on ChatGPT with a user-supplied prompt.

### Command:

```                        
$ python similarity.py

usage: SimilarityChecker [-h] [--ground-truth-filename GROUND_TRUTH_FILENAME] [--llm-output-filename LLM_OUTPUT_FILENAME]
                         [--llm-output-prompt LLM_OUTPUT_PROMPT] --ground-truth-input [{stdin,file}]) (--llm-input [{stdin,file,gpt}]
```

### Example:

```
$ python similarity.py --ground-truth-input file --ground-truth-filename input/ground_truth.txt --llm-input file --llm-output-filename input/llm_output.txt
Semantic relationship is neutral [=0.7144]
$
```

## Documentation:

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
  --ground-truth-input [{stdin,file}], -gti [{stdin,file}]
                        Choice of input for ground truth.
  --llm-input [{stdin,file,gpt}], -li [{stdin,file,gpt}]
                        Choice of input for LLM output.
```

