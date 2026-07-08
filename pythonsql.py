import pymysql

#connecting to mysql database
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="crud_pro"
)
cursor=conn.cursor()

#adding data to the database
def add_hotel():
    room_no=int(input("Enter the roon no: "))
    guest_name=input("Enter the guest name: ")
    helper_name=input("Enter the helper name: ")
    no_days=input("Enter the number of days the guest is staying: ")
    vip=input("Is the guest a VIP? (yes/no): ")
    
    sql="insert into hotel(room_no,guest_name,helper_name,no_days,vip) values(%s,%s,%s,%s,%s)"
    cursor.execute(sql,(room_no,guest_name,helper_name,no_days,vip))
    conn.commit()
    print("The data of the guest has been added successfully.")
    
    
#viewing the data of the guests
def display_hotel():
    cursor.execute("select * from hotel")
    rows=cursor.fetchall()
    print("\nRoom_no  Guest  Helper  No_days VIP")
    print("-" * 50)
    for r in rows:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}")
        
        
#update the data of the guest
def update_hotel():
    room_no=int(input("Enter the room number: "))
    guest_name=input("Enter the guest name: ")
    helper_name=input("Enter the helper name: ")
    no_days=input("Enter the number of days the guest is staying: ")
    vip=input("Is the guest a VIP? (yes/no): ")
    
    sql="""
    update hotel
    set guest_name=%s,helper_name=%s,no_days=%s,vip=%s
    where room_no=%s"""
    cursor.execute(sql,(guest_name,helper_name,no_days,vip,room_no))
    conn.commit
    print("The data of the guest is updated successfully..")
    
    
#deleting data of the guest
def delete_hotel():
    room_no=int(input("Enter the room number: "))
    sql="delete from hotel where room_no=%s"
    cursor.execute(sql,(room_no))
    conn.commit()
    print("The data of the guest is deleted successfully..")
    
    
#selecting only the vip guests
def vip_guest():
    cursor.execute("select * from hotel where vip='yes'")
    conn.commit()
    rows = cursor.fetchall()
    print("\nRoom_no  Guest  Helper  No_days VIP")
    print("-" * 50)
    for r in rows:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}")
        
        
#searching for a particular guest
def search_guest():
    room_no=int(input("Enter the room no: "))
    sql="select * from hotel where room_no=%s"
    cursor.execute(sql,(room_no))
    conn.commit()
    row=cursor.fetchone()
    print("\nRoom_no  Guest  Helper  No_days VIP")
    print("-" * 50)
    if row:
        print(f"{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{row[4]}")
    else:
        print("Guest not found")
        
 
 #counting the total number of guests
def total_guests():
    cursor.execute("select count(*) from hotel")
    total = cursor.fetchone()[0]

    cursor.execute("select count(*) from hotel where vip='yes'")
    vip = cursor.fetchone()[0]

    cursor.execute("select count(*) from hotel where vip='no'")
    non_vip = cursor.fetchone()[0]

    print("\n:::::::: COUNT OF GUESTS ::::::::")
    print("Total Guests     :", total)
    print("VIP Guests       :", vip)
    print("Non-VIP Guests   :", non_vip)
    
    
 #Checking the availability of the room       
def room_available():
    room_no = int(input("Enter Room Number: "))
    cursor.execute("select * from hotel where room_no=%s", (room_no,))
    room = cursor.fetchone()
    if room:
        print("Room is occupied by another guest.")
    else:
        print("Room is available.")
        
        
#condition for each function
while True:
    print("\n:::::::::::TRINAY HOTELS::::::::::::")
    print("i) Upload the data of the Guest")
    print("ii) Display the data of the Guest")
    print("iii) Update the data of the Guest")
    print("iv) Remove the data of the Guest")  
    print("v) Display only the VIP Guests")
    print("vi) Search for a particular Guest ")
    print("vii) Count the number of Guests")
    print("viii) Check for availability of room")
    print("ix) End") 
    
    choice=input("Choose an option from the data given below: ")
    if choice == "i":
        add_hotel()
    elif choice == "ii":
        display_hotel()
    elif choice =="iii":
        update_hotel()
    elif choice == "iv":
        delete_hotel()
    elif choice == "v":
        vip_guest()
    elif choice == "vi":
        search_guest()
    elif choice == "vii":
        total_guests()
    elif choice == "viii":
        room_available()
    elif choice == "ix":
        print("THANK YOU")
        break;
    else:
        print("Invalid Choice")
        
cursor.close()
conn.close()