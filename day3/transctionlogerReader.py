transactions = {}

try:

    with open("transactions.txt", "r") as file:
        for line in file:
            # Skip empty lines
            cleaned_line = line.strip()
            if not cleaned_line:
                continue
            
            try:
              
                name, amount_str = cleaned_line.split(",")
                name = name.strip()
                amount = float(amount_str.strip())
  
                if name in transactions:
                    transactions[name] += amount
                else:
                    transactions[name] = amount
            except ValueError:
              
                print(f"Skipping malformed line: {line.strip()}")

    if transactions:
        sorted_transactions = sorted(
            transactions.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\nTransaction Report")
        print("-" * 30)
        for name, total in sorted_transactions:
            print(f"{name}: {total:.2f}")

        with open("report.txt", "w") as report:
            report.write("Transaction Report\n")
            report.write("-" * 30 + "\n")
            for name, total in sorted_transactions:
                report.write(f"{name}: {total:.2f}\n")

        print("\nReport saved to report.txt")
    else:
        print("No valid transactions found to process.")

except FileNotFoundError:
    print("Error: transactions.txt file not found.")