# Contributing

Contributions to `bvbrc` are welcome and appreciated! There are a handful of
different ways to contribute to the project.

## Types of Contributions

### Report Bugs

Bugs can be reported by
[filing an issue on GitHub](https://github.com/abates20/bvbrc/issues). If you
are reporting a bug, please follow the provided issue template and make sure to
provide enough details for someone else to be able to reproduce the bug.

### Fix Bugs

Any issues on GitHub that are tagged with "bug" and "help wanted" are open to
whoever wants to implement them.

### Write Documentation

Clear and thorough documentation is important for helping people be able to use
`bvbrc` effectively. For `bvbrc`, the main points of focus for documentation are
docstrings in the code and the official documentation pages. You are welcome to
contribute to the documentation in both these areas.

### Implement Features

> [!NOTE]
> The scope of `bvbrc` is mean to be pretty narrow so adding new features is not
> a high priority.

Adding new features is lower in priority than the above categories, but there is
likely some functionality that makes sense to add to `bvbrc`. Any issues that
are tagged with "enhancement" and "to do" are open to whoever would like to
implement them. Issues tagged as "enhancement" but without "to do" are ones
where an official decision still needs to be made on whether the feature will be
added.

### Submit Feedback

Feedback on the project is always welcome. The best way to send feedback is by
[filing an issue on GitHub](https://github.com/abates20/bvbrc/issues). If you
would like a feature to be added, please following these guidelines:

- Include a detailed explanation of how the feature would work
- The scope of `bvbrc` is meant to stay pretty narrow, so please provide a
  rationale for why the feature should be added

## Getting Started

Here are the basic steps to set up your local development environment:

1. Fork the `bvbrc` repo on GitHub.

2. Clone your fork locally:

    ```shell
    git clone git@github.com:[your_username]/bvbrc.git
    ```

3. Create a virtual environment for the project and install the project
    dependencies. I used [uv](https://docs.astral.sh/uv/) for this project:

    ```shell
    uv venv # Create the venv
    uv sync # Install dependencies into it
    ```

4. Create a new branch for development:

    ```shell
    git checkout -b name-of-your-branch
    ```

5. After making changes, make sure the code passes linting and any tests:

    ```shell
    uv run ruff check src
    uv run ruff format src
    # Tests have not been implemented yet
    ```

6. Commit your changes and push your branch to GitHub:

    ```shell
    git add .
    git commit -m "Description of your changes"
    git push origin name-of-your-branch
    ```

7. Submit a pull request on GitHub (make sure you follow the guidlines below).

## Pull Request Guidelines

Any pull requests should follow these guidelines:

- Include tests to ensure that the code changes are working properly.
- Update the docs appropriately based on any changes made.
- The code should work for all supported python versions (see pyproject.toml)

## Code of Conduct

By participating in this project, you are agreeing to the following principles
of conduct:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
