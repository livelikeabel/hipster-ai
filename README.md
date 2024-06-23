# sophiabel.ai

Welcome to sophiabel.ai project! This project uses `crewAI`, a flexible and powerful AI framework that enables you to create and manage AI agents, tools, and tasks efficiently.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
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

**Create vertual environment**

```bash
python -m venv venv
```

**Activate vertual environment**

```bash
source venv/bin/activate
pip install --upgrade pip
pip install requirements.txt
```

**When you add new packages**

```bash
pip freeze > requirements.txt
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
