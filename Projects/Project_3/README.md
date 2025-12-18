# Hazard Detector and Simulator in Python

## Overview

This project focuses on the **analysis, detection, and correction of hazards in combinational logic circuits** using a Python-based simulation framework. It evaluates Boolean functions, simulates input transitions with unequal propagation  elays, and identifies potential glitches that can lead to unreliable circuit behavior.

The system is designed to bridge **digital logic theory** and **practical simulation**, providing a clear, structured approach to understanding static and dynamic hazards.

---

## Project Description

The **Hazard Detector and Simulator** accepts a Boolean function (expression or minterms), generates its truth table,simulates adjacent input transitions, and detects hazards caused by unequal propagation delays.

The system identifies:
- **Static-1 hazards**
- **Static-0 hazards**
- **Dynamic hazards**

It also suggests corrective measures, such as **adding consensus terms**, to achieve hazard-free logic.

---

## Functional Requirements

- Accept Boolean expressions or minterm lists as input  
- Generate a complete truth table for the given logic function  
- Simulate adjacent input transitions to detect output glitches  
- Identify static-1, static-0, and dynamic hazards  
- Recommend logic corrections (e.g., consensus terms)  
- Optionally visualize hazard waveforms using Python plotting libraries  

---

## Deliverables

### 1. System Block Diagram

A high-level diagram illustrating the system architecture, including:

- Expression Parser  
- Truth Table Generator  
- Transition Simulator  
- Hazard Detection Engine  
- Correction Suggestion Module  
- Optional Waveform Visualization Module  

---

### 2. Detailed Design

The design documentation covers:

- Boolean expression parsing strategy  
- Truth table generation algorithm  
- Identification of adjacent input transitions  
- Output simulation under assumed propagation delays  
- Hazard detection and classification logic  
- Computation of consensus terms for hazard elimination  
- Python code structure with flowcharts or pseudocode  
- Example cases demonstrating hazard detection and correction  

---

### 3. Timing Analysis

- Waveform-style plots showing output behavior during transitions  
- Clear indication of glitches and their durations  
- Before-and-after comparison demonstrating hazard removal  

---

### 4. Design Documentation

Includes:

- Justification for using Python as the simulation platform  
- Explanation of key design choices (parsing, detection, visualization)  
- Assumptions regarding gate delays and input transitions  
- Limitations and future enhancements, such as:
  - Real-time GUI support  
  - Integration with professional logic simulators  
  - Extension to multilevel combinational circuits  

---

## Tools & Technologies

- **Python 3**
- Boolean logic handling libraries (optional)
- `matplotlib` for waveform visualization (optional)

---

## Conclusion

This project provides a structured and practical approach to understanding **hazards in digital logic circuits**. By combining theoretical concepts with Python-based simulation, it enables precise detection, visualization, and correction of logic hazards—an essential skill in reliable digital system design.