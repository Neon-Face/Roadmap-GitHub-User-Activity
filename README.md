# GitHub User Activity Tracker

## Project URL

https://roadmap.sh/projects/github-user-activity

## Introduction

This is a simple command-line interface (CLI) tool written in Python to fetch and display recent public activity for any given GitHub user. It utilizes the GitHub Events API to show various interactions like pushes, pull requests, forks, and watches.

## Features

*   Fetches recent public events for a specified GitHub username.
*   Parses and displays different types of GitHub events in a human-readable format.
*   Provides basic error handling for network issues, API errors (like user not found), and JSON decoding problems.

## Requirements

*   Python 3.x
*   The `requests` library.

### Installing `requests`

If you don't have the `requests` library installed, you can install it using pip:

```bash
pip install requests
```

## How to Run

1.  **Save the script:** Save the provided Python code as `github_activity.py` (or any other `.py` filename you prefer) in a directory of your choice.
2.  **Open your terminal/command prompt:** Navigate to the directory where you saved `github_activity.py`.

    ```bash
    cd /path/to/your/project
    ```

3.  **Execute the script:** Run the script using `python github_activity.py` followed by the GitHub username you want to check.

## Usage

```bash
python github_activity.py <username>
```

Replace `<username>` with the actual GitHub username you wish to query.

### Examples

*   **To check activities for the user `octocat`:**
    ```bash
    python github_activity.py octocat
    ```
*   **If you forget to provide a username:**
    ```bash
    python github_activity.py
    ```
    This will output an error message:
    ```
    Error: Username is required.
    Usage: python github_activity.py <username>
    ```

## Event Types Displayed

The script currently parses and displays the following event types:

*   **Create Event:** (e.g., creating a branch, tag, or repository)
*   **Delete Event:** (e.g., deleting a branch or tag)
*   **Fork Event:** (forking a repository)
*   **PullRequest Event:** (opening, closing, or updating a pull request)
*   **Push Event:** (pushing commits to a repository)
*   **Watch Event:** (starring a repository)

Other event types returned by the GitHub API will currently be ignored.

## Important Notes on GitHub API Rate Limits

*   **Unauthenticated Access:** The GitHub API has strict [rate limits](https://docs.github.com/en/rest/overview/rate-limits-for-the-rest-api) for unauthenticated requests. You are typically limited to **60 requests per hour per IP address**.
*   **`403 Forbidden` Errors:** If you make too many requests within an hour, the API will start returning `403 Forbidden` errors.
*   **Authentication (for extended use):** For more frequent use, you would need to authenticate your requests using a [Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens). This script currently does not support authentication, but it's a common next step for projects interacting with GitHub's API.
