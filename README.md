# 🏋️ Workout Progress Tracker

A lightweight **Python-based Workout Progress Tracker** that allows users to record workout sessions, track exercises and repetitions, and review their workout history directly from the terminal.

This project was developed as a practical application of fundamental Python programming concepts, including functions, loops, conditionals, file handling, data structures, and input validation.

## 📌 Overview

The Workout Progress Tracker provides a simple way to maintain workout records without requiring a database or external application.

Users can:

* Add workout entries
* Record exercises and repetitions
* Store workout information persistently
* View previous workout sessions
* Track workout activity over time

The application is designed to be lightweight, easy to use, and completely terminal-based.

## ✨ Features

* 🏋️ **Add Workout Entries** — Record exercises performed during a workout.
* 📊 **Track Exercise Data** — Store information such as exercises, repetitions, and weights.
* 💾 **Persistent Storage** — Save workout information using local files.
* 📅 **Workout History** — Review previously recorded workouts.
* ✅ **Input Validation** — Handle user input and prevent invalid entries.
* 💻 **Terminal Interface** — Runs directly from the command line with no additional GUI dependencies.
* ⚡ **Lightweight** — Uses Python's built-in functionality without requiring a database.

## 🛠️ Technologies Used

| Technology               | Purpose                                   |
| ------------------------ | ----------------------------------------- |
| **Python**               | Core application development              |
| **Lists & Dictionaries** | Organizing workout data                   |
| **File I/O**             | Reading and writing workout information   |
| **Functions**            | Structuring and reusing application logic |
| **Loops & Conditionals** | Program flow and menu interaction         |
| **Input Validation**     | Handling user input                       |
| **Terminal / CLI**       | User interface                            |

## 🧠 Programming Concepts Demonstrated

This project demonstrates several fundamental programming concepts:

### Functions

The application separates different tasks into functions, making the code easier to understand and maintain.

### Data Structures

Python lists and dictionaries are used to organize and manage workout information.

### File Handling

Workout information is stored locally so that data can persist between program executions.

### Input Validation

User input is validated to reduce errors and ensure the application receives usable information.

### Control Flow

Loops and conditional statements are used to create the interactive terminal menu and control application behavior.

## 📂 Project Structure

```text
Workout-Progress-Tracker/
│
├── cps109_a1.py
├── workouts.txt
├── workouts_summary.txt
├── cps109_a1_output1.png
├── cps109_a1_output2.png
├── cps109_project.pdf
└── README.md
```

### File Descriptions

| File                    | Description                                               |
| ----------------------- | --------------------------------------------------------- |
| `cps109_a1.py`          | Main Python program containing the workout tracking logic |
| `workouts.txt`          | Stores workout information                                |
| `workouts_summary.txt`  | Contains summarized workout information                   |
| `cps109_a1_output1.png` | Example program output                                    |
| `cps109_a1_output2.png` | Additional example output                                 |
| `cps109_project.pdf`    | Project documentation                                     |
| `README.md`             | Project documentation and usage instructions              |

## ⚙️ Getting Started

### Prerequisites

You only need:

* Python 3.x
* A terminal or command-line environment

No external Python packages are required.

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/mpatel1802/Workout-Progress-Tracker.git
```

Navigate into the project directory:

```bash
cd Workout-Progress-Tracker
```

## ▶️ Running the Application

Run the Python program using:

```bash
python cps109_a1.py
```

If your system uses `python3`, run:

```bash
python3 cps109_a1.py
```

## 💡 Example Usage

The application provides a menu-driven terminal interface.

Example workflow:

```text
1. Add Workout
2. View Progress
3. Exit

Enter choice: 1

Enter exercise: Push-ups
Enter reps: 30

Workout saved successfully!
```

Users can then return to the program and review previously recorded workout information.

## 🔄 How It Works

The application follows a simple workflow:

```text
User
  │
  ▼
Main Menu
  │
  ├── Add Workout
  │      │
  │      ▼
  │   Enter Exercise Data
  │      │
  │      ▼
  │   Validate Input
  │      │
  │      ▼
  │   Save Workout
  │
  ├── View Progress
  │      │
  │      ▼
  │   Read Stored Data
  │      │
  │      ▼
  │   Display Workout History
  │
  └─
```
