#!/usr/bin/env python3
"""
Test script to verify Airtable API connection.
This script tests basic connectivity to the DA Event Management System Airtable base.
"""

from pyairtable import Api
import os
from dotenv import load_dotenv

def test_connection():
    """Test connection to Airtable and display basic information."""

    load_dotenv()

    api_key = os.getenv('AIRTABLE_API_KEY')
    base_id = os.getenv('AIRTABLE_BASE_ID')

    if not api_key:
        print("❌ ERROR: AIRTABLE_API_KEY not found in .env file")
        print("Please add: AIRTABLE_API_KEY=patYourTokenHere")
        return False

    if not base_id:
        print("❌ ERROR: AIRTABLE_BASE_ID not found in .env file")
        print("Please add: AIRTABLE_BASE_ID=appYourBaseIdHere")
        return False

    print("🔍 Testing Airtable API connection...")
    print(f"   Base ID: {base_id[:8]}...")
    print(f"   API Key: {api_key[:10]}...")
    print()

    try:
        api = Api(api_key)
        base = api.base(base_id)

        print("✅ Successfully authenticated with Airtable API!")
        print()

        print("📊 Testing table access...")

        tables_to_test = [
            'Events Master',
            'Speakers',
            'Tasks & Workflow',
            'Volunteers & Staff',
            'Committees & Caucuses',
            'Email Communications',
            'Reports & Analytics'
        ]

        for table_name in tables_to_test:
            try:
                table = base.table(table_name)
                records = table.all()
                print(f"   ✅ {table_name}: {len(records)} records")
            except Exception as e:
                print(f"   ❌ {table_name}: Error - {str(e)}")

        print()
        print("📋 Sample Event Data:")
        events_table = base.table('Events Master')
        events = events_table.all()

        if events:
            first_event = events[0]['fields']
            print(f"   Event Name: {first_event.get('Event Name', 'N/A')}")
            print(f"   Event Type: {first_event.get('Event Type', 'N/A')}")
            print(f"   Status: {first_event.get('Status', 'N/A')}")
            print(f"   Event Date: {first_event.get('Event Date', 'N/A')}")
            print(f"   Organizer: {first_event.get('Event Organizer Name', 'N/A')}")
        else:
            print("   No events found in database")

        print()
        print("🎉 All tests passed! Airtable connection is working correctly.")
        return True

    except Exception as e:
        print(f"❌ ERROR: Failed to connect to Airtable")
        print(f"   {str(e)}")
        print()
        print("Troubleshooting:")
        print("1. Verify your API token is correct (starts with 'pat')")
        print("2. Verify your Base ID is correct (starts with 'app')")
        print("3. Check that the token has proper scopes (data.records:read, data.records:write)")
        print("4. Ensure the token has access to this specific base")
        return False

if __name__ == "__main__":
    success = test_connection()
    exit(0 if success else 1)