from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI


def get_basic_conversation_chain(model_name='gpt-3.5-turbo'):

    llm = ChatOpenAI(
        model_name=model_name,
        temperature=0,
    )

    return ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory()
    )
