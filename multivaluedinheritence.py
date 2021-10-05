class company:
    branchname="codvita"
    branchid=25
    branchstreth=357
    def situation(self):
        print("data")
class employee:
    number_of_working=335
    number_of_notworking=22
class teamleader():
    team_lead_working=25
    team_lead_notworking=0
s1=company()
print("branchname =",s1.branchname)
print("brancid =",s1.branchid)
print("branchstreth =",s1.branchstreth)
s1.situation()
s2=employee()
print("number of working =",s2.number_of_working)
print("number of not working =",s2.number_of_notworking)
s3=teamleader()
print("team_lead_working =",s3.team_lead_working)
print("team_lead_notworking =",s3.team_lead_notworking)

