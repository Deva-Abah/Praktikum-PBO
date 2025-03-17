class BankAccount:
    def __init__(self, account_holder, balance, currency):
        self.account_holder = account_holder
        self.balance = balance
        self.currency = currency
    
    def apply_interest(self):
        if self.balance > 5000:
            self.balance *= 1.02  # Bunga 2%
        else:
            self.balance *= 1.01  # Bunga 1%
        self.balance = round(self.balance, 2)
    
    def convert_currency(self, amount, target_currency):
        #Simulasi kurs tetap untuk konversi mata uang
        exchange_rates = {("EUR", "USD"): 1.1, ("USD", "EUR"): 0.91}
        if (self.currency, target_currency) in exchange_rates:
            return amount * exchange_rates[(self.currency, target_currency)]
        return amount  #Jika tidak ada konversi
    
    def withdraw(self, amount, target_currency):
        #Konversi saldo jika mata uang berbeda
        converted_amount = self.convert_currency(amount, self.currency)
        if converted_amount > self.balance:
            print("Penarikan gagal! Saldo tidak mencukupi.")
        else:
            self.balance -= converted_amount
            print(f"Penarikan berhasil! Saldo baru: {self.currency} {self.balance}")
    
    def show_balance(self):
        print(f"{self.account_holder}'s Account: Balance = {self.currency} {self.balance}")

#Membuat akun bank dengan saldo awal
john = BankAccount("John", 6780, "USD")
emily = BankAccount("Emily", 4567, "EUR")

#Menampilkan saldo awal
john.show_balance()
john.apply_interest()  #Menambahkan bunga ke saldo
print("Bunga diterapkan... Saldo baru:")
john.show_balance()

emily.show_balance()
emily.withdraw(1700, "USD")  #Percobaan penarikan yang lebih besar dari saldo
print("Saldo setelah percobaan penarikan:")
emily.show_balance()