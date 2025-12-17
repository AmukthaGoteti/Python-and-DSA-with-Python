# 🎮 Tic-Tac-Toe (Python GUI)

A simple **Tic-Tac-Toe game built using Python and Tkinter**, designed to demonstrate GUI development, event-driven programming, and basic game logic in Python.

This project is ideal for beginners learning Python GUIs and for showcasing a **clean, functional mini-project** in portfolios or interviews.

---

## 📌 Features

* Two-player gameplay (**X vs O**)
* Interactive **graphical user interface (GUI)**
* Automatic **win detection**
* **Draw detection**
* One-click **game reset**
* Simple, readable, and modular code structure

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** (Python’s standard GUI library)

---

## 📂 Project Structure

```bash
├── Tic_Tac_Toe.py
└── README.md
```

---

## ▶️ How to Run

### Prerequisites

* Python **3.9 or higher**
* Tkinter (comes pre-installed with Python)

### Run the Game

```bash
python Tic_Tac_Toe.py
```

A window will open with a 3×3 Tic-Tac-Toe board.

---

## 🎯 How the Game Works

* The game starts with **Player X**
* Players take turns clicking on empty cells
* The game checks for:

  * Horizontal wins
  * Vertical wins
  * Diagonal wins
* A popup message appears when:

  * A player wins
  * The game ends in a draw
* The board resets automatically after game completion
* You can also reset the game manually using the **Reset Game** button

---

## 🧠 Core Logic Overview

### Board Representation

* The board is stored as a **1D list of 9 elements**
* Each index corresponds to a cell in the 3×3 grid

### Win Detection

* Predefined winning index combinations are checked after every move

### Event Handling

* Each button click updates:

  * The board state
  * The UI text
  * The current player

---

## 🚀 Learning Outcomes

By building this project, you will learn:

* Creating GUIs using **Tkinter**
* Handling **button events**
* Managing game state
* Implementing conditional logic
* Writing clean, modular Python functions

---

## 🔧 Possible Enhancements

* Single-player mode (Player vs Computer)
* Score tracking
* Highlight winning combinations
* Improved UI styling
* Sound effects

---

**Happy coding and game building! 🎉**