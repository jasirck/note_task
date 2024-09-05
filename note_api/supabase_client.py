from supabase import create_client, Client

url = "https://dntzgnbopjydjhfzudqi.supabase.co"
anon_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRudHpnbmJvcGp5ZGpoZnp1ZHFpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU1MzQxMzQsImV4cCI6MjA0MTExMDEzNH0.ukUomMSgI38SPItKe8sWJb6U8p8IfKnumC-xx48rGtg"

supabase: Client = create_client(url, anon_key)

# Example: Fetch data from Supabase
data = supabase.table("notes").select("*").execute()
print(data)
