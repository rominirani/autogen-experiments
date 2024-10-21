from autogen import ConversableAgent
import autogen
import pprint

config_list_gemini = autogen.config_list_from_json("model_config.json")

article_processor_agent = ConversableAgent(
    name="Article Processor Agent",
    llm_config = {"config_list" : config_list_gemini},
    human_input_mode = "NEVER",
)

hashtag_agent = ConversableAgent(
    name="Hashtag Generator Agent",
    system_message="Your task is to generate hashtags and add that to the message and return the messsage and hashtags",
    llm_config = {"config_list" : config_list_gemini},
    human_input_mode = "NEVER",
)

title_agent = ConversableAgent(
    name="Title Generator Agent",
    system_message="Your task is to understand the text provided and then generate a 1 line title. Add that to the top of the message and then the rest of the message as is.",
    llm_config = {"config_list" : config_list_gemini},
    human_input_mode = "NEVER",
)

sample_text = """
                Johannes Gutenberg (1398 - 1468) was a German goldsmith and publisher who introduced printing to Europe. His introduction of mechanical movable type printing to Europe started the Printing Revolution and is widely regarded as the most important event of the modern period. It played a key role in the scientific revolution and laid the basis for the modern knowledge-based economy and the spread of learning to the masses.
                Gutenberg many contributions to printing are: the invention of a process for mass-producing movable type, the use of oil-based ink for printing books, adjustable molds, and the use of a wooden printing press. His truly epochal invention was the combination of these elements into a practical system that allowed the mass production of printed books and was economically viable for printers and readers alike.
                In Renaissance Europe, the arrival of mechanical movable type printing introduced the era of mass communication which permanently altered the structure of society. The relatively unrestricted circulation of information—including revolutionary ideas—transcended borders, and captured the masses in the Reformation. The sharp increase in literacy broke the monopoly of the literate elite on education and learning and bolstered the emerging middle class.
                """


article_processor_agent.initiate_chats(
    [
        {
            "recipient" : hashtag_agent,
            "message" : sample_text,
            "max_turns":1,
            "summary_method":"last_msg",
        },
        {
            "recipient" : title_agent,
            "message" : "process the message",
            "max_turns":1,
            "summary_method":"last_msg",
        }
    ]
)
