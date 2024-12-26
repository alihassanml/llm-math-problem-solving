import streamlit as st
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.agents import Tool,initialize_agent
from langchain.chains import LLMMathChain
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.agents.agent_types import AgentType
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler

st.set_page_config(page_title='Text to Math problem solving using Gemma 2',page_icon="📈")
st.title('Text to Math problem solving')
groq_api_key = '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'

llm = ChatGroq(model='Gemma2-9b-It',groq_api_key=groq_api_key)

wikpedia = WikipediaAPIWrapper()
wikipedia_tool = Tool(
    name='wikipedia',
    func=wikpedia.run,
    description="A tool for searching the internet to find the various information on the topics mentioned"
)

math_chian = LLMMathChain.from_llm(llm=llm)
calculator = Tool(
    name='calculator',
    func=math_chian.run,
    description = 'A tool for providing answering math related question.Only input math related expression need to bed provided'
)

prompt="""
Your a agent tasked for solving users mathemtical question. Logically arrive at the solution and provide a detailed explanation
and display it point wise for the question below
Question:{question}
Answer:
"""

prompt_template=PromptTemplate(
    input_variables=["question"],
    template=prompt
)

chain = LLMMathChain(llm=llm,prompt=prompt_template)

reasoning_tool = Tool(
    name="Reasoning Tool",
    func=chain.run,
    description="A tool for providing answering logic-base and reasoning base in detail"
)


assistant = initialize_agent(
    tools=[wikipedia_tool,calculator,reasoning_tool],
    llm =llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = False,
    handle_parsing_error = True
)

if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"Hi, I'm a Math chatbot who can answer all your maths questions"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])


input = st.text_area(label="Enter your question")
if st.button('Find answer'):
    st.session_state.messages.append({"role":"user","content":input})
    st.chat_message("user").write(input)

    st_cb=StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
    response=assistant.run(st.session_state.messages,callbacks=[st_cb]
                                    )
    st.session_state.messages.append({'role':'assistant',"content":response})
    st.write('### Response:')
    st.success(response)