# Instructions

This folder (`app5`) demonstrates how you can integrate [AgentOps.ai](agentops.ai) for your agents and then get monitoring, metrics and more for your agents. 

# Get Your Gemini AI API Key
You will need to provide your Gemini AI API Key in the `model_config.json` folder. You can get your key from https://aistudio.google.com/app/apikey. Once you have the API Key, please provide that value in the `model_config.json` file for the two Gemini model configurations.

# Application
- `multi-agent-101.py` : This program demonstrates how you can configure two autonomous agents : `quote_writer` and `quote_reader`.

The scenario is as follows:
- The Quote Writer is used to first get a specific quote on life. 
- The Quote Writer then initiates the conversation with the Quote Reviewer.
- The conversation continues for a maximum of two turns.
- We initialize the AgentOps module with the API Key from AgentOps.ai and a tag. This intiatites the metrics getting collected and funelled off to AgentOps.ai, where you can then view the metrics, drill down into a session , see the interaction between agents and more.

# Blog Post
Refer to the following article for a detailed analysis : https://iromin.medium.com/tutorial-multi-agent-interactions-with-autogen-and-gemini-part-5-agentops-a70912486c13
    
# Run the Application
- Setup a Python environment via the `requirements.txt` file that is provided.
  ```
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
- Run the program at the command line for e.g. `$ python multi-agent-101.py`
