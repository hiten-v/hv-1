import pickle
def inputmenu():
    obj1=open(r'Stud.txt','ab')
    print("###^^^^^####^^^^^####^^^^^###")
    print()
    print("****------WELCOME TO SCOOBEE DOO VEGETARIAN RESTAURENT-------****")
    print()
    print("###^^^^^####^^^^^####^^^^^###")
    print()
    print()
    t=True
    sum=0
    ordt=[]
    q=[]
    print("Please select the mode of your order :--")
    print()
    print(" PRESS 1 FOR DINE IN")
    print(" PRESS 2 FOR HOME DELIEVERY")
    s=int(input())
    item=0
    if s==1:
        print("CHOOSEN DINE IN")
        while t==True:
            print()
            print()
            print("PRESS 1 FOR FOOD MENU")
            print("PRESS 2 FOR BEVREAGES MENU")
            print("PRESS 3 FOR DESSERT MENU")
            print("PRESS 4 TO QUIT")
            k=int(input())
            if k==1:
                print("CHOOSEN FOOD MENU")
                print()
                print("PRESS 1 FOR BURGERS AND PIZZAS")
                print("PRESS 2 FOR PASTAS AND SANDWICHES")
                print("PRESS 3 FOR INDIAN SNACKS")
                t1=int(input())
                if t1==1:
                    print("CHOOSEN BURGERS AND PIZZAS")
                    print("PRESS 1 FOR CRISPY VEGGIE BURGER----RS. 65")
                    print("PRESS 2 FOR DELUXE VEGGIE BURGER-----RS. 95")
                    print("PRESS 3 FOR KING SUPREME BURGER------RS. 135")
                    print("PRESS 4 FOR VEG EXTRAVEGENZA PIZZA-----RS. 225")
                    print("PRESS 5 FOR FRESH PEPPY PANEER PIZZA-----RS. 165")
                    print("PRESS 6 FOR FARMHOUSE CLASSIC PIZZA-----RS. 190")
                    n1=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEMS YOU WANT TO ORDER")
                    c1=int(input())
                    if n1==1:
                        sum=sum+65*c1
                        item=item+c1
                        ordt.append("CRISPY VEGGIE BURGER")
                        q.append(c1)
                    if n1==2:
                        sum=sum+95*c1
                        item=item+c1
                        ordt.append("DELUXE VEGGIE BURGER")
                        q.append(c1)
                    if n1==3:
                        sum=sum+135*c1
                        item=item+c1
                        ordt.append("KING SUPREME BURGER")
                        q.append(c1)
                    if n1==4:
                        sum=sum+225*c1
                        item=item+c1
                        ordt.append("VEG EXTRAVEGENZA PIZZA")
                        q.append(c1)
                    if n1==5:
                        sum=sum+165*c1
                        item=item+c1
                        ordt.append("FRESH PEPPY PANEER PIZZA")
                        q.append(c1)
                    if n1==6:
                        sum=sum+190*c1
                        item=item+c1
                        ordt.append("FARMHOUSE CLASSIC PIZZA")
                        q.append(c1)
                if t1==2:
                    print("CHOOSEN PASTAS AND SANDWICHES")
                    print("PRESS 1 FOR TANGY RED SAUCEPASTA----RS. 145")
                    print("PRESS 2 FOR CREAMY WHITE SAUCE PASTA-----RS. 145")
                    print("PRESS 3 FOR SPAGHETTI------RS. 165")
                    print("PRESS 4 FOR MONSTER WRAP MIXVEGETABLE SANDWICH-----RS. 125")
                    print("PRESS 5 FOR GRILLED PANEER TIKKA SANDWICH-----RS. 165")
                    print("PRESS 6 FOR PERI PERI CHEESE CLUB SANDWICH-----RS. 150")
                    n2=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEMS YOU WANT TO ORDER")
                    c2=int(input())
                    if n2==1:
                        sum=sum+145*c2
                        item=item+c2
                        ordt.append("TANGY RED SAUCEPASTA")
                        q.append(c2)
                    if n2==2:
                        sum=sum+145*c2
                        item=item+c2
                        ordt.append("CREAMY WHITE SAUCE PASTA")
                        q.append(c2)
                    if n2==3:
                        sum=sum+165*c2
                        item=item+c2
                        ordt.append("SPAGHETTI")
                        q.append(c2)
                    if n2==4:
                        sum=sum+125*c2
                        item=item+c2
                        ordt.append("MONSTER WRAP MIXVEGETABLE SANDWICH")
                        q.append(c2)
                    if n2==5:
                        sum=sum+165*c2
                        item=item+c2
                        ordt.append("GRILLED PANEER TIKKA SANDWICH")
                        q.append(c2)
                    if n2==6:
                        sum=sum+150*c2
                        item=item+c2
                        ordt.append("PERI PERI CHEESE CLUB SANDWICH")
                        q.append(c2)
                if t1==3:
                    print("CHOOSEN INDIAN SNACKS")
                    print("PRESS 1 FOR PANI PURI----RS. 60")
                    print("PRESS 2 FOR BHALLA PAPDI CHAAT-----RS. 75")
                    print("PRESS 3 FOR VEG CHOWMEIN------RS. 80")
                    print("PRESS 4 FOR PAV BHAJI-----RS. 95")
                    print("PRESS 5 FOR ALOO TIKKI-----RS. 75")
                    print("PRESS 6 FOR SAMOSA-----RS. 60")
                    n3=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c3=int(input())
                    if n3==1:
                        sum=sum+60*c3
                        item=item+c3
                        ordt.append("PANI PURI")
                        q.append(c3)
                    if n3==2:
                        sum=sum+75*c3
                        item=item+c3
                        ordt.append("BHALLA PAPDI CHAAT")
                        q.append(c3)
                    if n3==3:
                        sum=sum+80*c3
                        item=item+c3
                        ordt.append("VEG CHOWMEIN")
                        q.append(c3)
                    if n3==4:
                        sum=sum+95*c3
                        item=item+c3
                        ordt.append("PAV BHAJI")
                        q.append(c3)
                    if n3==5:
                        sum=sum+75*c3
                        item=item+c3
                        ordt.append("ALOO TIKKI")
                        q.append(c3)
                    if n3==6:
                        sum=sum+60*c3
                        item=item+c3
                        ordt.append("SAMOSA")
                        q.append(c3)
            elif k==2:
                print("CHOOSEN BEVRAGES MENU")
                print()
                print("PRESS 1 FOR MOCKTAILS AND COLD DRINKS")
                print("PRESS 2 FOR COFFEE AND HOT DRINKS")
                print("PRESS 3 FOR MILKSHAKES ")
                t2=int(input())
                if t2==1:
                    print("CHOOSEN MOCKTAILS AND COLD DRINKS")
                    print("PRESS 1 FOR BLUE LAGOON----RS. 145")
                    print("PRESS 2 FOR CINDERELLA-----RS. 135")
                    print("PRESS 3 FOR CHERRY-BERRY------RS. 130")
                    print("PRESS 4 FOR GREEN APPLE COOLER-----RS. 145")
                    print("PRESS 5 FOR DIET COKE LEMONADE-----RS. 110")
                    print("PRESS 6 FOR MINT VIRGIN MOJITO-----RS. 100")
                    n4=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c4=int(input())
                    if n4==1:
                        sum=sum+145*c4
                        item=item+c4
                        ordt.append("BLUE LAGOON")
                        q.append(c4)
                    if n4==2:
                        sum=sum+135*c4
                        item=item+c4
                        ordt.append("CINDERELLA")
                        q.append(c4)
                    if n4==3:
                        sum=sum+130*c4
                        item=item+c4
                        ordt.append("CHERRY-BERRY")
                        q.append(c4)
                    if n4==4:
                        sum=sum+145*c4
                        item=item+c4
                        ordt.append("GREEN APPLE COOLER")
                        q.append(c4)
                    if n4==5:
                        sum=sum+110*c4
                        item=item+c4
                        ordt.append("DIET COKE LEMONADE")
                        q.append(c4)
                    if n4==6:
                        sum=sum+100*c4
                        item=item+c4
                        ordt.append("MINT VIRGIN MOJITO")
                        q.append(c4)
                if t2==2:
                    print("CHOOSEN COFFEE AND HOT DRINKS")
                    print("PRESS 1 FOR DARK AMERICANO----RS. 235")
                    print("PRESS 2 FOR CHOCOCHIP CAPPUCCINO-----RS. 245")
                    print("PRESS 3 FOR STRAWBERRY FRAPPACCINO------RS. 245")
                    print("PRESS 4 FOR PUMPKIN-SPICED LATTE-----RS. 200")
                    print("PRESS 5 FOR MASALA TEA-----RS. 125")
                    print("PRESS 6 FOR RED VELVET COFFEE-----RS. 190")
                    n5=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c5=int(input())
                    if n5==1:
                        sum=sum+235*c5
                        item=item+c5
                        ordt.append("DARK AMERICANO")
                        q.append(c5)
                    if n5==2:
                        sum=sum+245*c5
                        item=item+c5
                        ordt.append("CHOCOCHIP CAPPUCCINO")
                        q.append(c5)
                    if n5==3:
                        sum=sum+245*c5
                        item=item+c5
                        ordt.append("STRAWBERRY FRAPPACCINO")
                        q.append(c5)
                    if n5==4:
                        sum=sum+200*c5
                        item=item+c5
                        ordt.append("PUMPKIN-SPICED LATTE")
                        q.append(c5)
                    if n5==5:
                        sum=sum+165*c5
                        item=item+c5
                        ordt.append("MASALA TEA")
                        q.append(c5)
                    if n5==6:
                        sum=sum+190*c5
                        item=item+c5
                        ordt.append("RED VELVET COFFEE")
                        q.append(c5)
                if t2==3:
                    print("CHOOSEN MILKSHAKES")
                    print("PRESS 1 FOR CHOCOLATE MILKSHAKE----RS. 160")
                    print("PRESS 2 FOR STRAWBERRY MILKSHAKE-----RS. 165")
                    print("PRESS 3 FOR MANGO MILKSHAKE------RS. 160")
                    print("PRESS 4 FOR BLUEBERRY MILKSHAKE-----RS. 195")
                    print("PRESS 5 FOR COLD COFFEE-----RS. 135")
                    print("PRESS 6 FOR RASPBERRY DRAGON MILKSHAKE-----RS. 210")
                    n6=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c6=int(input())
                    if n6==1:
                        sum=sum+160*c6
                        item=item+c6
                        ordt.append("CHOCOLATE MILKSHAKE----")
                        q.append(c6)
                    if n6==2:
                        sum=sum+165*c6
                        item=item+c6
                        ordt.append("STRAWBERRY MILKSHAKE")
                        q.append(c6)
                    if n6==3:
                        sum=sum+160*c6
                        item=item+c6
                        ordt.append("MANGO MILKSHAKE")
                        q.append(c6)
                    if n6==4:
                        sum=sum+195*c6
                        item=item+c6
                        ordt.append("BLUEBERRY MILKSHAKE")
                        q.append(c6)
                    if n6==5:
                        sum=sum+135*c6
                        item=item+c6
                        ordt.append("COLD COFFEE")
                        q.append(c6)
                    if n6==6:
                        sum=sum+210*c6
                        item=item+c6
                        ordt.append("RASPBERRY DRAGON MILKSHAKE")
                        q.append(c6)
            elif k==3:
                print("CHOOSEN DESSERT MENU")
                print()
                print("PRESS 1 FOR CAKES AND PASTRIES")
                print("PRESS 2 FOR ICE-CREAMS AND SUNDAES")
                print("PRESS 3 FOR INDIAN SWEETS")
                t3=int(input())
                if t3==1:
                    print("CHOOSEN CAKES AND PASTRIES")
                    print("PRESS 1 FOR DOUBLE CHOCO-FLAKE CAKE-----RS. 285")
                    print("PRESS 2 FOR FRUIT TREAT CAKE-----RS. 300")
                    print("PRESS 3 FOR RED VELVET LAVA CAKE------RS. 320")
                    print("PRESS 4 FOR CHOCO-TRUFFLE PASTRY-----RS. 95")
                    print("PRESS 5 FOR STRAWBERRY PASTRY-----RS. 75")
                    print("PRESS 6 FOR PINEAPPLE PASTRY-----RS. 70")
                    n7=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c7=int(input())
                    if n7==1:
                        sum=sum+285*c7
                        item=item+c7
                        ordt.append("DOUBLE CHOCO-FLAKE CAKE")
                        q.append(c7)
                    if n7==2:
                        sum=sum+300*c7
                        item=item+c7
                        ordt.append("FRUIT TREAT CAKE")
                        q.append(c7)
                    if n7==3:
                        sum=sum+320*c7
                        item=item+c7
                        ordt.append("RED VELVET LAVA CAKE")
                        q.append(c7)
                    if n7==4:
                        sum=sum+95*c7
                        item=item+c7
                        ordt.append("CHOCO-TRUFFLE PASTRY")
                        q.append(c7)
                    if n7==5:
                        sum=sum+75*c7
                        item=item+c7
                        ordt.append("STRAWBERRY PASTRY")
                        q.append(c7)
                    if n7==6:
                        sum=sum+70*c7
                        item=item+c7
                        ordt.append("PINEAPPLE PASTRY")
                        q.append(c7)
                if t3==2:
                    print("CHOOSEN ICE-CREAMS AND SUNDAES")
                    print("PRESS 1 FOR ALPHANSO MANGO----RS. 85")
                    print("PRESS 2 FOR SWEET STRAWBWERRY-----RS. 75")
                    print("PRESS 3 FOR BELGIUM CHOCOCHIP------RS. 105")
                    print("PRESS 4 FOR FRUIT KITKAT SUNDAE-----RS. 135")
                    print("PRESS 5 FOR PURPLE COLA ICE-BLAST-----RS. 95")
                    print("PRESS 6 FOR RASPBERRY DRY-FRUIT SUNDAE-----RS. 140")
                    n8=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c8=int(input())
                    if n8==1:
                        sum=sum+85*c8
                        item=item+c8
                        ordt.append("ALPHANSO MANGO")
                        q.append(c8)
                    if n8==2:
                        sum=sum+75*c8
                        item=item+c8
                        ordt.append("SWEET STRAWBWERRY")
                        q.append(c8)
                    if n8==3:
                        sum=sum+105*c8
                        item=item+c8
                        ordt.append("BELGIUM CHOCOCHIP")
                        q.append(c8)
                    if n8==4:
                        sum=sum+135*c8
                        item=item+c8
                        ordt.append("FRUIT KITKAT SUNDAE")
                        q.append(c8)
                    if n8==5:
                        sum=sum+95*c8
                        item=item+c8
                        ordt.append("PURPLE COLA ICE-BLAST")
                        q.append(c8)
                    if n8==6:
                        sum=sum+140*c8
                        item=item+c8
                        ordt.append("RASPBERRY DRY-FRUIT SUNDAE")
                        q.append(c8)
                if t3==3:
                    print("CHOOSEN INDIAN SWEETS")
                    print("PRESS 1 FOR RASMALAI----RS. 60")
                    print("PRESS 2 FOR GULAB-JAMUN-----RS. 75")
                    print("PRESS 3 FOR RASGULLA------RS. 80")
                    print("PRESS 4 FOR LADDO-----RS. 65")
                    print("PRESS 5 FOR JALEBI-RABRI-----RS. 95")
                    print("PRESS 6 FOR HOT CHOCO BROWNIE-----RS. 110")
                    n9=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c9=int(input())
                    if n9==1:
                        sum=sum+60*c9
                        item=item+c9
                        ordt.append("RASMALAI")
                        q.append(c9)
                    if n9==2:
                        sum=sum+75*c9
                        item=item+c9
                        ordt.append("GULAB-JAMUN")
                        q.append(c9)
                    if n9==3:
                        sum=sum+80*c9
                        item=item+c9
                        ordt.append("RASGULLA")
                        q.append(c9)
                    if n9==4:
                        sum=sum+65*c9
                        item=item+c9
                        ordt.append("LADDO")
                        q.append(c9)
                    if n9==5:
                        sum=sum+95*c9
                        item=item+c9
                        ordt.append("JALEBI-RABRI")
                        q.append(c9)
                    if n9==6:
                        sum=sum+110*c9
                        item=item+c9
                        ordt.append("HOT CHOCO BROWNIE")
                        q.append(c9)
            elif k==4:
                t=False
            else:
                print("WRONG CHOICE")
                continue
    elif s==2:
        print("CHOOSEN HOME DELIVERY")
        print("DELIVERY CHARGES WILL BE APPLIED @RS. 75")
        sum=sum+75
        while t==True:
            print()
            print()
            print("PRESS 1 FOR FOOD MENU")
            print("PRESS 2 FOR BEVREAGES MENU")
            print("PRESS 3 FOR DESSERT MENU")
            print("PRESS 4 TO QUIT")
            k=int(input())
            if k==1:
                print("CHOOSEN FOOD MENU")
                print()
                print("PRESS 1 FOR BURGERS AND PIZZAS")
                print("PRESS 2 FOR PASTAS AND SANDWICHES")
                print("PRESS 3 FOR INDIAN SNACKS")
                t1=int(input())
                if t1==1:
                    print("CHOOSEN BURGERS AND PIZZAS")
                    print("PRESS 1 FOR CRISPY VEGGIE BURGER----RS. 65")
                    print("PRESS 2 FOR DELUXE VEGGIE BURGER-----RS. 95")
                    print("PRESS 3 FOR KING SUPREME BURGER------RS. 135")
                    print("PRESS 4 FOR VEG EXTRAVEGENZA PIZZA-----RS. 225")
                    print("PRESS 5 FOR FRESH PEPPY PANEER PIZZA-----RS. 165")
                    print("PRESS 6 FOR FARMHOUSE CLASSIC PIZZA-----RS. 190")
                    n1=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEMS YOU WANT TO ORDER")
                    c1=int(input())
                    if n1==1:
                        sum=sum+65*c1
                        item=item+c1
                        ordt.append("CRISPY VEGGIE BURGER")
                        q.append(c1)
                    if n1==2:
                        sum=sum+95*c1
                        item=item+c1
                        ordt.append("DELUXE VEGGIE BURGER")
                        q.append(c1)
                    if n1==3:
                        sum=sum+135*c1
                        item=item+c1
                        ordt.append("KING SUPREME BURGER")
                        q.append(c1)
                    if n1==4:
                        sum=sum+225*c1
                        item=item+c1
                        ordt.append("VEG EXTRAVEGENZA PIZZA")
                        q.append(c1)
                    if n1==5:
                        sum=sum+165*c1
                        item=item+c1
                        ordt.append("FRESH PEPPY PANEER PIZZA")
                        q.append(c1)
                    if n1==6:
                        sum=sum+190*c1
                        item=item+c1
                        ordt.append("FARMHOUSE CLASSIC PIZZA")
                        q.append(c1)
                if t1==2:
                    print("CHOOSEN PASTAS AND SANDWICHES")
                    print("PRESS 1 FOR TANGY RED SAUCEPASTA----RS. 145")
                    print("PRESS 2 FOR CREAMY WHITE SAUCE PASTA-----RS. 145")
                    print("PRESS 3 FOR SPAGHETTI------RS. 165")
                    print("PRESS 4 FOR MONSTER WRAP MIXVEGETABLE SANDWICH-----RS. 125")
                    print("PRESS 5 FOR GRILLED PANEER TIKKA SANDWICH-----RS. 165")
                    print("PRESS 6 FOR PERI PERI CHEESE CLUB SANDWICH-----RS. 150")
                    n2=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEMS YOU WANT TO ORDER")
                    c2=int(input())
                    if n2==1:
                        sum=sum+145*c2
                        item=item+c2
                        ordt.append("TANGY RED SAUCEPASTA")
                        q.append(c2)
                    if n2==2:
                        sum=sum+145*c2
                        item=item+c2
                        ordt.append("CREAMY WHITE SAUCE PASTA")
                        q.append(c2)
                    if n2==3:
                        sum=sum+165*c2
                        item=item+c2
                        ordt.append("SPAGHETTI")
                        q.append(c2)
                    if n2==4:
                        sum=sum+125*c2
                        item=item+c2
                        ordt.append("MONSTER WRAP MIXVEGETABLE SANDWICH")
                        q.append(c2)
                    if n2==5:
                        sum=sum+165*c2
                        item=item+c2
                        ordt.append("GRILLED PANEER TIKKA SANDWICH")
                        q.append(c2)
                    if n2==6:
                        sum=sum+150*c2
                        item=item+c2
                        ordt.append("PERI PERI CHEESE CLUB SANDWICH")
                        q.append(c2)
                if t1==3:
                    print("CHOOSEN INDIAN SNACKS")
                    print("PRESS 1 FOR PANI PURI----RS. 60")
                    print("PRESS 2 FOR BHALLA PAPDI CHAAT-----RS. 75")
                    print("PRESS 3 FOR VEG CHOWMEIN------RS. 80")
                    print("PRESS 4 FOR PAV BHAJI-----RS. 95")
                    print("PRESS 5 FOR ALOO TIKKI-----RS. 75")
                    print("PRESS 6 FOR SAMOSA-----RS. 60")
                    n3=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c3=int(input())
                    if n3==1:
                        sum=sum+60*c3
                        item=item+c3
                        ordt.append("PANI PURI")
                        q.append(c3)
                    if n3==2:
                        sum=sum+75*c3
                        item=item+c3
                        ordt.append("BHALLA PAPDI CHAAT")
                        q.append(c3)
                    if n3==3:
                        sum=sum+80*c3
                        item=item+c3
                        ordt.append("VEG CHOWMEIN")
                        q.append(c3)
                    if n3==4:
                        sum=sum+95*c3
                        item=item+c3
                        ordt.append("PAV BHAJI")
                        q.append(c3)
                    if n3==5:
                        sum=sum+75*c3
                        item=item+c3
                        ordt.append("ALOO TIKKI")
                        q.append(c3)
                    if n3==6:
                        sum=sum+60*c3
                        item=item+c3
                        ordt.append("SAMOSA")
                        q.append(c3)
            elif k==2:
                print("CHOOSEN BEVRAGES MENU")
                print()
                print("PRESS 1 FOR MOCKTAILS AND COLD DRINKS")
                print("PRESS 2 FOR COFFEE AND HOT DRINKS")
                print("PRESS 3 FOR MILKSHAKES ")
                t2=int(input())
                if t2==1:
                    print("CHOOSEN MOCKTAILS AND COLD DRINKS")
                    print("PRESS 1 FOR BLUE LAGOON----RS. 145")
                    print("PRESS 2 FOR CINDERELLA-----RS. 135")
                    print("PRESS 3 FOR CHERRY-BERRY------RS. 130")
                    print("PRESS 4 FOR GREEN APPLE COOLER-----RS. 145")
                    print("PRESS 5 FOR DIET COKE LEMONADE-----RS. 110")
                    print("PRESS 6 FOR MINT VIRGIN MOJITO-----RS. 100")
                    n4=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c4=int(input())
                    if n4==1:
                        sum=sum+145*c4
                        item=item+c4
                        ordt.append("BLUE LAGOON")
                        q.append(c4)
                    if n4==2:
                        sum=sum+135*c4
                        item=item+c4
                        ordt.append("CINDERELLA")
                        q.append(c4)
                    if n4==3:
                        sum=sum+130*c4
                        item=item+c4
                        ordt.append("CHERRY-BERRY")
                        q.append(c4)
                    if n4==4:
                        sum=sum+145*c4
                        item=item+c4
                        ordt.append("GREEN APPLE COOLER")
                        q.append(c4)
                    if n4==5:
                        sum=sum+110*c4
                        item=item+c4
                        ordt.append("DIET COKE LEMONADE")
                        q.append(c4)
                    if n4==6:
                        sum=sum+100*c4
                        item=item+c4
                        ordt.append("MINT VIRGIN MOJITO")
                        q.append(c4)
                if t2==2:
                    print("CHOOSEN COFFEE AND HOT DRINKS")
                    print("PRESS 1 FOR DARK AMERICANO----RS. 235")
                    print("PRESS 2 FOR CHOCOCHIP CAPPUCCINO-----RS. 245")
                    print("PRESS 3 FOR STRAWBERRY FRAPPACCINO------RS. 245")
                    print("PRESS 4 FOR PUMPKIN-SPICED LATTE-----RS. 200")
                    print("PRESS 5 FOR MASALA TEA-----RS. 125")
                    print("PRESS 6 FOR RED VELVET COFFEE-----RS. 190")
                    n5=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c5=int(input())
                    if n5==1:
                        sum=sum+235*c5
                        item=item+c5
                        ordt.append("DARK AMERICANO")
                        q.append(c5)
                    if n5==2:
                        sum=sum+245*c5
                        item=item+c5
                        ordt.append("CHOCOCHIP CAPPUCCINO")
                        q.append(c5)
                    if n5==3:
                        sum=sum+245*c5
                        item=item+c5
                        ordt.append("STRAWBERRY FRAPPACCINO")
                        q.append(c5)
                    if n5==4:
                        sum=sum+200*c5
                        item=item+c5
                        ordt.append("PUMPKIN-SPICED LATTE")
                        q.append(c5)
                    if n5==5:
                        sum=sum+165*c5
                        item=item+c5
                        ordt.append("MASALA TEA")
                        q.append(c5)
                    if n5==6:
                        sum=sum+190*c5
                        item=item+c5
                        ordt.append("RED VELVET COFFEE")
                        q.append(c5)
                if t2==3:
                    print("CHOOSEN MILKSHAKES")
                    print("PRESS 1 FOR CHOCOLATE MILKSHAKE----RS. 160")
                    print("PRESS 2 FOR STRAWBERRY MILKSHAKE-----RS. 165")
                    print("PRESS 3 FOR MANGO MILKSHAKE------RS. 160")
                    print("PRESS 4 FOR BLUEBERRY MILKSHAKE-----RS. 195")
                    print("PRESS 5 FOR COLD COFFEE-----RS. 135")
                    print("PRESS 6 FOR RASPBERRY DRAGON MILKSHAKE-----RS. 210")
                    n6=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c6=int(input())
                    if n6==1:
                        sum=sum+160*c6
                        item=item+c6
                        ordt.append("CHOCOLATE MILKSHAKE----")
                        q.append(c6)
                    if n6==2:
                        sum=sum+165*c6
                        item=item+c6
                        ordt.append("STRAWBERRY MILKSHAKE")
                        q.append(c6)
                    if n6==3:
                        sum=sum+160*c6
                        item=item+c6
                        ordt.append("MANGO MILKSHAKE")
                        q.append(c6)
                    if n6==4:
                        sum=sum+195*c6
                        item=item+c6
                        ordt.append("BLUEBERRY MILKSHAKE")
                        q.append(c6)
                    if n6==5:
                        sum=sum+135*c6
                        item=item+c6
                        ordt.append("COLD COFFEE")
                        q.append(c6)
                    if n6==6:
                        sum=sum+210*c6
                        item=item+c6
                        ordt.append("RASPBERRY DRAGON MILKSHAKE")
                        q.append(c6)
            elif k==3:
                print("CHOOSEN DESSERT MENU")
                print()
                print("PRESS 1 FOR CAKES AND PASTRIES")
                print("PRESS 2 FOR ICE-CREAMS AND SUNDAES")
                print("PRESS 3 FOR INDIAN SWEETS")
                t3=int(input())
                if t3==1:
                    print("CHOOSEN CAKES AND PASTRIES")
                    print("PRESS 1 FOR DOUBLE CHOCO-FLAKE CAKE-----RS. 285")
                    print("PRESS 2 FOR FRUIT TREAT CAKE-----RS. 300")
                    print("PRESS 3 FOR RED VELVET LAVA CAKE------RS. 320")
                    print("PRESS 4 FOR CHOCO-TRUFFLE PASTRY-----RS. 95")
                    print("PRESS 5 FOR STRAWBERRY PASTRY-----RS. 75")
                    print("PRESS 6 FOR PINEAPPLE PASTRY-----RS. 70")
                    n7=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c7=int(input())
                    if n7==1:
                        sum=sum+285*c7
                        item=item+c7
                        ordt.append("DOUBLE CHOCO-FLAKE CAKE")
                        q.append(c7)
                    if n7==2:
                        sum=sum+300*c7
                        item=item+c7
                        ordt.append("FRUIT TREAT CAKE")
                        q.append(c7)
                    if n7==3:
                        sum=sum+320*c7
                        item=item+c7
                        ordt.append("RED VELVET LAVA CAKE")
                        q.append(c7)
                    if n7==4:
                        sum=sum+95*c7
                        item=item+c7
                        ordt.append("CHOCO-TRUFFLE PASTRY")
                        q.append(c7)
                    if n7==5:
                        sum=sum+75*c7
                        item=item+c7
                        ordt.append("STRAWBERRY PASTRY")
                        q.append(c7)
                    if n7==6:
                        sum=sum+70*c7
                        item=item+c7
                        ordt.append("PINEAPPLE PASTRY")
                        q.append(c7)
                if t3==2:
                    print("CHOOSEN ICE-CREAMS AND SUNDAES")
                    print("PRESS 1 FOR ALPHANSO MANGO----RS. 85")
                    print("PRESS 2 FOR SWEET STRAWBWERRY-----RS. 75")
                    print("PRESS 3 FOR BELGIUM CHOCOCHIP------RS. 105")
                    print("PRESS 4 FOR FRUIT KITKAT SUNDAE-----RS. 135")
                    print("PRESS 5 FOR PURPLE COLA ICE-BLAST-----RS. 95")
                    print("PRESS 6 FOR RASPBERRY DRY-FRUIT SUNDAE-----RS. 140")
                    n8=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c8=int(input())
                    if n8==1:
                        sum=sum+85*c8
                        item=item+c8
                        ordt.append("ALPHANSO MANGO")
                        q.append(c8)
                    if n8==2:
                        sum=sum+75*c8
                        item=item+c8
                        ordt.append("SWEET STRAWBWERRY")
                        q.append(c8)
                    if n8==3:
                        sum=sum+105*c8
                        item=item+c8
                        ordt.append("BELGIUM CHOCOCHIP")
                        q.append(c8)
                    if n8==4:
                        sum=sum+135*c8
                        item=item+c8
                        ordt.append("FRUIT KITKAT SUNDAE")
                        q.append(c8)
                    if n8==5:
                        sum=sum+95*c8
                        item=item+c8
                        ordt.append("PURPLE COLA ICE-BLAST")
                        q.append(c8)
                    if n8==6:
                        sum=sum+140*c8
                        item=item+c8
                        ordt.append("RASPBERRY DRY-FRUIT SUNDAE")
                        q.append(c8)
                if t3==3:
                    print("CHOOSEN INDIAN SWEETS")
                    print("PRESS 1 FOR RASMALAI----RS. 60")
                    print("PRESS 2 FOR GULAB-JAMUN-----RS. 75")
                    print("PRESS 3 FOR RASGULLA------RS. 80")
                    print("PRESS 4 FOR LADDO-----RS. 65")
                    print("PRESS 5 FOR JALEBI-RABRI-----RS. 95")
                    print("PRESS 6 FOR HOT CHOCO BROWNIE-----RS. 110")
                    n9=int(input())
                    print("PLZ ENTER THE NO. OF SELECTED ITEM YOU WANT TO ORDER")
                    c9=int(input())
                    if n9==1:
                        sum=sum+60*c9
                        item=item+c9
                        ordt.append("RASMALAI")
                        q.append(c9)
                    if n9==2:
                        sum=sum+75*c9
                        item=item+c9
                        ordt.append("GULAB-JAMUN")
                        q.append(c9)
                    if n9==3:
                        sum=sum+80*c9
                        item=item+c9
                        ordt.append("RASGULLA")
                        q.append(c9)
                    if n9==4:
                        sum=sum+65*c9
                        item=item+c9
                        ordt.append("LADDO")
                        q.append(c9)
                    if n9==5:
                        sum=sum+95*c9
                        item=item+c9
                        ordt.append("JALEBI-RABRI")
                        q.append(c9)
                    if n9==6:
                        sum=sum+110*c9
                        item=item+c9
                        ordt.append("HOT CHOCO BROWNIE")
                        q.append(c9)
            elif k==4:
                t=False
            else:
                print("WRONG CHOICE")
                continue
    if(item>0):
        pickle.dump(ordt,obj1)
        pickle.dump(q,obj1)
        print()
        print()
        print("###^^^^^####^^^^^####^^^^^###")
        print()
        print("YOUR CHOOSEN ITEMS ARE.......")
        for a in ordt:
            for b in q:
                print(a," ........Qty:",b)
                break
            q.pop(0)
        print()
        print()
        print("Total bill without TAXES...",sum)
        tax=(14.39*2)+sum
        pickle.dump(tax,obj1)
        print()
        print("GST RATE IS 9% CGST AND 9% SGST")
        print("TOATL TAXES --- 14.39*2")
        print()
        print("SUB TOTAL --> ", tax)
        print()
        print()
        print("###^^^^^####^^^^^####^^^^^###")
        print()
        print("****------THANK-YOU FOR VISITING SCOOBEE DOO VEGETARIAN RESTAURENT-------****")
        print()
        print("DO COME AGAIN SOON.....")
        print()
        print("###^^^^^####^^^^^####^^^^^###")
    else:
        print()
        print("**********DO VISIT OUR RESTAURENT AGAIN************")
        print()
    obj1.close()
def dispmenu():
    obj1=open(r'Stud.txt',"rb")
    data=[]
    try:
        while True:
            data=pickle.load(obj1)
            print(data)
    except Exception as e:
        print()
    obj1.close()
while True:
    print("1. New Order \n2. Previous Orders\n3. Exit")
    ch=int(input("Enter your choice <1-3> ="))
    if ch==1:
        inputmenu()
    elif ch==2:
        dispmenu()
    elif ch==3:
        break
    else:
        print("Wrong op. selected")
    op=input("Do you want to continue <y/n>=")
    if op in "Nn":
        break
