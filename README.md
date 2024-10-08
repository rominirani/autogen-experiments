Experiments demonstrating Autogen framework. 

1. [`app1`](app1) : Multi-turn conversation between 2 agents, CFP Writer and CFP Reviewer that converse with each other to improve a CFP. Their conversation lasts the number of `max_turns` mentioned while setting up i.e. initiating the chat. 
2. [`app2`](app2) : Multi-turn conversation between 2 agents with an explicit termination done by the framework if the CFP Reviewer mentions "looks good". It does not depend on the `max_turns` parameter while initiating the chat. 
