import math

#PRINTING UNIVERSITIES NAME
print("1. NUST")
print("2. UET LAHORE")
print("3. GIKI")
print("4. FAST NU")
print("5. HiTEC TAXILA")


nust = "...AGGREGATE CALCULATION FOR NUST..."
uet = "...AGGREGATE CALCULATION FOR UET LAHORE..."
giki = "...AGGREGATE CALCULATION FOR GIKI..."
fast = "...AGGREGATE CALCULATION FOR FAST NU..."
hitec = "...AGGREGATE CALCULATION FOR HiTEC TAXILA..."

#CALCULATING AGGREGATE FOR UNI
def calculation(nust, uet, giki, fast, hitec):

#TAKING ACADEMIC INFO
    uni= input("ENTER UNIVERSITY : ")
    matric = int(input("Enter Matric Marks : "))
    matric_total = int(input("Enter Total Marks In Matric : "))
    fsc = int(input("Enter FSc-1 Marks : "))
    fsc_total = int(input("Enter Total Marks In FSc : "))
    et_marks = int(input("Enter Entry Test Marks : "))
    et_total = int(input("Enter Total Marks Of Entry Test : "))

#CALCULATING PERCENTAGES
    matric_percent = (matric / matric_total)*100
    fsc_per = (fsc/fsc_total)*100
    et_per = (et_marks / et_total)*100

##CALCULATING AGGREGATE FOR NUST 75% ET 15 FSC 10 MATRIC
    if uni == "1" or "NUST" or "nust":
                print(nust)
                agg_nust = (matric_percent*0.1) + (fsc_per*0.15) + (et_per*0.75)
                print("YOUR AGGREGATE IS: " + agg_nust)
                


## AGGREGATE FOR UET 50 FSC 33 ET 17 MATRIC
    elif uni == "2" or "uet lahore" "uet" "UET LAHORE":
                print(uet)
                agg_uet = (matric_percent * 0.17) + (fsc_per * 50) + (et_per * 33)
                print("YOUR AGGREGATE IS: " + agg_uet)

## AGGREGATE FOR GIKI 85 ET 10 FSC 5 MATRIC
    elif uni == "3" or "giki" or "GIKI":
                print(giki)
                agg_giki = (matric_percent * 0.5) + (fsc_per * 0.1) + (et_per * 0.85)
                print("YOUR AGGREGATE IS: " + agg_giki)

## AGGREGATE FOR FAST 50 FSC/MATRIC 50 ET
    elif uni == "4" or "fast" or "fast nu" or "FAST NU" or "FAST":
                print(fast)
                agg_fast = (fsc_per * 0.5) + (et_marks * 0.5)
                agg_fast_m = (matric_percent * 0.5) + (et_marks * 0.5)
                print("YOUR AGGREGATE IS(Using FSc Marks): " + agg_fast)
                print("YOUR AGGREGATE IS(Using Matric Marks): " + agg_fast_m)


## AGGREGATE FOR HITEC 50 ET 30 FSC 20 MATRIC
    elif uni == "5" or "hitec" or "HiTEC" or "HiTEC TAXILA":
                print(hitec)
                agg_hitec = (matric_percent * 0.2) + (fsc_per * 0.3) + (et_per * 0.5)
                print("YOUR AGGREGATE IS: " + agg_hitec)

calculation(nust, uet, giki, fast, hitec)


