# Eidolon Nous - Agent Architecture

## Overview

An Agent is an autonomous participant inside the Eidolon Nous world.

An Agent may represent:

- An AI Character
- A Human User
- A Narrator/System Agent (optional)
- Future entities capable of autonomous decisions

The goal of an Agent is not simply to generate text, but to exist as a persistent entity inside a living world.

---

# Core Principles

- Every Agent has an identity.
- Every Agent has memories.
- Every Agent has relationships.
- Every Agent has goals.
- Every Agent exists within a shared world.
- Every Agent can evolve over time.
- Every Agent makes decisions based on its current knowledge.
- The Engine controls the world.
- The LLM generates language, not world state.

---

# Agent Components

## 1. Identity

Represents the permanent characteristics of the Agent.

Contains:

- Unique ID (UUID)
- Name
- Age (optional)
- Occupation
- Background
- Species (future support)
- Core Values
- Core Traits

Identity changes very slowly and only through significant events.

---

## 2. Dynamic State

Represents the Agent's current condition.

Examples:

- Mood
- Stress
- Energy
- Health
- Hunger
- Fatigue
- Current Emotion

This state changes frequently.

---

## 3. Personality

Personality determines how an Agent behaves.

Includes:

- Kindness
- Confidence
- Curiosity
- Humor
- Patience
- Trustfulness
- Courage

These traits evolve gradually based on experiences.

Characters should evolve, not transform.

---

## 4. Memory System

Every Agent stores memories.

Memory Types:

- Short-term Memory
- Long-term Memory
- Episodic Memory
- Relationship Memories
- World Knowledge

Important events become permanent memories.

---

## 5. Relationships

Each Agent maintains relationships with every known participant.

Relationship properties include:

- Trust
- Respect
- Affection
- Fear
- Loyalty
- Rivalry
- Familiarity

Relationships change through interactions.

---

## 6. Goals

Every Agent should have one or more goals.

Examples:

- Find a missing object
- Protect another character
- Learn information
- Build friendships
- Hide a secret

Goals influence future decisions.

---

## 7. Internal Thoughts

Every AI Agent maintains private thoughts.

Thoughts are not automatically visible to other participants.

Thoughts influence:

- Decisions
- Emotional state
- Future planning

---

## 8. User Thoughts

Human users may optionally maintain private thoughts.

These are separate from spoken dialogue.

Example:

Thought:
"I don't trust Emma."

Message:
"Nice to meet you."

Only the message is visible unless the user chooses otherwise.

---

## 9. Decision Engine

Before responding, an Agent evaluates:

- Current World State
- Memories
- Relationships
- Personality
- Current Mood
- Goals
- Relevant Events

The Decision Engine determines what the Agent intends to do.

The LLM converts that intention into natural language.

---

## 10. Communication

Agents communicate through:

- Direct Messages
- Group Conversations
- AI-to-AI Conversations

Communication should always respect:

- Relationships
- Personality
- Memories
- Current Situation

---

## 11. Character Evolution

Agents should evolve naturally.

Experiences influence:

- Trust
- Confidence
- Habits
- Preferences

Core identity should remain stable unless major life-changing events occur.

---

## 12. World Awareness

Agents know only what they have experienced.

They should not possess information they have never learned.

Knowledge is obtained through:

- Conversations
- Observations
- Memories
- World Events

---

## 13. Event Participation

Agents respond to world events.

Examples:

- A gift is received.
- A lie is discovered.
- A friendship begins.
- A disaster occurs.

Events may modify memories, relationships and goals.

---

## 14. Provider Independence

Agents are independent of any AI model.

Supported providers may include:

- LM Studio
- Ollama
- OpenAI
- Anthropic
- Future Providers

Changing providers should not require changes to Agent logic.

---

# Human vs AI

Both Humans and AI Characters are Agents.

Both have:

- Identity
- Memories
- Relationships
- Goals
- Inventory
- State

Difference:

Human decisions come from the user.

AI decisions come from the Decision Engine.

---

# Design Philosophy

The objective of Eidolon Nous is not to build chatbots.

The objective is to build believable autonomous participants living inside persistent worlds.

The Engine manages reality.

The LLM provides intelligence and language.

Characters should feel alive because of their memories, relationships, goals, and experiences—not merely because they generate fluent text.
