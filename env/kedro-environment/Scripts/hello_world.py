from kedro.pipeline import node
from kedro.pipeline import Pipeline
from kedro.io import DataCatalog, MemoryDataSet
from kedro.runner import SequentialRunner

# Preparing data catalog
data_catalog = DataCatalog({'my_salutation':MemoryDataSet()})

# First node
def return_greeting():
    return 'Hello'

return_greeting_node = node(return_greeting, inputs=None, outputs='my_salutation')

# Second node
def join_statements(greeting):
    return f"{greeting} Kedro!"

join_statements_node = node(join_statements, inputs='my_salutation', outputs='my_message')

pipeline = Pipeline([return_greeting_node, join_statements_node])

runner = SequentialRunner()

print(runner.run(pipeline, data_catalog))