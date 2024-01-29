import os.path
import approval
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1vG55EpIkt45ZKNneCpFEbVVNWAxwOubAuqQqC4SfgHM"
SAMPLE_RANGE_NAME = "engenharia_de_software!A4:H27"


def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result['values']
    for students in values:
        presencesbooleam, presences = approval.situation_pres(int(students[2]) )
        if(presencesbooleam):
            situation = approval.situation(approval.avarege_calc(int(students[3]),int(students[4]),int(students[5])))
            students.append(situation)
            
            if(situation == "Exame Final"):
                students.append(str(approval.notefinal_calc(int(approval.avarege_calc(int(students[3]),int(students[4]),int(students[5])))))) 
            else: 
               students.append("0")  
              
        else:
          students.append(presences)
          students.append("0")
    print(values)  

  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()