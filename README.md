# Autonomous Agent System

A **framework-free** autonomous agent that demonstrates planning, tool execution, memory, and self-evaluation—built from first principles without LangChain or similar abstractions.

## Overview

This system implements the canonical agent loop: decompose → execute → evaluate → persist. It handles multi-step tasks by breaking goals into sub-tasks, selecting and running appropriate tools, evaluating outputs, and maintaining context across turns. A **retry loop** re-plans when the critic score is below threshold, feeding feedback into the planner for iterative improvement.

```
User Input
     │
     ▼
┌──────────────────────────────────────────────────────────────┐
│  RETRY LOOP (max attempts, score threshold, best-result)     │
│                                                               │
│  ┌─────────┐     ┌──────────┐     ┌────────┐     ┌────────┐  │
│  │ PLANNER │────▶│ EXECUTOR │────▶│ CRITIC │────▶│ MEMORY │  │
│  └────┬────┘     └──────────┘     └────┬────┘     └───┬────┘  │
│       │                │               │              │      │
│       │                │         [score ≥ threshold?]   │      │
│       │  feedback ◀────┴───────────────┤               │      │
│       └────────────────────────────────┴───────────────┘      │
└──────────────────────────────────────────────────────────────┘
```

## Features

| Component | Description |
|-----------|-------------|
| **Planner** | Decomposes user goals into ordered sub-tasks; uses critic feedback to improve on retry |
| **Executor** | Dynamically selects tools (calculator, search) via LLM and runs them |
| **Critic** | Evaluates output (score 0–10, feedback); drives retry and stopping decisions |
| **Memory** | Short-term (session) + long-term (JSON persistence) for context-aware planning |
| **Retry Loop** | Re-runs planner→executor→critic until score ≥ threshold or max attempts; tracks best result |

## Project Structure

```
agent_system/
├── main.py           # Entry point, orchestrates retry loop + agent pipeline
├── planner.py       # Task decomposition; accepts memory context and critic feedback
├── executer.py      # Tool selection and execution
├── critic.py        # Output evaluation (score + feedback)
├── memory.py        # Short-term + long-term storage
├── tools/
│   ├── base_tool.py # Tool interface
│   ├── calculator.py
│   └── search.py
├── utils/
│   └── llm.py       # OpenAI client wrapper
└── data/            # Persistent memory store (created at runtime)

config.py            # MAX_RETRIES, SCORE_THRESHOLD (project root)
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

# Run (from project root so config is found)
python -m agent_system.main
```

## Configuration

Edit `config.py` to tune retry behavior:

| Setting | Default | Description |
|---------|---------|-------------|
| `MAX_RETRIES` | 3 | Maximum planner→executor→critic cycles per task |
| `SCORE_THRESHOLD` | 7 | Stop early when critic score ≥ this (0–10 scale) |

## Usage

Interactive mode prompts for a task, then runs the retry loop:

```
Enter your task:  Search for best laptops under 1 lakh and compare top 3

 Attempt 1
[PLANNER]
1. Search for laptops under 1 lakh
2. Compare top 3 results
...
[EXECUTOR]
...
[CRITIC]
{"score": 5, "feedback": "Missing comparison criteria"}

 Attempt 2
[PLANNER]
(Improved plan using feedback)
...
[CRITIC]
{"score": 8, "feedback": "..."}
 GOOD ENOUGH!, stopping retries

 FINAL OUTPUT
(best result across attempts)
```

## Tech Stack

- **LLM**: OpenAI GPT-4o-mini (configurable)
- **Storage**: JSON file for long-term memory
- **Tools**: Extensible registry; currently Calculator and Search

## Design Decisions

- **No LangChain**: Full control over each component; easier to debug and extend
- **Explicit components**: Planner, Executor, Critic, Memory are isolated and testable
- **Retry with score threshold**: Iterative improvement; stops when quality is good enough
- **Env-based config**: API keys and sensitive data via environment variables

## License

MIT
