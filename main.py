from task import Task

mytask=Task()
while mytask.run:
    def Run():
        
        run=input("Enter the command: \n")

        if run == "/A":
            mytask.Add()
            

        if run == "/R":
            mytask.Remove()
            


        if run == "/S":
            mytask.Show()
            
        if run == "/H":
            mytask.Help()
            
        if run == "/Q":
            mytask.End()
            
                        
    Run()



