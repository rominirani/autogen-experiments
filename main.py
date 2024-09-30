import os
from autogen import AssistantAgent, UserProxyAgent
import autogen


config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
    filter_dict={
        "model": ["gemini-pro"],
    },
)

seed = 25  # for caching

assistant1 = AssistantAgent(
    "assistant", llm_config={"config_list": config_list_gemini, "seed": seed}, max_consecutive_auto_reply=3
)

assistant2 = AssistantAgent(
    "assistant", llm_config={"config_list": config_list_gemini, "seed": seed}, max_consecutive_auto_reply=3
)

assistant2.initiate_chat(
    assistant1,
    message="Tell me a joke about NVDA and TESLA stock prices.",
)
