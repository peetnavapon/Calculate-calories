import tkinter as tk

# ฟังก์ชันคำนวณแคลอรี่ที่ควรได้รับตามอายุและเพศ
def calculate_daily_calorie(age, gender):
    if age >= 2 and age <= 3:
        if gender == "ชาย":
            return 1000
        elif gender == "หญิง":
            return 1000
    elif age >= 4 and age <= 8:
        if gender == "ชาย":
            return 1400
        elif gender == "หญิง":
            return 1200
    elif age >= 9 and age <= 13:
        if gender == "ชาย":
            return 1800
        elif gender == "หญิง":
            return 1600
    elif age >= 14 and age <= 18:
        if gender == "ชาย":
            return 2200
        elif gender == "หญิง":
            return 1800
    elif age >= 19 and age <= 30:
        if gender == "ชาย":
            return 2400
        elif gender == "หญิง":
            return 2000
    elif age >= 31 and age <= 50:
        if gender == "ชาย":
            return 2200
        elif gender == "หญิง":
            return 1800
    elif age >= 51:
        if gender == "ชาย":
            return 2000
        elif gender == "หญิง":
            return 1600

# ฟังก์ชันเพิ่มอาหารและแคลอรี่
def add_food():
    food_name = food_entry.get()
    calorie = calorie_entry.get()
    food_list.insert(tk.END, f"{food_name}: {calorie} แคลอรี่")
    total_calories.set(total_calories.get() + int(calorie))
    food_entry.delete(0, tk.END)
    calorie_entry.delete(0, tk.END)

#ฟังก์ชันเปรียบเทียบอายุและเพศ
def age_gender():
    age = int(age_variable.get().split("-")[0])
    gender = gender_variable.get()
    daily_calorie = calculate_daily_calorie(age, gender)  # คำนวณแคลอรี่ที่ควรได้รับตามอายุและเพศ
    daily_calories.set(daily_calorie)  # กำหนดค่าแคลอรี่ที่ควรได้รับต่อวันให้กับตัวแปร daily_calories

# ฟังก์ชันคำนวณแคลอรี่ที่ควรได้รับตามที่กินไป
def calculate_remaining_calories():   
    age = int(age_variable.get().split("-")[0])
    gender = gender_variable.get() 
    daily_calorie = calculate_daily_calorie(age, gender)
    daily_calories.set(daily_calorie)
    consumed_calorie = total_calories.get()
    remaining_calorie = daily_calorie - consumed_calorie
    remaining_calories.set(remaining_calorie)

# GUI
window = tk.Tk()
window.title("โปรแกรมคำนวณแคลอรี่ที่ควรได้รับในแต่ละวัน")
window.geometry("1920x1080")


# ส่วนกรอกเพศและอายุ
age_label = tk.Label(window, text="อายุ:")
age_label.pack()
age_options = ["2-3 ปี", "4-8 ปี", "9-13 ปี", "14-18 ปี", "19-30 ปี", "31-50 ปี", "51 ปีขึ้นไป"]
age_variable = tk.StringVar(window)
age_variable.set(age_options[0])
age_dropdown = tk.OptionMenu(window, age_variable, *age_options)
age_dropdown.pack()

gender_label = tk.Label(window, text="เพศ:")
gender_label.pack()
gender_variable = tk.StringVar(window)
gender_variable.set("ชาย")
gender_radio_male = tk.Radiobutton(window, text="ชาย", variable=gender_variable, value="ชาย")
gender_radio_female = tk.Radiobutton(window, text="หญิง", variable=gender_variable, value="หญิง")
gender_radio_male.pack()
gender_radio_female.pack()

#ปุ่มดูปริมาณcalที่ควรได้รับในแต่ละวัน แปรผันตามเพศและอายุ
button=tk.Button(window, text="คำนวณ", command=age_gender)
button.pack()
daily_calories = tk.IntVar()
daily_calories_label = tk.Label(window, text="แคลอรี่ที่ควรได้รับต่อวัน:")
total_calories_entry = tk.Entry(window, textvariable=daily_calories, state="readonly")
daily_calories_label.pack()
total_calories_entry.pack()

# ส่วนเพิ่มอาหาร
food_label = tk.Label(window, text="อาหาร:")
food_label.pack()
food_entry = tk.Entry(window)
food_entry.pack()

calorie_label = tk.Label(window, text="แคลอรี่:")
calorie_label.pack()
calorie_entry = tk.Entry(window)
calorie_entry.pack()

add_button = tk.Button(window, text="เพิ่มรายการ", command=add_food)
add_button.pack()

# ส่วนแคลอรี่ทั้งหมด
food_list = tk.Listbox(window)
food_list.pack()

total_calories = tk.IntVar()
total_calories_label = tk.Label(window, text="แคลอรี่ที่รับประทานทั้งหมด:")
total_calories_label.pack()
total_calories_entry = tk.Entry(window, textvariable=total_calories, state="readonly")
total_calories_entry.pack()

# ส่วนคำนวณแคลอรี่

remaining_calories = tk.IntVar()
remaining_calories_label = tk.Label(window, text="แคลอรี่ที่เหลือ:")
remaining_calories_label.pack()
calculate_button = tk.Button(window, text="คำนวณ", command=calculate_remaining_calories)
calculate_button.pack()

remaining_calories_entry = tk.Entry(window, textvariable=remaining_calories, state="readonly")
remaining_calories_entry.pack() 


window.mainloop()
