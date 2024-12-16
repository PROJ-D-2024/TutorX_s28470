import gspread
from oauth2client.service_account import ServiceAccountCredentials

creds_file = './credentials.json'
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
client = gspread.authorize(creds)

spreadsheet = client.open("Wine Quality Dataset")
main_account_email = 'your_email'
spreadsheet.share(main_account_email, perm_type='user', role='writer')

print(f"Access granted to {main_account_email}")