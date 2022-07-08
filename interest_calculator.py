#İstinye Üniversitesi BIL101 Temel Programlama 1 (Python) mini proje 1.
#Aynı klasöre eklediğim "BIL101_Temel Programlama 1_MP1.pdf" yönergesine göre yazılmıştır.
# Burada koduma güzellik katsın diye ASCI art ekledim.
print("""                                                                
 __        __   _                             _          _   _                       
 \ \      / ___| | ___ ___  _ __ ___   ___   | |_ ___   | |_| |__   ___              
  \ \ /\ / / _ | |/ __/ _ \| '_ ` _ \ / _ \  | __/ _ \  | __| '_ \ / _ \             
   \ V  V |  __| | (_| (_) | | | | | |  __/  | || (_) | | |_| | | |  __/             
  ____/\_/ \___|_|\___\___/|_| |__ |_|\_____  \__\___/   \__|_|_|_|\____             
 |_ _|_ __ | |_ ___ _ __ ___ ___| |_   / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
  | || '_ \| __/ _ | '__/ _ / __| __| | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
  | || | | | ||  __| | |  __\__ | |_  | |__| (_| | | (__| |_| | | (_| | || (_) | |   
 |___|_| |_|\__\___|_|  \___|___/\__|  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
                                                                                     """)

# 4. Fonksiyon diğer bütün fonksiyonları içinde barındırır.
def main_function():
    #Burada Kullanıcıdan inputları aldım.
    name = str(input("Please enter your name:"))
    loan_amount = float(input("Loan amount:"))
    annual_interest_rate = float(input("Interest rate (per year):"))
    max_year = int(input("-> TIME LENGTH\n   Loan term in years:"))
    year_to_month = max_year*12
    max_month  = int(input("   Loan term in months:"))
    total_month = year_to_month + max_month 
    iteration_interval = int(input("   Iteration in months:"))
    start = 0

    # 2. Fonksiyon: Burada float olan çıktıları ekstra basamaklardan arındırdım.
    def simplified_money(a):
        return format(a, ".2f")

    # 3. Fonksiyon Burada faizi hesapladım total payment ve monthly payment olarak ekrana verdim.
    print("\nReport for",name,":\n" + 24*"-")
    def interest_print():
        interest_calc = (loan_amount/100)*(annual_interest_rate/12)*start
        total_payment = (interest_calc+loan_amount)
        monthly_payment = (total_payment/start)
        print("Total Payment:\n",simplified_money(total_payment),"$")
        print("Monthly Payment:\n",simplified_money(monthly_payment),"$")
        return 24*"-"

    # 1. Fonksiyon: Burada ay olarak bir süre girildiğinde onu yıla çevirdim.
    def month_to_year(): 
        bol1 = start//12
        bol2 = start%12
        bol1 = str(bol1)
        bol2 = str(bol2)
        if total_month>=1:
            year = ">>>" + " Year: " + bol1 + ", " + "Month: " +bol2
            return year

    # Burada kodumu döngüye soktum.
    while iteration_interval <= total_month:
        start += iteration_interval
        if start > total_month:
            break
        print(month_to_year())
        print(interest_print())  
        
main_function()
