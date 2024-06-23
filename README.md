# sophiabel.ai

## Table of Contents

- [Updating Dependencies](#updating-dependencies)

## Introduction

## Installation

**python version: 3.10.12**

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
