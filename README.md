# sophiabel.ai

Welcome to sophiabel.ai project! This project uses `crewAI`, a flexible and powerful AI framework that enables you to create and manage AI agents, tools, and tasks efficiently.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Usage](#usage)
- [Updating Dependencies](#updating-dependencies)

## Introduction

This project is designed to help english teacher. Follow the steps below to set up and run the project on your local machine.

## Installation

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.10.12
- `git` installed on your machine

### Setup

1. **Install pyenv**

   ```bash
   curl https://pyenv.run | bash
   ```

2. **Configure pyenv**
   Add the following lines to your `~/.bashrc` or `~/.zshrc` file:

   ```bash
   export PYENV_ROOT="$HOME/.pyenv"
   command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"
   eval "$(pyenv init --path)"
   eval "$(pyenv init -)"
   eval "$(pyenv virtualenv-init -)"
   ```

   Reload your shell configuration:

   ```bash
   exec "$SHELL"
   ```

3. **Install Python Version**

   ```bash
   pyenv install 3.10.12
   pyenv global 3.10.12
   ```

4. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

5. **Activate the Virtual Environment**

   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

6. **Upgrade pip**

   ```bash
   pip install --upgrade pip
   ```

7. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the project, follow these steps:

1. **Activate the virtual environment** (if not already activated):

   ```bash
   source venv/bin/activate  # macOS/Linux
   .\venv\Scripts\activate  # Windows
   ```

2. **Run your script or application**
   ```bash
   python main.py
   ```

## Updating Dependencies

If you install new packages, remember to update the `requirements.txt` file to include the new dependencies. This ensures that others can install the same packages and run the project without issues.

### To install a new package and update `requirements.txt`:

1. **Install the new package**:

   ```bash
   pip install new_package
   ```

2. **Update `requirements.txt`**:
   ```bash
   pip freeze > requirements.txt
   ```

By following these steps, you can keep the `requirements.txt` file up-to-date and ensure that all dependencies are properly managed.

Thank you for using sophiabel.ai project!
