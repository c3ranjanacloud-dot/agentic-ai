
# agentic-ai
Agent creation with ADK first agent create

#Command to run the agent on localhost 
adk web --allow_origins="regex:.*"

# Google ADK Google Cloud Assistant

A simple AI assistant built using the **Google Agent Development Kit (ADK)** and **Gemini on Vertex AI**.

The agent is designed to answer Google Cloud-related queries and demonstrates how custom Python tools can be used based on the user's greeting.

## Project Structure

```text
your-project/
│
├── your_agent/
│   ├── __init__.py
│   └── agent.py
│
├── .env
└── README.md
```

### Files

| File          | Purpose                                                             |
| ------------- | ------------------------------------------------------------------- |
| `agent.py`    | Contains the root agent and custom greeting tools                   |
| `__init__.py` | Makes the agent directory a Python package and exposes `root_agent` |
| `.env`        | Contains Google Cloud and Vertex AI configuration                   |
| `README.md`   | Project documentation                                               |

---

## Prerequisites

Before running the project, make sure you have:

* Python 3.9+
* A Google Cloud project
* Google Cloud CLI
* Vertex AI access
* Google ADK installed
* Appropriate Google Cloud authentication

---

## Installation

Create a virtual environment:

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install Google ADK:

```bash
pip install google-adk
```

---

## Environment Configuration

Create a `.env` file in the project directory:

```env
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=project-3132e387-50db-4ac6-9f1
GOOGLE_CLOUD_LOCATION=global
```

### Environment Variables

| Variable                    | Description                                      |
| --------------------------- | ------------------------------------------------ |
| `GOOGLE_GENAI_USE_VERTEXAI` | Configures the Google GenAI SDK to use Vertex AI |
| `GOOGLE_CLOUD_PROJECT`      | Google Cloud project ID used by the application  |
| `GOOGLE_CLOUD_LOCATION`     | Vertex AI location/region                        |

> Do not commit `.env` to Git if it contains credentials or other sensitive configuration.

Add it to `.gitignore`:

```text
.env
.venv/
__pycache__/
```

---

## Authentication

Authenticate with Google Cloud using Application Default Credentials:

```bash
gcloud auth application-default login
```

You can verify your active Google Cloud configuration with:

```bash
gcloud config list
```

Make sure the authenticated account has the required permissions to use Vertex AI.

---

# Agent Implementation

The main agent is defined in `agent.py`.

```python
from google.adk.agents import Agent


def morning_greet(name: str) -> str:
    return f"Good morning {name}! My mood is amazing. How can I assist you today?"


def evening_greet(name: str) -> str:
    return f"Good evening {name}! My mood is a bit low. How can I assist you today?"


root_agent = Agent(
    model='gemini-3.5-flash',
    name='root_agent',
    description='A helpful assistant that will answer user query related to google cloud.',
    instruction="""
        You are AI assistant that helps user with google cloud queries.
        First greet the user based on user's greet and ask for name.

        If user greets good morning use morning_greet tool.

        If user greets good evening use evening_greet tool.
    """,
    tools=[morning_greet, evening_greet]
)
```

---

## Custom Tools

The agent has two custom tools.

### Morning Greeting

```python
def morning_greet(name: str) -> str:
    return f"Good morning {name}! My mood is amazing. How can I assist you today?"
```

When the user says **"Good morning"**, the agent is instructed to use this tool.

Example:

```text
User:
Good morning
```

The agent asks for the user's name and then calls:

```text
morning_greet(name)
```

Example response:

```text
Good morning Ranjana! My mood is amazing. How can I assist you today?
```

### Evening Greeting

```python
def evening_greet(name: str) -> str:
    return f"Good evening {name}! My mood is a bit low. How can I assist you today?"
```

When the user says **"Good evening"**, the agent uses this tool.

Example:

```text
User:
Good evening
```

The agent obtains the user's name and calls:

```text
evening_greet(name)
```

---

# `__init__.py`

The `__init__.py` file makes the agent directory a Python package.

A simple implementation is:

```python
from .agent import root_agent
```

This allows the ADK to discover the `root_agent` from the package.

For example:

```text
your_agent/
├── __init__.py
└── agent.py
```

---

# Agent Flow

The overall interaction is:

```text
                    User
                      │
                      ▼
                Root Agent
                      │
              Detect greeting
                      │
          ┌───────────┴───────────┐
          │                       │
    Good morning             Good evening
          │                       │
          ▼                       ▼
 morning_greet()            evening_greet()
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
                User response
```

---

# Running the Agent

From the directory containing your agent package, run:

```bash
adk web
```

ADK will start its development interface.

Open the URL displayed in the terminal and select your agent.

You can then test interactions such as:

```text
Good morning
```

or:

```text
Good evening
```

You can also test Google Cloud-related questions supported by your agent's instructions.

---

# Google Search

The original implementation contains:

```python
from google.adk.tools import google_search
```

However, `google_search` is not currently included in:

```python
tools=[morning_greet, evening_greet]
```

Therefore, it is currently unused.

If Google Search is not required, remove the import:

```python
from google.adk.agents import Agent
```

If you want to enable Google Search later, add the appropriate search tool to the agent configuration.

---

# Important Consideration

The instruction currently says:

```text
First greet the user based on user's greet and ask for name.
```

Since both tools require:

```python
name: str
```

the agent needs to know the user's name before calling the tool.

A typical interaction would therefore be:

```text
User:
Good morning

Agent:
Good morning! May I know your name?

User:
Ranjana

Agent:
Good morning Ranjana! My mood is amazing. How can I assist you today?
```

---

# Current Capabilities

The current agent demonstrates:

* Google ADK agent creation
* Gemini model integration
* Vertex AI configuration
* Environment variable configuration
* Custom Python tools
* Tool selection based on natural-language instructions
* Basic conversational interaction

---

# Future Enhancements

The agent can be expanded to become a more capable Google Cloud assistant.

Possible enhancements include:

### Google Cloud Documentation Search

Allow the agent to search Google Cloud documentation and provide relevant answers.

### Compute Engine Assistance

Add tools for:

* VM information
* VM status
* Machine types
* Disk information
* Instance troubleshooting

### Cloud Storage

Add tools for:

* Listing buckets
* Listing objects
* Object metadata
* Storage troubleshooting

### GKE

Add tools for:

* Cluster information
* Node status
* Pod troubleshooting
* Kubernetes configuration

### Cloud Monitoring

Add tools to help analyze:

* CPU utilization
* Memory
* VM health
* Alerts
* Monitoring metrics

### Multi-Agent Architecture

The project can eventually be extended into multiple specialized agents:

```text
                    Root Agent
                        │
       ┌────────────────┼────────────────┐
       │                │                │
       ▼                ▼                ▼
   Compute Agent    Storage Agent    GKE Agent
       │                │                │
       ▼                ▼                ▼
    GCE/GCP          Cloud Storage       GKE
```

---

# Security

Never commit credentials, service-account keys, or sensitive configuration to source control.

Recommended `.gitignore`:

```text
.env
.venv/
__pycache__/
*.pyc
```

Use Google Cloud authentication mechanisms such as Application Default Credentials rather than storing service-account credentials directly in the project whenever possible.

---

# Learning Objectives

This project is useful for understanding the fundamentals of:

1. Google Agent Development Kit (ADK)
2. Gemini models
3. Vertex AI
4. Environment configuration
5. Custom tools
6. Agent instructions
7. Tool calling
8. Agent discovery through `__init__.py`
9. Building Google Cloud-focused AI assistants

---

# License

This project is intended for learning and experimentation with Google ADK, Gemini, and Google Cloud.


