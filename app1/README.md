# Instructions

This folder (`app1`) demonstrates how to get started with [Autogen](https://github.com/microsoft/autogen) framework. 

# Get Your Gemini AI API Key
You will need to provide your Gemini AI API Key in the `model_config.json` folder. You can get your key from https://aistudio.google.com/app/apikey. Once you have the API Key, please provide that value in the `model_config.json` file for the two Gemini model configurations.

# Application List
- `main.py` : Basic program to demonstrate ConversableAgent that integrates Google Gemini and sends across a prompt.
- `mutli-agent-101.py` : This program demonstrate how to configure 2 ConversableAgent's and make them converse back and forth with each other for a few turns.
- `multi-agent-interaction.py` : This program demonstrates how you can configure 2 ConversableAgent's (`CFP Writer` and `CFP Reviwer`) and make them converse iteratively with each other in a feedback loop to improve a Call for Proposal/Papers (CFP).

# Blog Post
Refer to the blog post over here for a detailed analysis: https://medium.com/google-cloud/multi-agent-interactions-using-autogen-with-gemini-a416008e5df6

# Run the Applications
- Setup a Python environment via the `requirements.txt` file that is provided.
  ```
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
- Run any of the programs at the command line for e.g. `$ python multi-agent-interaction.py`
