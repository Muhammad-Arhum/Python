# Python
Documentation for the code:

This code calculates the aggregate for different universities based on the academic information provided by the user. The user is prompted to select the university they want to calculate the aggregate for, and then they are asked to enter their matric, FSc-1, and entry test marks along with their respective total marks. The code then calculates the percentage for each exam and uses the given weightage for each university to calculate the aggregate.

The universities supported in this code are NUST, UET Lahore, GIKI, FAST NU, and HiTEC Taxila.

Functions:

calculation(): This function takes in the weightage for each university along with the academic information provided by the user, calculates the percentage for each exam, and then calculates the aggregate using the given weightage.
Variables:

nust: This variable contains the string that represents the aggregate calculation formula for NUST.
uet: This variable contains the string that represents the aggregate calculation formula for UET Lahore.
giki: This variable contains the string that represents the aggregate calculation formula for GIKI.
fast: This variable contains the string that represents the aggregate calculation formula for FAST NU.
hitec: This variable contains the string that represents the aggregate calculation formula for HiTEC Taxila.
Inputs:

uni: This variable takes in the user's input for the university they want to calculate the aggregate for.
matric: This variable takes in the user's input for their matric marks.
matric_total: This variable takes in the user's input for the total marks in matric.
fsc: This variable takes in the user's input for their FSc-1 marks.
fsc_total: This variable takes in the user's input for the total marks in FSc-1.
et_marks: This variable takes in the user's input for their entry test marks.
et_total: This variable takes in the user's input for the total marks in the entry test.
Outputs:

agg_nust: This variable contains the calculated aggregate for NUST.
agg_uet: This variable contains the calculated aggregate for UET Lahore.
agg_giki: This variable contains the calculated aggregate for GIKI.
agg_fast: This variable contains the calculated aggregate for FAST NU (using FSc-1 marks).
agg_fast_m: This variable contains the calculated aggregate for FAST NU (using matric marks).
agg_hitec: This variable contains the calculated aggregate for HiTEC Taxila.
Note: The weightage for each university is given in the comments of the code
