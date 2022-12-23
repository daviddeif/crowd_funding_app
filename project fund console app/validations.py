import datetime
def date_check():
     try:
          start_project =input("enter start date in 'yyyy-mm-dd' formula in numbers: ").split("-")
          start_project = datetime.datetime(int(start_project[0]), int(start_project[1]), int(start_project[2]))
          end_project=input("enter end date in 'yyyy-mm-dd' formula in numbers: ").split("-")
          end_project=datetime.datetime(int(end_project[0]), int(end_project[1]), int(end_project[2]))
          if start_project>=end_project:
               print("error\n start date can't be before end date")
               date_check()
     except:
          print("date is invalid please try again...")
          date_check()
     return [start_project,end_project]
     
