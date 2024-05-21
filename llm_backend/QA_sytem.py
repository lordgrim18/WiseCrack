
import os
from llmware.prompts import Prompt
from llmware.configs import LLMWareConfig
from llmware.library import Library
from llmware.retrieval import Query


def prompt_with_sources(model_name, library_name, prompt):
    library = Library().load_library(library_name)
    prompter = Prompt().load_model(model_name)

    query_results = Query(library).query('Compiler Design')
    prompt_instruction = "default_with_context"
    sources4 = prompter.add_source_query_results(query_results)
    response = prompter.prompt_with_source(prompt=prompt, prompt_name=prompt_instruction)[0]["llm_response"]
    print(f"Prompt: {prompt}\n- LLM Response:\n{response}")
    prompter.clear_source_materials()

    return response


if __name__ == "__main__":
    model_name = "llmware/bling-tiny-llama-v0"

    library_name = "compiler_design"

    prompt = "What are Regular Expressions?"

    LLMWareConfig().set_active_db("sqlite")

    prompt_with_sources(model_name, library_name, prompt)

