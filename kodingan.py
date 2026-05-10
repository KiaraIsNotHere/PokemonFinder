#All function

# 1
def pokeName():
     print("You are choosing Single pokemon")
     while True:
        inp = input("Enter pokemon name (or Q to quit): ").capitalize()
        if inp == "Q":
            print("Bye")
            break
        try:
            print()
            print(  f"Name: {inp.capitalize()} \n"
                    f"Type 1: {df.loc[inp,"Type1"]}\n"
                    f"Type 2: {df.loc[inp,"Type2"]}\n"
                    f"Weight: {df.loc[inp,"Weight"]} {"Weight" if round(df.loc[inp,"Weight"]) > round(df["Weight"].mean(numeric_only=True))  else "Light"}\n"
                    f"Height: {df.loc[inp,"Height"]} {"Tall" if round(df.loc[inp,"Height"]) > round(df["Height"].mean(numeric_only=True))  else "Short"}\n"
                    f"Legendary: {df.loc[inp,"Legendary"]}\n"
                    )
            print()
        except KeyError:
            print(f"{inp} not found")
            inp = input("Enter pokemon name (after error): ").capitalize()




# 2
def pokeData():
    Runnin = True
    while Runnin:
        jumlah = input("Whole Pokemon or Single Pokemon (W/S): ").upper()
        if jumlah not in ('W','S'):
            print("Please enter only (W/S)")
            continue
        
        print(f"You are Choosing {'Whole' if jumlah == 'W' else 'Single'}")

        tipe = input("What do ya want 2 know ? (sum - mean - min - max - count): ").upper()

        if tipe not in("MAX","MEAN","MIN","SUM","COUNT"):
            print("Please insert only (sum - mean - min - max - count)")
            continue
        
        if jumlah == 'W' and tipe == "MAX":
            print(df.max(numeric_only=True))
        elif jumlah == 'W' and tipe == "MEAN":
            print(df.mean(numeric_only=True))
        elif jumlah == 'W' and tipe == "SUM":
            print(df.sum(numeric_only=True))
        elif jumlah == 'W' and tipe == "MIN":
            print(df.min(numeric_only=True))
        elif jumlah == 'W' and tipe == "COUNT":
            print(df.count())

        if jumlah == 'S':
            col = input("Which coloumn would you like to know (Type1/2 - Height - Weight - legendary): ").upper()
            
            if col not in("TYPE1","TYPE2","HEIGHT","WEIGHT","LEGENDARY"):
                continue
            ops = {
                "MEAN": ("mean", {"numeric_only": True}),
                "COUNT": ("count", {}),
                "MAX": ("max", {"numeric_only": True}),
                "MIN": ("min", {"numeric_only": True}),
                "SUM": ("sum", {"numeric_only": True}),
            }
            
            if tipe in ops:
                method, kwargs = ops[tipe]
                print(getattr(df[col.capitalize()], method)(**kwargs))


# 3
def gerup():
    runnin = True
    while runnin:
        inp1 = input("Enter 1st Group (only Name - Type1/2): ").capitalize()
        if inp1 not in ("Name","Type1","Type2","Type 1","Type 2"):
            print("Please only enter (Name - Type1/2)")
            continue
        else:
            inp2 = input("Enter 2nd Group (only Height - Weight - Legendary): ").capitalize()
            if inp2 not in("Height","Weight","Legendary"):
                print("Please only enter (Height - Weight - Legendary)")
                inp2 = input("Enter 2nd Group (only Height - Weight - Legendary): ").capitalize()
                
            runnin = False

        if inp1 == "Type 1":
            inp1 = "Type1"
        elif inp1 == "Type 2":
            inp1 = "Type2"
        tipe = input("What do ya want 2 know ? (sum - mean - min - max - count - ALL of em): ").capitalize()
        tempe = df.groupby(inp1)

        while tipe not in("MAX","MEAN","MIN","SUM","COUNT"):
            break
        if tipe == "Max":
            print(tempe[inp2].max().to_string())
        elif tipe == "Min":
            print(tempe[inp2].min().to_string())
        elif tipe == "Sum":
            print(tempe[inp2].sum().to_string())
        elif tipe == "Count":
            print(tempe[inp2].count().to_string())
        elif tipe == "Mean":
            print(tempe[inp2].mean().to_string())