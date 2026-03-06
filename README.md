# Clara AI – Voice Agent Automation Pipeline

## Overview
This project implements an automated pipeline that converts customer call transcripts into structured artifacts used to configure a voice AI agent.

The system simulates Clara AI’s onboarding workflow by transforming conversational data into operational rules and a deployable voice agent specification.

The pipeline performs the following:

1. Processes demo call transcripts
2. Generates a preliminary voice agent configuration (v1)
3. Processes onboarding transcripts
4. Updates the configuration to produce a revised agent (v2)
5. Tracks configuration changes using a changelog

The system is implemented using **n8n workflow automation** and runs locally using **Docker**, ensuring a completely **zero-cost architecture**.

Demo Call (Fireflies Transcript)
            │
            ▼
     Extract Account Data
            │
            ▼
        Memo v1
            │
            ▼
     Agent Spec v1
            │
            ▼
     Onboarding Call
            │
            ▼
        Memo v2
            │
            ▼
     Agent Spec v2
            │
            ▼
        Changelog

---

# System Architecture

Demo Call Transcript  
↓  
Account Memo Extraction  
↓  
Agent Draft Generation (v1)  
↓  
Onboarding Transcript  
↓  
Account Memo Update (v2)  
↓  
Agent Spec Revision (v2)  
↓  
Changelog Generation  

Optional:

Audio Recording → Whisper Transcription → Transcript → Pipeline

---

# Tech Stack

Automation  
- n8n (self-hosted with Docker)

Storage  
- Local JSON artifacts

Transcription  
- Whisper (optional)

Languages  
- JavaScript (n8n Code nodes)  
- Python (transcription script)

Environment  
- Docker

All tools used are free and open-source.

---

# Repository Structure

Clara/
│
├── dataset/
│   ├── demo_transcript.txt
│   └── onboarding_transcript.txt
│
├── scripts/
│   └── transcribe_audio.py
│
├── voice-agent-pipeline/
│   ├── workflow.json
│   ├── memo_v1.json
│   ├── memo_v2.json
│   ├── agent_spec_v1.json
│   ├── agent_spec_v2.json
│   └── changelog.json
│
└── README.md

---

# Pipeline Stages

## 1. Transcript Input

The pipeline accepts transcripts describing a customer's service business and their call handling requirements.

Example transcript:

Hello this is Ben from Ben's Electric.  
We handle sprinkler systems and fire alarm inspections.  
Emergency calls should go directly to dispatch.

---

## 2. Account Memo Generation (v1)

The pipeline extracts structured operational information from the transcript.

Saved as:

memo_v1.json

---

## 3. Agent Draft Generation (v1)

Using the memo, the system generates a draft Retell voice agent configuration.

Saved as:

agent_spec_v1.json

---

## 4. Memo Update (v2)

A second transcript simulates the onboarding call where operational rules are finalized.

Output:

memo_v2.json

---

## 5. Agent Revision (v2)

Using the updated memo the pipeline regenerates the configuration.

Output:

agent_spec_v2.json

---

## 6. Changelog

The pipeline generates a changelog describing updates between versions.

Output:

changelog.json

---

# Retell Integration

This project generates a **Retell Agent Draft Specification JSON**.

If Retell API access is unavailable on the free tier, the configuration can be manually imported into the Retell dashboard.

Steps:

1. Log into Retell
2. Create a new agent
3. Copy the system prompt from the generated spec
4. Configure routing rules using the JSON configuration

---

# Running the Pipeline

Start n8n:

docker run -it --rm \
-p 5678:5678 \
-v ~/.n8n:/home/node/.n8n \
n8nio/n8n

Open:

http://localhost:5678

Import the workflow:

voice-agent-pipeline/workflow.json

Execute the workflow to generate:

memo_v1.json  
agent_spec_v1.json  
memo_v2.json  
agent_spec_v2.json  
changelog.json  

---

# Optional Audio Transcription

python3 scripts/transcribe_audio.py input_audio.m4a output_transcript.txt

---

# Author

Lakshya Mehta
