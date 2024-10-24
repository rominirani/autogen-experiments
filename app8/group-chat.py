from autogen import ConversableAgent
from autogen import GroupChat
from autogen import GroupChatManager

import autogen
import pprint

config_list_gemini = autogen.config_list_from_json("model_config.json")

user_proxy = autogen.UserProxyAgent(
   name="User_proxy",
   human_input_mode="ALWAYS",
   code_execution_config=False,
   description="A human user capable of working with Autonomous AI Agents.",
)

blog_writer_agent = autogen.AssistantAgent(
    system_message = "You are an expert blog post generator, who generates only 1 paragraph. You do not generate any other content.",
    name="blog_writer_agent",
    llm_config={
        "config_list": config_list_gemini,
    },
    description="""This agent is responsible for generating a blog post based on a topic. Restrict to one paragraph only.
    """,
)

hashtag_agent = autogen.AssistantAgent(
    system_message = "You are an expert hashtag generator only. You generate only 3 hashtags for any input provided to you. You do not generate any other content. ",
    name="hashtag_agent",
    llm_config={
        "config_list": config_list_gemini,
    },
    description="""This agent can only fix and generate hashtags based on content returned by the blog_writer_agent. Do not generate any other content, only hashtags.
    """,
)

groupchat = GroupChat(agents=[user_proxy, hashtag_agent, blog_writer_agent ], messages=[], max_round=100)
manager = GroupChatManager(groupchat=groupchat, 
                                   llm_config={
                                    "config_list": config_list_gemini,
                                })

user_proxy.initiate_chat(manager, message="Write a blog post on Autogen Framework. Ask for it to be reviewed.")
