
Sources : 

- [ ] https://huggingface.co/learn/agents-course
- [ ] [(April 2025) Which Multi‑Agent Framework Should Run Your Enterprise AI?](https://medium.com/@mpuig/which-multi-agent-framework-should-run-your-enterprise-ai-abdc8e09ad89)
- [ ] https://www.learn-agents.diy/basics/prompt-eng



> [!IMPORTANT]
An agentic framework is **not always needed when building an application around LLMs**. They provide flexibility in the workflow to efficiently solve a specific task, but they’re not always necessary.


### LLM vs tool augmented LLM vs agent   

[Tool calling](https://python.langchain.com/docs/concepts/tool_calling/) allows a chat model to respond to a given prompt by "calling a tool".
Remember, while the name "tool calling" implies that the model is directly performing some action, this is actually not the case! The model only generates the arguments to a tool, and actually running the tool (or not) is up to the user.

In summary, an LLM-based agent is an autonomous entity that leverages an LLM’s reasoning _and_ its own tooling loop to achieve goals.  It has **high autonomy** (little or no user intervention during execution), uses tools proactively, and often employs explicit planning and state tracking.  These agents are suited for complex multi-step tasks (e.g. automated research, coding projects, itinerary planning) where simple one-shot LLM calls would fail.

| **Dimension**    | **Foundational LLMs**                                                               | **Tool-Augmented LLMs**                                                                       | **LLM-Based Agents**                                                                                        |
| ---------------- | ----------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Autonomy**     | Low – single-turn or chat-driven; no self-initiated actions.                        | Limited – follows user or prompt guidance; may call tools if prompted.                        | High – operates in a loop toward a goal; can decide next actions without user each step.                    |
| **Tool Use**     | None. Pure text generation.                                                         | Yes – integrated API calls/plugins (e.g. search, calculators, databases) .                    | Yes – actively uses tools via actions (search, code, UI automation) as part of planning .                   |
| **Memory**       | Context-only (token window + fixed parameters). No long-term memory.                | Context + ephemeral memory. Can retrieve docs or use RAG but usually no persistent memory.    | Context + explicit memory (chat history, vector DB, scratchpad). Remembers earlier steps and facts.         |
| **Architecture** | Single transformer (auto-regressive).                                               | Transformer + tool interface. LLM connected to external functions (via plugin/API) .          | Multi-component. LLM plus planner/controller module, memory store, tool executor, possibly multiple agents. |
| **Control Flow** | Straightforward prompt→response (or simple chat).                                   | Mostly linear: prompt (with possible function call)→tool run→response.                        | Iterative loop: sense (input/observation) → think (LLM reasoning) → act (tool call or environment action) . |
| **Planning**     | Implicit or none. Any planning is inside one prompt’s reasoning (chain-of-thought). | Reactive: might choose a tool call based on prompt, but no explicit multi-step planning.      | Explicit: breaks task into subgoals, may use tree-of-thought or planner modules. Recursively refines plan.  |
| **Examples**     | GPT-4 (no plugins), Claude, LLaMA, GPT-3 (text only).                               | ChatGPT/GPT-4 with plugins (browser, code), OpenAI Function Calling, RAG systems.             | LangGraph.                                                                                                  |
| **Use Cases**    | General text, Q&A on known data, drafting, summarization, chatbots.                 | Queries needing up-to-date data or compute (e.g. weather lookup, calculation, data analysis). | Complex workflows (booking, research, coding), autonomous agents for tasks, multi-step decision-making.     |


![[Pasted image 20250504000023.png]]


Libraries : 

- Google ADK (my choice)
- CrewAI
- LangGraph
- atomic-agents
- PydanticAI
- 