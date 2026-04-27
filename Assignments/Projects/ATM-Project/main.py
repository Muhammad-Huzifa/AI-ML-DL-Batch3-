from atm import ATM
print("=" * 30 + "\nWELCOME TO PYTHON BANK ATM\n" + "=" * 30)

atm = ATM()
atm.authenticate()
if atm.current_user:
    atm.show_menu()