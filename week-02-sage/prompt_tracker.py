# prompt-tracker.py - Updated to include save dates
from datetime import date # We import this to get the current calendar date

def main():
    categories = ["learning", "creating", "evaluating", "other"]
    filename = "my-prompts.txt"

    while True:
        print("\n--- AI Prompt Tracker ---")
        print("1. Add Prompt")
        print("2. View Prompts (by category)")
        print("3. Search Prompts")
        print("4. Quit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            text = input("Enter the prompt text: ")
            print(f"Categories: {', '.join(categories)}")
            category = input("Enter category: ").lower()
            
            if category not in categories:
                print("Invalid category. Setting to 'other'.")
                category = "other"
                
            note = input("Enter a short note: ")

            # Get today's date in a simple YYYY-MM-DD format
            today = date.today() 

            # We add '|{today}' to the end of the line
            with open(filename, "a") as file:
                file.write(f"{category}|{text}|{note}|{today}\n")
            print(f"Prompt saved on {today}!")

        elif choice == "2":
            try:
                with open(filename, "r") as file:
                    lines = file.readlines()
                
                if not lines:
                    print("No prompts found yet.")
                    continue

                for cat in categories:
                    print(f"\n>> CATEGORY: {cat.upper()} <<")
                    found_any = False
                    
                    for line in lines:
                        parts = line.strip().split("|")
                        # Now parts[0]=cat, parts[1]=text, parts[2]=note, parts[3]=date
                        if parts[0] == cat:
                            print(f"- [{parts[3]}] Prompt: {parts[1]}") # Showing date first
                            print(f"  Note: {parts[2]}")
                            found_any = True
                    
                    if not found_any:
                        print("  (No prompts in this category)")

            except FileNotFoundError:
                print("No prompts file exists yet.")

        elif choice == "3":
            keyword = input("Enter search keyword: ").lower()
            found_count = 0
            
            try:
                with open(filename, "r") as file:
                    for line in file:
                        if keyword in line.lower():
                            parts = line.strip().split("|")
                            # Showing the date in the search results too
                            print(f"\n[{parts[0].upper()}] - Saved on: {parts[3]}")
                            print(f"Prompt: {parts[1]}")
                            print(f"Note:   {parts[2]}")
                            found_count += 1
                
                if found_count == 0:
                    print(f"No prompts found matching '{keyword}'.")
            except FileNotFoundError:
                print("No prompts file exists yet.")

        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()