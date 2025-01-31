"""
LinkedIn Network Extractor
Extracts your LinkedIn network connections and their connections,
creating a JSON file suitable for network visualization.
"""

from linkedin_api import Linkedin
from getpass import getpass
import json
from typing import Dict, List, Set
import sys

# Constants
MAX_CONNECTIONS = 50  # Limit number of first-degree connections to process
OUTPUT_FILE = 'network_data.json'

def get_credentials() -> tuple[str, str]:
    """Prompt user for LinkedIn credentials."""
    try:
        email = input("Please input the email you use to log into LinkedIn:\n")
        password = getpass("Please input your LinkedIn password:\n")
        return email, password
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(1)

def initialize_linkedin_api(email: str, password: str) -> tuple[Linkedin, str]:
    """Initialize LinkedIn API and get user's profile ID."""
    try:
        api = Linkedin(email, password)
        profile_id = input("Please input your LinkedIn public profile id:\n")
        profile = api.get_profile(profile_id)
        user_id = profile["profile_id"]
        return api, profile_id, user_id
    except Exception as e:
        print(f"Error connecting to LinkedIn: {str(e)}")
        sys.exit(1)

def extract_network_data(api: Linkedin, profile_id: str, user_id: str) -> tuple[Set[str], List[Dict]]:
    """Extract network connections and build nodes/links data."""
    public_ids: Set[str] = {profile_id}
    links: List[Dict] = []
    
    try:
        # Get first-degree connections
        connections = api.get_profile_connections(user_id)
        total_connections = len(connections)
        
        print(f"Found {total_connections} connections. Processing up to {MAX_CONNECTIONS}...")
        
        for index, connection in enumerate(connections, 1):
            print(f"Downloading connection {index} of {min(total_connections, MAX_CONNECTIONS)}")
            
            if index > MAX_CONNECTIONS:
                break
                
            first_degree_id = connection["public_id"]
            public_ids.add(first_degree_id)
            links.append({
                "source": profile_id,
                "target": first_degree_id
            })
            
            # Get second-degree connections
            second_connections = api.get_profile_connections(connection["urn_id"])
            for second_connection in second_connections:
                second_degree_id = second_connection["public_id"]
                if second_degree_id != profile_id:
                    public_ids.add(second_degree_id)
                    links.append({
                        "source": first_degree_id,
                        "target": second_degree_id
                    })
                    
        return public_ids, links
        
    except Exception as e:
        print(f"Error extracting network data: {str(e)}")
        sys.exit(1)

def save_network_data(public_ids: Set[str], links: List[Dict]) -> None:
    """Save network data to JSON file."""
    try:
        nodes = [{"publicId": pid} for pid in public_ids]
        
        network_data = {
            "nodes": nodes,
            "links": links
        }
        
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(network_data, f, indent=4)
            
        print(f"\nNetwork data saved to {OUTPUT_FILE}")
        print(f"Total nodes: {len(nodes)}")
        print(f"Total connections: {len(links)}")
            
    except Exception as e:
        print(f"Error saving network data: {str(e)}")
        sys.exit(1)

def main():
    """Main execution function."""
    # Get credentials and initialize API
    email, password = get_credentials()
    api, profile_id, user_id = initialize_linkedin_api(email, password)
    
    # Extract network data
    public_ids, links = extract_network_data(api, profile_id, user_id)
    
    # Save results
    save_network_data(public_ids, links)

if __name__ == "__main__":
    main()
