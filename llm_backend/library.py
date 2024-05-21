from llmware.library import Library
from llmware.setup import Setup
from llmware.configs import LLMWareConfig


def parsing_documents_into_library(library_name):

    print(f"\nParsing Files into Library")

    #   create new library
    print (f"\ncreating library {library_name}")
    library = Library().create_new_library(library_name)

    ingestion_folder_path = './data'

    parsing_output = library.add_files(ingestion_folder_path)

    library_path = library.library_main_path
    print(f"saved at folder path - {library_path}")

    return parsing_output


if __name__ == "__main__":

    LLMWareConfig().set_active_db("sqlite")

    library_name = "compiler_design"
    output = parsing_documents_into_library(library_name)