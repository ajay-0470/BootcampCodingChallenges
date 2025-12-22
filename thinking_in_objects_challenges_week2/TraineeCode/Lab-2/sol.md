The bug is that the  fill_account_data() function does not assign any values to the account object. Because of that, acc.acc_no remains None, causing a TypeError during string concatenation.

Hence the way to fix that is by properly initializing the data in the fill_account_data() function

        acc.acc_no = "004701"
        acc.name = "Nitesh"
        acc.balance = 45000.0