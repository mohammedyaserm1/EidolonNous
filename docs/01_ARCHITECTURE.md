# Eidolon Nous Architecture

Version: 0.1

This document describes the high-level architecture of Eidolon Nous.

## Philosophy

Eidolon Nous is not a chatbot.

It is an AI simulation engine.

The frontend is only one interface.

The backend is only one transport layer.

The Engine contains all simulation logic.


             User
               │
               ▼
         React Frontend
               │
               ▼
        REST / WebSocket
               │
               ▼
        FastAPI Backend
               │
               ▼
        Eidolon Engine
     ┌─────────┼──────────┐
     │         │          │
 Agent      Memory     World
 Manager     Engine     Engine
     │         │          │
     └─────────┼──────────┘
               │
        Relationship Engine
               │
        Decision Engine
               │
        Prompt Builder
               │
        Model Provider
               │
          LM Studio



## Core Modules

- Agent Manager
- Conversation Manager
- Memory Engine
- World Engine
- Relationship Engine
- Decision Engine
- Prompt Builder
- Model Provider
