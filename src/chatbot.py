import dotenv
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

dotenv.load_dotenv()
from langchain_openai import ChatOpenAI



chat = ChatOpenAI(model="gpt-3.5-turbo-1106", temperature=0.2)

from langchain_core.messages import HumanMessage
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant. Answer all questions to the best of your ability.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | chat



def firstaidschatbot(q):

    res=chain.invoke(
    {
        "messages": [
            HumanMessage(
                content=f"{q}"
            ),
            #AIMessage(content="J'adore la programmation."),
            #HumanMessage(content="What did you just say?"),
        ],
    }
    
)
    return res








