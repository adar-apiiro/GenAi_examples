from langchain import PromptTemplate, LLMChain, Anthropic

prompt = PromptTemplate(template=template_no_overlap, input_variables=["topics"])
llm = Anthropic(temperature=1, model="claude-v1.3")
llm_chain = LLMChain(prompt=prompt, llm=llm)
llm_name_chain = LLMChain(prompt=prompt, llm=llm)
