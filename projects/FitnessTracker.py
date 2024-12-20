import sqlite3

con=sqlite3.connect('fitnesstracker.db')
cur=con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS WORKOUTS(
            ID NUMBER PRIMARY KEY,
            WORKOUT_TYPE VARCHAR(25) NOT NULL,
            DURATION NUMBER NOT NULL,
            CALORIES NUMBER NOT NULL,
            DATE DATE NOT NULL)''')

con.commit()

def log_workout():
    id=int(input('Enter the id:'))
    workout_type=input('Enter the workout name:')
    duration=int(input('Enter the duration in minutes:'))
    calories=int(input('Enter the calories burned:'))
    date=input('Enter the date:')
    cur.execute('INSERT INTO WORKOUTS VALUES(?, ?, ?, ?, ?)',(id,workout_type,duration,calories,date))
    con.commit() 
    print('Workout Logged Successfully!')

def view_workouts():
    view=cur.execute('SELECT * FROM WORKOUTS')
    rows=view.fetchall()
    if rows:
        print('Workout History:')
        for row in rows:
            print(f'ID : {row[0]} , workout_type : {row[1]} , duration : {row[2]} , calories : {row[3]} , date : {row[4]}')
    else:
        print('No workouts found')


def view_stat():
    var=cur.execute('SELECT SUM(DURATION),SUM(CALORIES) FROM WORKOUTS')
    stat=var.fetchone()
    duration=stat[0] or 0
    calories=stat[1] or 0
    print(f'Total duration of workout is {duration}')
    print(f'Total amount of calories burned is {calories}')

def main():
    while True:
        print("\nFitness Tracker")
        print("1. Log a workout")
        print("2. View all workouts")
        print("3. View statistics")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            log_workout()
        elif choice == '2':
            view_workouts()
        elif choice == '3':
            view_stat()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again")


main()
con.close()