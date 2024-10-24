# Instructions

This folder (`app8`) demonstrates Group Chat, a single chat comprising one or more agents (Autonomous or Human).

# Get Your Gemini AI API Key
You will need to provide your Gemini AI API Key in the `model_config.json` folder. You can get your key from https://aistudio.google.com/app/apikey. Once you have the API Key, please provide that value in the `model_config.json` file for the two Gemini model configurations.

# Application List
- `group-chat.py` : This program demonstrates a group chat, where we are going to accomplish the task of creating a blog post, creating hashtags for the blog post and then doing a human (manual) review. 
   - `blog_writer_agent` : This agent will generate the blog content for a specific blog topic.
   - `blog_writer_agent` : This agent will generate 3 hashtags for the blog content provided to it. 
   - `user_proxy` : This is a human agent that will review and determine if the chat needs to go on.
 
The key pieces of code is the `GroupChat` and `GroupChatManager` as shown below:

```
# Creating a group chat with 3 agents. 
groupchat = GroupChat(agents=[user_proxy, hashtag_agent, blog_writer_agent ], messages=[], max_round=100)

# Creating a group chat manager and specifying the groupchat to use and the llm to use for determining which agent is next to speak.
# If required, you can provide the `speaker_selection_method` attribute and set it to `round_robin` for another way to select the speakers. 
manager = GroupChatManager(groupchat=groupchat, 
                                   llm_config={
                                    "config_list": config_list_gemini,
                                })

# Initiate the group chat by using the `user_proxy` to send a message to the Group Chat Manager.
user_proxy.initiate_chat(manager, message="Write a blog post on Java language. Ask for it to be reviewed.")
```

# Blog Post
Refer to the blog post over here for a detailed analysis: https://medium.com/google-cloud/tutorial-multi-agent-interactions-with-autogen-and-gemini-part-8-group-chat-511440860129
  
# Run the Applications
- Setup a Python environment via the `requirements.txt` file that is provided.
  ```
  $ python3 -m venv .venv
  $ source .venv/bin/activate
  $ pip install -r requirements.txt
  ```
- Run the program at the command line for e.g. `$ python group-chat.py`

