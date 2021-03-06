import requests

print("\nWorking on it.")

MasterFile = open("./NFLScheduleByWeek/All/allGames.txt",'w')

for week in range(1,18):
    weekNum = "week"+str(week)
    URL = ("http://www.nfl.com/ajax/scorestrip?season=2018&seasonType=REG&week="+str(week))
    CurWeek = "./NFLScheduleByWeek/week"+str(week)+".out"
    CurWeekBare = "./NFLScheduleByWeek/Bare/week"+str(week)+"Bare.out"

    response = requests.get(URL)
#   with open(CurWeek, 'wb') as file:
#       file.write(response.content)

    week1 = str(response.content)

    HomeTeams = []
    if(week%3==0):
        print(".")

    #    print(week1)
    for num in range(len(week1)):
        if(week1[num]=='n' and week1[num+1] =='n'):
            num = num + 3
            #   print(week1[num])
            if(week1[num]=='"'):
                CurTeam = 0
                num = num + 1
                while(week1[num]!='"' and week1[num]!=' '):
                    CurTeam = CurTeam + 1
                    num = num + 1
                HomeTeams.append(week1[num-CurTeam:num])

    #    print(HomeTeams)
    #    print("NFL Week 1:")
    #    WeekCount = 1

    #    for num in range(0,len(HomeTeams)-1,2):
    #        print(" Game #"+str(WeekCount))
    #        WeekCount = WeekCount + 1
    #        print("     Home Team: "+str(HomeTeams[num]))
    #        print("     Away Team: "+str(HomeTeams[num+1])+"\n")

    fileOut = open(CurWeek,'w')
    WeekCount = 1
    for num in range(0,len(HomeTeams)-1,2):
        fileOut.write(" Game #"+str(WeekCount))
        WeekCount = WeekCount + 1
        fileOut.write("     Home Team: "+str(HomeTeams[num]))
        fileOut.write("     Away Team: "+str(HomeTeams[num+1])+"\n")
        
    fileOut.close()


    fileOut = open(CurWeekBare,'w')
    WeekCount = 1
    fileOut.write("{")
    for num in range(0,len(HomeTeams)-1,2):
        MasterFile.write(HomeTeams[num]+str(weekNum)+"\n"+HomeTeams[num+1]+str(weekNum)+"\n")
        if(num==len(HomeTeams)):
            fileOut.write("\""+HomeTeams[num]+"\": \""+HomeTeams[num+1]+"\"")
            break
        fileOut.write("\""+HomeTeams[num]+"\": \""+HomeTeams[num+1]+"\",\n")
    fileOut.write("}")
    fileOut.close()
    
MasterFile.close()
print("\nDone, checkout \"./NFLSchedule2018!\"")

