# Autonomous Agent System

A **framework-free** autonomous agent that demonstrates planning, tool execution, memory, and self-evaluation—built from first principles without LangChain or similar abstractions.

## Overview

This system implements the canonical agent loop: decompose → execute → evaluate → persist. It handles multi-step tasks by breaking goals into sub-tasks, selecting and running appropriate tools, evaluating outputs, and maintaining context across turns.

```
User Input
     │
     ▼
┌─────────┐     ┌──────────┐     ┌────────┐     ┌────────┐
│ PLANNER │────▶│ EXECUTOR │────▶│ CRITIC │────▶│ MEMORY │
└────┬────┘     └──────────┘     └────────┘     └───┬────┘
     │                │                │             │
     └────────────────┴────────────────┴─────────────┘
                      (context feedback)
```

## Features

| Component | Description |
|-----------|-------------|
| **Planner** | Decomposes user goals into ordered sub-tasks using LLM |
| **Executor** | Dynamically selects tools (calculator, search) via LLM and runs them |
| **Critic** | Evaluates output quality against the original task |
| **Memory** | Short-term (session) + long-term (JSON persistence) for context-aware planning |

## Project Structure

```
agent_system/
├── main.py           # Entry point, orchestrates the agent loop
├── planner.py       # Task decomposition with optional memory context
├── executer.py      # Tool selection and execution
├── critic.py        # Output evaluation
├── memory.py        # Short-term + long-term storage
├── tools/
│   ├── base_tool.py # Tool interface
│   ├── calculator.py
│   └── search.py
├── utils/
│   └── llm.py       # OpenAI client wrapper
└── data/            # Persistent memory store (created at runtime)
```

## Requirements

- Python 3.10+
- OpenAI API key

## Quick Start

```bash
# Clone and setup
git clone https://github.com/Syedafzal059/autonomous-agent-system.git
cd autonomous-agent-system

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Configure (copy .env.example and add your key)
cp .env.example .env
# Set OPENAI_API_KEY in .env

# Run
python -m agent_system.main
```

## Usage

Interactive mode prompts for a task, then runs the full pipeline:

```
Enter your task:  Search for best laptops under 1 lakh and compare top 3

[PLANNER]
1. Search for laptops under 1 lakh
2. Compare top 3 results
...

[EXECUTOR]
1. Search for laptops under 1 lakh -> Search result for: ...
...

[CRITIC]
Evaluation: ...
```

## Tech Stack

- **LLM**: OpenAI GPT-4o-mini (configurable)
- **Storage**: JSON file for long-term memory
- **Tools**: Extensible registry; currently Calculator and Search

## Design Decisions

- **No LangChain**: Full control over each component; easier to debug and extend
- **Explicit components**: Planner, Executor, Critic, Memory are isolated and testable
- **Env-based config**: API keys and sensitive data via environment variables

## License

MIT
