from rich.console import Console
from rich.table import Table
from rich.box import DOUBLE

user_names = ["User1", "User2", "User3", "User4"]
user_amounts = [0.0] * len(user_names)
user_history = [[] for _ in user_names]

def intro_func():
    print("Calculate Split:", "\nUsers:", sep="\n")
    for ind, name in enumerate(user_names, 1):
        print(ind, "-", name)
    print("\nChoices:", "d - Divide the amount", "a - Add money", "s - Sub money", "h - History", "q - Quit\n", sep="\n")

def history_func():
    print("\nHistory:")
    for name, his in zip(user_names, user_history):
        print(f"{name} --> {his}")
    print("Total =", sum(user_amounts), end="\n")

def split_func():
    console = Console()
    table = Table(show_header=True, show_footer=True, header_style="bold blue", box=DOUBLE, padding=(0, 4))

    table.add_column("ID", justify="center", max_width=10, footer="Total")
    table.add_column("Name")
    table.add_column("Amount", justify="center", footer=f"${round(sum(user_amounts), 2):.2f}")

    for ind, amo in enumerate(user_amounts):
        table.add_row(str(ind+1), user_names[ind], f"${amo:.2f}")

    console.print(table)
    print("\n")

def update_user_balance(user_ids, amount, is_addition):
    for i in user_ids:
        ind = int(i) - 1
        if is_addition:
            user_amounts[ind] += amount
        else:
            if user_amounts[ind] - amount < 0:
                raise ValueError("This is illegal because after this user has only a negative balance.")
            user_amounts[ind] -= amount
        user_history[ind].append(amount if is_addition else -amount)

def main():
    intro_func()
    run = True

    while run:
        try:
            input_str = input("Enter the choice [d or a or s or h or q] [person-id with space]: ").lower()
            sep_str = input_str.strip().split(" ")
            choice_str, *user_ids = sep_str
            user_ids = set(sep_str[1:])
            is_valid_ids = all(1 <= int(i) <= len(user_names) for i in user_ids)

            if choice_str == "q":
                print("\nFinal Split:")
                split_func()
                run = False
            elif choice_str == "h":
                history_func()
            elif choice_str in {"d", "a", "s"} and is_valid_ids:
                input_amount = input("Enter the amount: ").strip()
                amounts = round(sum(list(map(float, input_amount.split(" ")))), 2)
                
                if choice_str == "d":
                    rounded_avg = round(amounts/len(user_ids), 2)
                    for i in user_ids:                        
                        ind = int(i) - 1
                        user_amounts[ind] += rounded_avg
                        user_history[ind].append(rounded_avg)
                elif choice_str == "a":
                    update_user_balance(user_ids, amounts, True)
                elif choice_str == "s":
                    update_user_balance(user_ids, amounts, False)
                split_func()
            else:
                raise ValueError("Enter the correct choice letter.")  
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please enter the input with correct format and limits.")
            print("[d or a or s or h or q] [person-id with space]\n")


if __name__ == "__main__":
    main()
