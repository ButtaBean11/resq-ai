# ResQ-AI — Project Summary

**Challenge:** Civic Chat — Azure AI for community and emergency engagement  
**Event:** Microsoft Innovation Challenge, November 2025

## Problem
Emergency responders often arrive on scene with limited, incomplete, or unclear information.  
This slows down risk assessment, increases danger, and delays rescue operations.

## Solution
ResQ-AI generates a **fast, simple hazard snapshot** from short dispatcher-style text.

**Input Example:**  
“Industrial warehouse fire, heavy smoke showing, 10 workers trapped, 3 near hallway exit”

**Output Example (3–5 bullet summary):**  
- Warehouse fire with heavy smoke  
- Possible chemical/alcohol fuel risk  
- Total 13 occupants involved  
- Structural instability likely  
- High visibility/air quality concern  

## What This Prototype Demonstrates
This lightweight prototype shows:  
- A structured prompt workflow  
- Sample inputs and outputs  
- A tiny Python notebook stub demonstrating how the prompt would be tested  
- Clear documentation for expansion in future versions  

## Why It Matters
ResQ-AI helps build **faster scene awareness** for firefighters, medics, and dispatchers.  
The system supports quicker decision-making and more accurate hazard recognition before arrival.

## Repository Contents
- `prompt.txt` — core Azure prompt  
- `example_input_output.md` — sample inputs & outputs  
- `azure_notebook_stub.py` — simple demo/testing notebook  
- `README.md` — project overview  
