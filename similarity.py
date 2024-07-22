from sentence_transformers import SentenceTransformer

import argparse

from provider import *


def similarity(ground_truth, llm_output):
    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    ground_truth_embedding = embedder.encode(ground_truth, convert_to_tensor=True)

    llm_output_embedding = embedder.encode(llm_output, convert_to_tensor=True)

    similarity_score = embedder.similarity(llm_output_embedding, ground_truth_embedding)[0].cpu().numpy()[0]

    if similarity_score > 0.8:
        print(f"Semantic relationship is strong [={similarity_score:0.4f}]")
    elif similarity_score > 0.6:
        print(f"Semantic relationship is neutral [={similarity_score:0.4f}]")
    else:
        print(f"Semantic relationship is weak [={similarity_score:0.4f}]")


if __name__ == "__main__":
    ground_truth_inputs = {
        "stdin": StandardInputProvider(),
        "file": FileInputProvider()
    }

    llm_output_inputs = {
        "stdin": StandardInputProvider(),
        "file": FileInputProvider(),
        "gpt": ChatGPTInputProvider()
    }

    parser = argparse.ArgumentParser(
        prog='SimilarityChecker',
        description='Determines the similairty between a ground truth passage and an LLM output',
    )

    parser.add_argument(
        "--ground-truth-filename", 
        "-gtf", 
        type=argparse.FileType('r'), 
        required=False, 
        help="File name for ground truth input. Only required if file input type is selected."
    )

    parser.add_argument(
        "--llm-output-filename", 
        "-ltf", 
        type=argparse.FileType('r'), 
        required=False,
        help="File name for LLM input. Only required if file input type is selected."
    )

    parser.add_argument(
        "--llm-output-prompt", 
        "-ltp",
        type=str,
        required=False,
        help="Prompt for LLM input. Only required if GPT input type is selected."
    )

    ground_truth_group = parser.add_mutually_exclusive_group(required=True)

    ground_truth_group.add_argument(
        "--ground-truth-input", 
        choices=ground_truth_inputs, 
        default="file", 
        nargs='?',
        help="Choice of input for ground truth."
    )

    llm_output_group = parser.add_mutually_exclusive_group(required=True)

    llm_output_group.add_argument(
        "--llm-input", 
        choices=llm_output_inputs, 
        default="file", 
        nargs='?',
        help="Choice of input for LLM output."
    )

    args = parser.parse_args()

    if args.ground_truth_input == 'file':
        if not args.ground_truth_filename:
            parser.error('--ground-truth-filename is required when ground truth input type is "file".')
        ground_truth_input = ground_truth_inputs[args.ground_truth_input].provide(file=args.ground_truth_filename)
    else:
        ground_truth_input = ground_truth_inputs[args.ground_truth_input].provide()
    
    if args.llm_input == 'file':
        if not args.llm_output_filename:
            parser.error('--llm-output-filename is required when llm input type is "file".')
        llm_input = llm_output_inputs[args.llm_input].provide(file=args.llm_output_filename)
    elif args.llm_input == 'gpt':
        if not args.llm_output_prompt:
            parser.error('--llm-output-prompt is required when llm input type is "prompt".')
        llm_input = llm_output_inputs[args.llm_input].provide(prompt=args.llm_output_prompt)
    else:
        llm_input = llm_output_inputs[args.llm_input].provide()
    
    similarity(ground_truth_input, llm_input)
