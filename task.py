import sqlite3
class Task:


    def __init__(self):
        self.con = sqlite3.connect("task.db")
        self.cursor = self.con.cursor()
        self.cursor.execute("SELECT task_col FROM task;")
        self.run = True
        self.result=[]
        print(
            """
            type /A to add a task \n
            type /R to remove a task\n
            type /S to see all tasks\n
            type /Q to end\n"""
            
        )


    def Add(self):
        add_task=input("Enter the task: \n")
        self.cursor.execute(f"INSERT INTO task (task_col) VALUES ('{add_task}');")
        self.Show()

    def Remove(self):
        remove_task=input("What you wanna remove? \n : ") 
        self.cursor.execute(f"DELETE FROM task WHERE task_col='%{remove_task}%'; ")
        self.Show()


    def Show(self):
        self.cursor.execute("SELECT * FROM task;")
        self.result = self.cursor.fetchall()
        print(self.result)
    

    def End(self):
        self.run = False

    def Help():
        print(
            """
            type /Add to add a task \n
            type /Remove to remove a task\n
            type /Show to see all tasks\n
            type /End to end\n"""
            
        )

