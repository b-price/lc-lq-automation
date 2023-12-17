# llm-dataset-gen
Provides a `LLMDatasetMgr` class for generating and adding data to `.csv` datasets using LLMs (OpenAI API)

## Installation
Install the following packages:
`pip install openai==1.3.5 pandas==2.1.3 python-dotenv==1.0.0`

## Usage
**1. Create a .env file in the root directory of the project and add your OpenAI API key to it:**
```
OPENAI_API_KEY=<your-openai-api-key>
```
**2. Create an empty dataset file using the `create_and_save_empty_dataset` function in utils.py**
```python
from utils import create_and_save_empty_dataset
dataset_columns = ["ID", "Excerpt", "Comment"]
create_and_save_empty_dataset(columns=dataset_columns, filename="./data/Dataset.csv")
```
> Check create_dataset.py for an example. You can skip this step if you already have a dataset file

**3. Create an instance of the `LLMDatasetMgr` class and pass in a `dataset_path`:**
```python
data_filepath = "./data/Dataset.csv"
dataset = LLMDatasetMgr(dataset_path=data_filepath)
```
**4. Call the `add_data` method by providing the `context` and `num_samples` parameters:**
```python
dataset_context="For Context, this dataset represents requirements engineering excerpts and their corresponding Language Construct (LC) and Language Quality (LQ) codings"
dataset.add_data(context=dataset_context, num_samples=1000)
```
- The `add_data` method will automatically overwrite/save the dataset file after appending the new data
- The `context` parameter is the prompt that will be used to generate the data
- The `num_samples` parameter is the number of data samples to generate and add to the dataset

### How It Works
The `LLMDatasetMgr` class is designed to manage a dataset and interact with the OpenAI API to generate new data entries. By leveraging the JSON Mode in the OpenAI API and the `gpt-4-1106-preview` or `gpt-3.5-turbo-1106` model, we can generate new data entries (as JSON Objects) that match the structure of a given dataset, and easily append them to the dataset.

