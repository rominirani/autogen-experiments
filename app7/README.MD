# Instructions

This folder (`app7`) demonstrates Sequential Chat, a sequence of chats between two agents, chained together by a carryover mechanism, which brings the summary of the previous chat to the context of the next chat.

# Get Your Gemini AI API Key
You will need to provide your Gemini AI API Key in the `model_config.json` folder. You can get your key from https://aistudio.google.com/app/apikey. Once you have the API Key, please provide that value in the `model_config.json` file for the two Gemini model configurations.

# Application List
- `sequential-agents-101.py` : This program demonstrates a sequential chat, where we will call two agents in sequence:
   - `hashtag_agent` : This agent will generate the hashtags for the content.
   - `title_agent` : This agent will generate a 1-line title for the content. 
- `testpaper-evaluator-sequential.py` : This program demonstrates a sequential chat, where we will communicate to two Autonomous Agents in sequence:
   - `scan_answer_paper_agent` : This Agent will check if the student has submitted answers to each question.
   - `check_answer_paper_agent` : This Agent will check the correctness of the answers and compute a score. 

# Blog Post
Refer to the blog post over here for a detailed analysis: https://medium.com/google-cloud/tutorial-multi-agent-interactions-with-autogen-and-gemini-part-7-sequential-chat-885fe1cc55d0
  
# Run the Applications
- Setup a Python environment via the `requirements.txt` file that is provided.
  ```
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
- Run the program at the command line for e.g. `$ python sequential-agents-101.py` or `$ python testpaper-evaluator-sequential.py`

