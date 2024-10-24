import os

records = []

# 主選單
def display_menu():
    print("\n--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("------------------------")

# 新增資料
def add_record():
    while True:
        department = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機號碼: ")

        record = {
            "department": department,
            "name": name,
            "age": age,
            "phone": phone
        }
        records.append(record)

        cont = input("是否繼續新增資料? (y/n): ")
        if cont.lower() != 'y':
            break

# 查詢資料
def search_record():
    name = input("請輸入要查詢的姓名: ")
    found = False
    for record in records:
        if record["name"] == name:
            print("\n--- 查詢結果 ---")
            print("{:<10} {:<10} {:<5} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("{:<10} {:<10} {:<5} {:<15}".format(record["department"], record["name"], record["age"], record["phone"]))
            found = True
    if not found:
        print("查無此人。")

# 修改資料
def modify_record():
    name = input("請輸入要修改的姓名: ")
    for record in records:
        if record["name"] == name:
            print("當前資料:")
            print("{:<10} {:<10} {:<5} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("{:<10} {:<10} {:<5} {:<15}".format(record["department"], record["name"], record["age"], record["phone"]))
            print("\n1. 修改部門")
            print("2. 修改姓名")
            print("3. 修改年齡")
            print("4. 修改手機")
            choice = input("請選擇要修改的欄位 (1-4): ")
            if choice == '1':
                record["department"] = input("請輸入新的部門: ")
            elif choice == '2':
                record["name"] = input("請輸入新的姓名: ")
            elif choice == '3':
                record["age"] = input("請輸入新的年齡: ")
            elif choice == '4':
                record["phone"] = input("請輸入新的手機: ")
            else:
                print("無效的選項")
            print("\n--- 更新後的資料 ---")
            print("{:<10} {:<10} {:<5} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("{:<10} {:<10} {:<5} {:<15}".format(record["department"], record["name"], record["age"], record["phone"]))
            return
    print("查無此人。")

# 刪除資料
def delete_record():
    name = input("請輸入要刪除的姓名: ")
    for record in records:
        if record["name"] == name:
            print("找到的資料:")
            print("{:<10} {:<10} {:<5} {:<15}".format("部門", "姓名", "年齡", "手機"))
            print("{:<10} {:<10} {:<5} {:<15}".format(record["department"], record["name"], record["age"], record["phone"]))
            confirm = input("確定要刪除 {} 的資料嗎? (y/n): ".format(name))
            if confirm.lower() == 'y':
                records.remove(record)
                print("\n{} 的資料已刪除。".format(name))
                display_all_records()
            return
    print("查無此人。")

# 顯示所有資料
def display_all_records():
    if not records:
        print("目前沒有任何資料")
    else:
        print("{:<10} {:<10} {:<5} {:<15}".format("部門", "姓名", "年齡", "手機"))
        print("----------------------------------------")
        for record in records:
            print("{:<10} {:<10} {:<5} {:<15}".format(record["department"], record["name"], record["age"], record["phone"]))

# 退出系統
def main():
    while True:
        display_menu()
        choice = input("請選擇功能: ")
        if choice == '1':
            add_record()
        elif choice == '2':
            search_record()
        elif choice == '3':
            modify_record()
        elif choice == '4':
            delete_record()
        elif choice == '5':
            display_all_records()
        elif choice == '6':
            print("系統已退出。")
            break
        else:
            print("無效的選項，請重新選擇")

if __name__ == "__main__":
    main()
