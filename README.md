# 👨🏻‍💻 Code Quality Checker with Radon and Xenon

This repository uses Radon and Xenon to analyze code complexity and maintainability. These tools help ensure your code is readable, maintainable, and within specified complexity limits.

## ✅ Features

- Radon for cyclomatic complexity (CC) and maintainability index (MI).
- Xenon for enforcing complexity thresholds.
- Runs checks both locally and in CI/CD pipelines with GitHub Actions.

## 📝 Concepts

### Radon

- **Cyclomatic Complexity (CC)**: Measures how complex a function is by counting the number of decisions or branches (e.g., if, for, while). Lower complexity means simpler, easier-to-read code. Grades range from A (simplest) to F (most complex).

Example:

- A function with few if statements is simple (Grade A or B).
- A function with many conditions is complex (Grade C or worse).

- **Maintainability Index (MI)**: Tells you how easy the code is to maintain. Higher numbers mean more maintainable code. Radon uses the length of your code, the number of comments, and its complexity to calculate this score.

### Xenon

- Xenon builds on Radon by enforcing complexity rules. You set a maximum allowable complexity (like Grade B), and Xenon checks whether your code stays within that limit.

#### 💥 Complexity Grades

- A: Very simple.
- B: Slightly complex.
- C: Acceptable for complicated logic.
- D & F: Too complex, harder to maintain.

By using Xenon, you prevent overly complex code from being added to your project.

## Setup Instructions

1. 👨🏻‍💻 Running Locally

    Requirements:
    - Python 3.9 or higher
    - pip

    Install Dependencies:
    ``sh
    pip install radon xenon
    ``

    - Cyclomatic Complexity (CC) Check:

    ``sh
        radon cc ./ -s
    ``

    - Maintainability Index (MI) Check:

    ``sh
        radon mi ./
    ``  

    - Xenon Complexity Enforcement:

    ``sh
        xenon --max-absolute B ./
    ``

2. 📦 Using Docker

    Requirements:
    - Docker Desktop

    ``sh
    docker build -t code-quality-checker .
    docker run -t code-quality-checker
    ``

3. 🔂 GitHub Actions Integration

    Requirements:
    - Github repo

    This repository includes a GitHub Actions workflow that automatically checks the code quality when a pull request is opened or updated on the main branch.

    GitHub Actions Workflow ``.github/workflows/code-quality.yml``

    How it works:
    - Trigger: This workflow runs on any pull request targeting the main branch.
    - Python Setup: Python 3.9 is installed and used in the workflow.
    - Code Quality Check: The following checks are run:
        - Radon CC analysis.
        - Radon MI analysis.
        - Xenon complexity enforcement (max absolute complexity level B).

    Once the checks are completed, you'll see the results directly in the GitHub pull request under the "Checks" tab.

4. 🔨 Customizing Xenon Complexity

    You can modify the complexity threshold for Xenon by changing the ``--max-absolute`` flag in your GitHub Actions workflow or when running it locally.

    Available grades are A, B, C, D, and F, with A being the least complex and F being the most complex.

5. You can also enable the VSCode extension called ``python-radon`` or ``vscode-radon-linter``

### 😎 [Follow me on Linkedin](https://www.linkedin.com/in/alejandro-aboy/)
- Get tips, learnings and tricks for your Data career!

### 📩 [Subscribe to The Pipe & The Line](https://thepipeandtheline.substack.com/?utm_source=github&utm_medium=referral)
- Join the Substack newsletter to get similar content to this one and more to improve your Data career!
