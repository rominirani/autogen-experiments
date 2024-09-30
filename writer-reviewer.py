from autogen import AssistantAgent
import autogen


config_list_gemini = autogen.config_list_from_json(
    "OAI_CONFIG_LIST.json",
)

seed = 25  # for caching

writer = AssistantAgent(
    "assistant", 
    system_message="You are an expert Call for Proposals writer. You will keep improving the CFP until it is perfect. You will receive a list of suggestions from the Reviewer. Please review the list and incorporate the changes. Submit the CFP back to the reviewer for further review. If there are no more suggestions for changes, you can exit",
    llm_config={"config_list": config_list_gemini, "seed": seed}, 
    max_consecutive_auto_reply=3
)

reviewer = AssistantAgent(
    "assistant", 
    system_message="You are an expert reviewer of Call for Proposals. You will keep reviewing the CFP for improving it. Please suggest changes to be made in a bulleted list. If there are no changes, you can mention that.",
    llm_config={"config_list": config_list_gemini, "seed": seed}, 
    max_consecutive_auto_reply=3
)

writer.initiate_chat(
    reviewer,
    message="I would like to write a CFP for a conference. Can you help me improve the following CFP? \n---- \nI would like to discuss about Auotgen at a conference. I will show examples of Autogen works and how it can be a solid framework to write multi-Agent applications.",
)

