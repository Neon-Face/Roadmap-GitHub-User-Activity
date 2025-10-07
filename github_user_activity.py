import requests
import sys

def _check_args(args):
    """Checks if a username argument is provided."""
    # sys.argv[0] is the script name, so we need at least 2 elements for a username
    if len(args) < 2:
        print("Error: Username is required.", file=sys.stderr)
        print("Usage: python your_script_name.py <username>", file=sys.stderr)
        return True # Indicates an error
    return False # Indicates arguments are okay

def fetch_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    event_list = []
    try:
        response = requests.get(url)
        response.raise_for_status()
        events = response.json()
        if len(events) == 0:
            print(f"No events found for user '{username}'.")
            return
        for event in events:
            type = event['type'][:-5]
            if type == "Create":
                event_list.append(f"Create - {event['payload']['ref_type']} {event['repo']['url']}")
            elif type == "Delete":
                event_list.append(f"Delete - {event['payload']['ref_type']} {event['repo']['url']}")
            elif type == "Fork":
                event_list.append(f"Fork - {event['repo']['url']}")
            elif type == "PullRequest":
                event_list.append(f"Pull Request - {event['payload']['number']} {event['payload']['action']} {event['repo']['url']}")
            elif type == "Push":
                event_list.append(f"Push - {event['payload']['size']} commits to {event['repo']['url']}")
            elif type == "Watch":
                event_list.append(f"Watch - {event['payload']['action']} {event['repo']['url']}")
        
        print(f"Events of {username}:")
        for event in event_list:
            print(f"{event}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error: Network connection failed. Check your internet connection. {conn_err}", file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.Timeout as timeout_err:
        print(f"Error: Request timed out. The server took too long to respond. {timeout_err}", file=sys.stderr)
        sys.exit(1) # Exit after handling timeout error
    except requests.exceptions.RequestException as req_err:
        # Catch any other requests-related exceptions
        print(f"Error: An unexpected request error occurred: {req_err}", file=sys.stderr)
        sys.exit(1) # Exit after handling general request error
    except ValueError as val_err: # For issues with response.json() if content is not JSON
        print(f"Error: Failed to decode JSON response from API. {val_err}", file=sys.stderr)
        print(f"Raw response: {response.text[:200]}...", file=sys.stderr) # Show part of raw response
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Error: An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    
    
    
def main():
    args = sys.argv
    if _check_args(args):
        sys.exit(1)
    username = args[1]
    fetch_activity(username)

if __name__ == "__main__":
    main()



        
        




