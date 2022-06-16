"""
Used for appending extra routes after initial generation.
"""
from prefect_collection_generator.gql import GraphQLGenerator

# UPDATE THIS SECTION
service_name = ""  # e.g. GitHub
base_directory = ".."
overwrite = False
root_to_op_types = {"query": [], "mutations": []}

graphql_generator = GraphQLGenerator(
    service_name, base_directory=base_directory, overwrite=overwrite
)
for root_type, op_types in root_to_op_types.items():
    graphql_generator.generate_config_files(root_type, op_types=op_types)
    graphql_generator.generate_op_files(root_type, op_types=op_types)
graphql_generator.generate_docs_files()
