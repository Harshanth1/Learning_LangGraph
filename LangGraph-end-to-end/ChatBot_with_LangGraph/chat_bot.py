# from langgraph.graph import StateGraph, MessagesState, START, END
# from langgraph.graph import add_messages
# from typing import Annotated, Any, Literal, TypedDict

# from langchain.tools import tool
# from langchain_core.messages import HumanMessage

# from langgraph.checkpoint.memory import MemorySaver
# from langgraph.prebuilt import ToolNode

# from langchain_groq import ChatGroq
# from langchain_community.tools.tavily_search import TavilySearchResults

# from langgraph.checkpoint.memory import MemorySaver

# class ChatBot:
    
#     def __init__(self):
#         self.llm=ChatGroq(model="qwen/qwen3-32b")
        
#     def call_tool(self):
#         tool=TavilySearchResults(max_results=2)
#         tools=[tool]
#         self.tool_node=ToolNode(tools=tools)
#         self.llm_with_tool=self.llm.bind_tools(tools)
        
#     def call_model(self, state: MessagesState):
#         messages=state['messages']
#         response=self.llm_with_tool.invoke(messages)
#         return {"messages": [response]}
    
#     def router_function(self, state: MessagesState) -> Literal['tools',END]:
#         messages=state['messages']
#         last_message=messages[-1]
#         if last_message.tool_calls:
#             return 'tools'
#         return END
    
#     def __call__(self) -> Any:
        
#         self.call_tool()
#         workflow=StateGraph(MessagesState)
#         workflow.add_node("agent", self.call_model)
#         workflow.add_node("tools", self.tool_node)
#         workflow.add_edge(START, "agent")
#         workflow.add_conditional_edges('agent', self.router_function, {'tools':"tools", END:END})
#         workflow.add_edge("tools", 'agent')
        
#         memory=MemorySaver()
        
#         self.app=workflow.compile(checkpointer=memory)
        
#         config={'configurable':{'thread_id': '1'}}
#         events=self.app.stream(
#             {'messages':}
#             config=config,
#             stream_mode="values"
#         )
#         return self.app

# if __name__=="__main__":
#     mybot=ChatBot()
#     workflow=mybot()
#     # response=workflow.invoke({"messages":['Who is a current primte minister of India?']})
#     # print(response['messages'][-1].content)

from langgraph.graph import StateGraph, MessagesState, START, END
from typing import Any, Literal
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import ToolNode

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults


class ChatBot:

    def __init__(self):
        self.llm = ChatGroq(model="qwen/qwen3-32b")
        self.memory = MemorySaver()
        self._build_graph()

    def _build_graph(self):
        tool = TavilySearchResults(max_results=2)
        tools = [tool]

        self.tool_node = ToolNode(tools=tools)
        self.llm_with_tool = self.llm.bind_tools(tools)

        workflow = StateGraph(MessagesState)

        workflow.add_node("agent", self.call_model)
        workflow.add_node("tools", self.tool_node)

        workflow.add_edge(START, "agent")

        workflow.add_conditional_edges(
            "agent",
            self.router_function,
            {"tools": "tools", END: END},
        )

        workflow.add_edge("tools", "agent")

        self.app = workflow.compile(checkpointer=self.memory)

    def call_model(self, state: MessagesState):
        response = self.llm_with_tool.invoke(state["messages"])
        return {"messages": [response]}

    def router_function(self, state: MessagesState) -> Literal["tools", END]:
        last_message = state["messages"][-1]

        if getattr(last_message, "tool_calls", None):
            return "tools"

        return END

    def stream(self, messages, thread_id):
        config = {"configurable": {"thread_id": thread_id}}

        return self.app.stream(
            {"messages": messages},
            config=config,
            stream_mode="values"
        )