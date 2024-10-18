from autogen import ConversableAgent
import autogen
import pprint

config_list_gemini = autogen.config_list_from_json("model_config.json")

quote_writer = ConversableAgent(
    name="Quote Generator",
    system_message="Your task is to provide famous quotes",
    llm_config = {"config_list" : config_list_gemini},
    code_execution_config = False,
    human_input_mode = "NEVER",
    silent=True,
)

quote_reviewer = ConversableAgent(
    name="Quote Reviewer",
    system_message="Your task is to review a famous quote and provide your comments briefly in a list.",
    llm_config = {"config_list" : config_list_gemini},
    code_execution_config = False,
    human_input_mode = "NEVER",
    silent=True,
)

reply = quote_writer.generate_reply(messages=[{"content": "Give me a quote by Albert Einstein", "role": "user"}])

result = quote_writer.initiate_chat(quote_reviewer,message=reply['content'], 
                                    max_turns=2,
                                    summary_method="reflection_with_llm",)

pprint.pprint(result.summary)
pprint.pprint(result.chat_history)
pprint.pprint(result.cost)

