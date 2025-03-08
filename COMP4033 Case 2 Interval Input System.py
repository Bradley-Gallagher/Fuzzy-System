#Made By
#Bradley Gallagher (20599466)
#&
#Benjamin Hall (20603460)

import matplotlib.pyplot as plt
import numpy as np
import skfuzzy as fuzz

#Input Lists used to store all test data
age = []
temperature = []
headache = []

#Loop to allow for multiple user inputs to be processed
while True:
    while True:
        try:
            agemininput = float(input("Please enter the patient's Age Range Minimum: "))
            agemaxinput = float(input("Please enter the patient's Age Range Maximum: "))
            tempmininput = float(input("Please enter the patient's Temperature Range Minimum: "))
            tempmaxinput = float(input("Please enter the patient's Temperature Range Maximum: "))
            headmininput = float(input("Please enter the patient's Headache Severity Range Minimum: "))
            headmaxinput = float(input("Please enter the patient's Headache Severity Range Maximum: "))
        except ValueError:
            print("Please Provide a Numerical Input!")
            continue
        if agemininput < 0 or agemininput > 130 or agemaxinput < 0 or agemaxinput > 130:
            print("Please Enter a Valid Age! (0-120)")
            continue
        if agemininput >= agemaxinput:
            print("Please Ensure the Minimum Age is LESS than the Maximum Age!")
            continue
        if tempmininput < 0 or tempmininput > 100 or tempmaxinput < 0 or tempmaxinput > 100:
            print("Please Enter a Valid Temperature! (0-100)")
            continue
        if tempmininput >= tempmaxinput:
            print("Please Ensure the Minimum Temperature is LESS than the Maximum Temperature!")
            continue
        if headmininput < 0 or headmininput > 10 or headmaxinput < 0 or headmaxinput > 10:
            print("Please Enter a Valid Headache Severity! (0-10)")
            continue
        if headmininput >= headmaxinput:
            print("Please Ensure the Minimum Headache Severity is LESS than the Maximum Headache Severity!")
            continue
        age.append([agemininput, agemaxinput])
        temperature.append([tempmininput, tempmaxinput])
        headache.append([headmininput, headmaxinput])
        break
    validate = input("Please Enter 'Y' If You Would Like To Enter Another Patient's Details: ")
    if validate.lower() == "y":
        print("")
        continue
    else:
        print("")
        break

#Enter Y to reduce the amount of defuzzified outcomes provided (Entering Y will increase the output graphs and text outputs readability)
graphreductor = input("Please Enter 'Y' If You Would ONLY Like To View Centroid Defuzzification For Mamdani Inference: ")

# Age Membership Set Parameters and Set Ranges/Shape
age_child_a = 0
age_child_b = 0
age_child_c = 8
age_child_d = 15

age_adult_a = 8 
age_adult_b = 15 
age_adult_c = 60 
age_adult_d = 70 

age_elderly_a = 60 
age_elderly_b = 70 
age_elderly_c = 130
age_elderly_d = 130

x_age = np.arange(0, 131, 1)

fuzzyage_child = fuzz.trapmf(x_age, [age_child_a, age_child_b, age_child_c, age_child_d])
fuzzyage_adult = fuzz.trapmf(x_age, [age_adult_a, age_adult_b, age_adult_c, age_adult_d])
fuzzyage_elderly = fuzz.trapmf(x_age, [age_elderly_a, age_elderly_b, age_elderly_c, age_elderly_d])

# Temperature Membership Set Parameters and Set Ranges/Shape
temp_hypo_a = 0
temp_hypo_b = 0
temp_hypo_c = 35
temp_hypo_d = 36.3

temp_average_a = 36
temp_average_b = 37
temp_average_c = 38

temp_fever_a = 37.7
temp_fever_b = 41
temp_fever_c = 100
temp_fever_d = 100

x_temp = np.arange(0, 101, 1)

fuzzytemp_hypo = fuzz.trapmf(x_temp, [temp_hypo_a, temp_hypo_b, temp_hypo_c, temp_hypo_d])
fuzzytemp_average = fuzz.trimf(x_temp, [temp_average_a, temp_average_b, temp_average_c])
fuzzytemp_fever = fuzz.trapmf(x_temp, [temp_fever_a, temp_fever_b, temp_fever_c, temp_fever_d])

# Headache Severity Membership Set Parameters and Set Ranges/Shape
head_norm_a = 0
head_norm_b = 0
head_norm_c = 4

head_benign_a = 3
head_benign_b = 4
head_benign_c = 6
head_benign_d = 7

head_malign_a = 5
head_malign_b = 9
head_malign_c = 10
head_malign_d = 10

x_head = np.arange(0, 11, 1)

fuzzyhead_norm = fuzz.trimf(x_head, [head_norm_a, head_norm_b, head_norm_c])
fuzzyhead_benign = fuzz.trapmf(x_head, [head_benign_a, head_benign_b, head_benign_c, head_benign_d])
fuzzyhead_malign = fuzz.trapmf(x_head, [head_malign_a, head_malign_b, head_malign_c, head_malign_d])

# Urgency Response Membership Set Parameters and Set Ranges/Shape
non_urgent_a = 0
non_urgent_b = 0
non_urgent_c = 10
non_urgent_d = 40

semi_urg_a = 25
semi_urg_b = 40
semi_urg_c = 60
semi_urg_d = 75

urgent_a = 60
urgent_b = 90
urgent_c= 100
urgent_d = 100

x_urgency = np.arange(0, 101, 1)

fuzzyurg_low = fuzz.trapmf(x_urgency, [non_urgent_a, non_urgent_b, non_urgent_c, non_urgent_d])
fuzzyurg_mid = fuzz.trapmf(x_urgency, [semi_urg_a, semi_urg_b, semi_urg_c, semi_urg_d])
fuzzyurg_high = fuzz.trapmf(x_urgency, [urgent_a, urgent_b, urgent_c, urgent_d])

# Declaration of subplots to store the input/output membership graphs on 
fig, (ax0, ax1, ax2, ax3, ax4) = plt.subplots(nrows=5, figsize=(12, 15)) 
plt.subplots_adjust(hspace=0.4, wspace=0.4) 

# For each input, plot the age input onto the Age graph and the relevant membership set
num = 1
for x in age:
    xmemberlow = fuzz.interp_membership(x_age, fuzzyage_child, x[0])
    xmemberhigh = fuzz.interp_membership(x_age, fuzzyage_child, x[1])
    if fuzz.interp_membership(x_age, fuzzyage_adult, x[0]) > fuzz.interp_membership(x_age, fuzzyage_child, x[0]):
        xmemberlow = fuzz.interp_membership(x_age, fuzzyage_adult, x[0])
    if fuzz.interp_membership(x_age, fuzzyage_elderly, x[0]) > xmemberlow:
        xmemberlow = fuzz.interp_membership(x_age, fuzzyage_elderly, x[0])
    if fuzz.interp_membership(x_age, fuzzyage_adult, x[1]) > fuzz.interp_membership(x_age, fuzzyage_child, x[1]):
        xmemberhigh = fuzz.interp_membership(x_age, fuzzyage_adult, x[1])
    if fuzz.interp_membership(x_age, fuzzyage_elderly, x[1]) > xmemberhigh:
        xmemberhigh = fuzz.interp_membership(x_age, fuzzyage_elderly, x[1])

    inputnumberlow = "Patient No. "+str(num)+" Min Input"
    inputnumberhigh = "Patient No. "+str(num)+" Max Input"
    ax0.plot(x[0], xmemberlow, "bo")
    ax0.plot(x[1], xmemberhigh, "ro")
    ax0.text(x[0], xmemberlow, inputnumberlow, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    ax0.text(x[1], xmemberhigh, inputnumberhigh, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    num +=1

# For each input, plot the age input onto the Temperature graph and the relevant membership set
num = 1
for x in temperature:
    xmemberlow = fuzz.interp_membership(x_temp, fuzzytemp_hypo, x[0])
    xmemberhigh = fuzz.interp_membership(x_temp, fuzzytemp_hypo, x[1])
    if fuzz.interp_membership(x_temp, fuzzytemp_average, x[0]) > fuzz.interp_membership(x_temp, fuzzytemp_hypo, x[0]):
        xmemberlow = fuzz.interp_membership(x_temp, fuzzytemp_average, x[0])
    if fuzz.interp_membership(x_temp, fuzzytemp_fever, x[0]) > xmemberlow:
        xmemberlow = fuzz.interp_membership(x_temp, fuzzytemp_fever, x[0])
    if fuzz.interp_membership(x_temp, fuzzytemp_average, x[1]) > fuzz.interp_membership(x_temp, fuzzytemp_hypo, x[1]):
        xmemberhigh = fuzz.interp_membership(x_temp, fuzzytemp_average, x[1])
    if fuzz.interp_membership(x_temp, fuzzytemp_fever, x[1]) > xmemberhigh:
        xmemberhigh = fuzz.interp_membership(x_temp, fuzzytemp_fever, x[1])
    inputnumberlow = "Patient No. "+str(num)+" Min Input"
    inputnumberhigh = "Patient No. "+str(num)+" Max Input"
    ax1.plot(x[0], xmemberlow, "bo")
    ax1.plot(x[1], xmemberhigh, "ro")
    ax1.text(x[0], xmemberlow, inputnumberlow, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    ax1.text(x[1], xmemberhigh, inputnumberhigh, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    num +=1

# For each input, plot the age input onto the Headache graph and the relevant membership set
num = 1
for x in headache:
    xmemberlow = fuzz.interp_membership(x_head, fuzzyhead_norm, x[0])
    xmemberhigh = fuzz.interp_membership(x_head, fuzzyhead_norm, x[1])
    if fuzz.interp_membership(x_head, fuzzyhead_benign, x[0]) > fuzz.interp_membership(x_head, fuzzyhead_norm, x[0]):
        xmemberlow = fuzz.interp_membership(x_head, fuzzyhead_benign, x[0])
    if fuzz.interp_membership(x_head, fuzzyhead_malign, x[0]) > xmemberlow:
        xmemberlow = fuzz.interp_membership(x_head, fuzzyhead_malign, x[0])
    if fuzz.interp_membership(x_head, fuzzyhead_benign, x[1]) > fuzz.interp_membership(x_head, fuzzyhead_norm, x[1]):
        xmemberhigh = fuzz.interp_membership(x_head, fuzzyhead_benign, x[1])
    if fuzz.interp_membership(x_head, fuzzyhead_malign, x[1]) > xmemberhigh:
        xmemberhigh = fuzz.interp_membership(x_head, fuzzyhead_malign, x[1])    
    inputnumberlow = "Patient No. "+str(num)+" Min Input"
    inputnumberhigh = "Patient No. "+str(num)+" Max Input"
    ax2.plot(x[0], xmemberlow, "bo")
    ax2.plot(x[1], xmemberhigh, "ro")
    ax2.text(x[0], xmemberlow, inputnumberlow, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    ax2.text(x[1], xmemberhigh, inputnumberhigh, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    num +=1  

# Find the minimum output value from the input interval range
def interpmembershipmin(inputvar, parameter, inputrange):
    minmember = 1
    for i in np.linspace(inputrange[0], inputrange[1]+1):
        if fuzz.interp_membership(inputvar, parameter, i) < minmember:
            minmember = fuzz.interp_membership(inputvar, parameter, i)
    return minmember

# Find the minimum output value from the input interval range but do not allow for 0 membership
def interpmembershipminclause(inputvar, parameter, inputrange):
    minmember = 1
    for i in np.linspace(inputrange[0], inputrange[1]+1):
        if fuzz.interp_membership(inputvar, parameter, i) < minmember and fuzz.interp_membership(inputvar, parameter, i) != 0:
            minmember = fuzz.interp_membership(inputvar, parameter, i)
    return minmember

# Find the maximum output value from the input interval range
def interpmembershipmax(inputvar, parameter, inputrange):
    maxmember = 0
    for i in np.linspace(inputrange[0], inputrange[1]+1):
        if fuzz.interp_membership(inputvar, parameter, i) > maxmember:
            maxmember = fuzz.interp_membership(inputvar, parameter, i)
    return maxmember

# Find the maximum output membership value
def maxpossiblemembership(i):
    maximum = 0 
    if fuzz.interp_membership(x_urgency, fuzzyurg_low, i) > maximum:
        maximum = fuzz.interp_membership(x_urgency, fuzzyurg_low, i)
    if fuzz.interp_membership(x_urgency, fuzzyurg_mid, i) > maximum:
        maximum = fuzz.interp_membership(x_urgency, fuzzyurg_mid, i)
    if fuzz.interp_membership(x_urgency, fuzzyurg_high, i) > maximum:
        maximum = fuzz.interp_membership(x_urgency, fuzzyurg_high, i)
    return maximum

# Function to print all membership variables for a specified defuzzified output
def printoutput(label, linguistic, singleton):
    print("\n"+label+" Defuzzification:")
    print("Output = "+str(singleton))
    print("Linguistic Output = "+str(linguistic))
    print("Non-Urgent Membership = "+str(fuzz.interp_membership(x_urgency, fuzzyurg_low, singleton)))
    print("Semi-Urgent Membership = "+str(fuzz.interp_membership(x_urgency, fuzzyurg_mid, singleton)))
    print("Urgent Membership = "+str(fuzz.interp_membership(x_urgency, fuzzyurg_high, singleton)))

# Function to defuzzify an output, plot it on its respective graph, and print the output result details     
def defuzz(defuzztypelow, defuzztypehigh, defuzzname, graph):
    defuzzaggregate = []
    defuzzsingleton = defuzztypelow
    if defuzztypelow != defuzztypehigh:
        for i in range(0, 101):
            if i < defuzztypelow or i > defuzztypehigh:
                defuzzaggregate.append(0)
            else:
                defuzzaggregate.append(maxpossiblemembership(i))
        defuzzaggregate = np.fmin(defuzzaggregate,defuzzaggregate) # Convert to correct type
        defuzzsingleton = fuzz.defuzz(x_urgency, defuzzaggregate, 'centroid')
    
    outputmember = fuzz.interp_membership(x_urgency, fuzzyurg_high, defuzzsingleton)
    outputlabel = defuzzname+": "+inputnumbe
    defuzzlinguistic = 'Urgent'
    if fuzz.interp_membership(x_urgency, fuzzyurg_mid, defuzzsingleton) > outputmember:
        outputmember = fuzz.interp_membership(x_urgency, fuzzyurg_mid, defuzzsingleton)
        defuzzlinguistic = 'Semi-Urgent'
    if fuzz.interp_membership(x_urgency, fuzzyurg_low, defuzzsingleton) > outputmember:
        outputmember = fuzz.interp_membership(x_urgency, fuzzyurg_low, defuzzsingleton)
        defuzzlinguistic = 'Non-Urgent'
    graph.plot(defuzzsingleton, outputmember, 'ro', linewidth=1.5, alpha=0.9)
    graph.text(defuzzsingleton, outputmember, outputlabel, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    printoutput(defuzzname, defuzzlinguistic, defuzzsingleton)

# Function to plot the input/output sets onto the graph
def plotting(axis, x_member, fuzzy_features, labels, colours, title):
    for fuzzy_feature, label, color in zip(fuzzy_features, labels, colours):
        axis.plot(x_member, fuzzy_feature, color, linewidth=1.5, label=label)
    axis.set_title(title)
    axis.legend()

# Function to calculate the TSK output value
def calculate_tsk_output(firing_strengths, input_variables, rule_coefficients):
    weighted_sum, firing_strength_sum = 0, 0

    for rule_name, firing_strength in firing_strengths.items():
        if firing_strength > 0:
            coeffs = rule_coefficients[rule_name]
            rule_output = coeffs['p_temp'] * input_variables['temperature'] + \
                            coeffs.get('p_head', 0) * input_variables.get('headache', 0) + \
                            coeffs.get('p_age', 0) * input_variables.get('age', 0) + \
                            coeffs['r']
            weighted_sum += firing_strength * rule_output
            firing_strength_sum += firing_strength

            if firing_strength_sum > 0:
                tsk_output = weighted_sum / firing_strength_sum
                return max(0, min(tsk_output, 100))
            else:
                return 0

# Loop to iterate through all inputs, and determine what the defuzzified output should be
num = 1
for y in age:
    temperaturetmp = temperature
    for t in temperaturetmp:
        headtmp = headache
        for h in headtmp:
            
            #Establish the Inputs Membership value into all input sets - While finding the lowest and highest possible outcome memberships
            inputnumbe = "Patient "+str(num)
            agechildmemberlow = interpmembershipmin(x_age, fuzzyage_child, y)
            ageadultmemberlow = interpmembershipmax(x_age, fuzzyage_adult, y)
            ageeldermemberlow = interpmembershipmin(x_age, fuzzyage_elderly, y)
            if ageadultmemberlow == 0 and agechildmemberlow==0 and ageeldermemberlow==0:
                agechildmemberlow = interpmembershipminclause(x_age, fuzzyage_child, y)
                ageeldermemberlow = interpmembershipminclause(x_age, fuzzyage_elderly, y)
            agechildmemberhigh = interpmembershipmax(x_age, fuzzyage_child, y)
            ageadultmemberhigh = interpmembershipmin(x_age, fuzzyage_adult, y)
            ageeldermemberhigh = interpmembershipmax(x_age, fuzzyage_elderly, y)
            if agechildmemberhigh == 0 and ageadultmemberhigh == 0 and ageeldermemberhigh == 0:
                ageadultmemberhigh = interpmembershipminclause(x_age, fuzzyage_adult, y)
            
            temphypomemberlow = interpmembershipmin(x_temp, fuzzytemp_hypo, t)
            tempavgmemberlow = interpmembershipmax(x_temp, fuzzytemp_average, t)
            tempfevmemberlow = interpmembershipmin(x_temp, fuzzytemp_fever, t)
            if temphypomemberlow == 0 and tempavgmemberlow == 0 and tempfevmemberlow == 0:
                temphypomemberlow = interpmembershipminclause(x_temp, fuzzytemp_hypo, t)
                tempfevmemberlow = interpmembershipminclause(x_temp, fuzzytemp_fever, t)
            temphypomemberhigh = interpmembershipmax(x_temp, fuzzytemp_hypo, t)
            tempavgmemberhigh = interpmembershipmin(x_temp, fuzzytemp_average, t)
            tempfevmemberhigh = interpmembershipmax(x_temp, fuzzytemp_fever, t)
            if temphypomemberhigh == 0 and tempavgmemberhigh == 0 and tempfevmemberhigh == 0:
                tempavgmemberhigh = interpmembershipminclause(x_temp, fuzzytemp_average, t)
            
            headnormmemberlow = interpmembershipmax(x_head, fuzzyhead_norm, h)
            headbenignmemberlow = interpmembershipmin(x_head, fuzzyhead_benign, h)
            headmalignmemberlow = interpmembershipmin(x_head, fuzzyhead_malign, h)
            if headnormmemberlow == 0 and headbenignmemberlow == 0 and headmalignmemberlow == 0:
                headbenignmemberlow = interpmembershipminclause(x_head, fuzzyhead_benign, h)
                if headbenignmemberlow == 0:
                    headmalignmemberlow = interpmembershipminclause(x_head, fuzzyhead_malign, h)
            headnormmemberhigh = interpmembershipmin(x_head, fuzzyhead_norm, h)
            headbenignmemberhigh = interpmembershipmin(x_head, fuzzyhead_benign, h)
            headmalignmemberhigh = interpmembershipmax(x_head, fuzzyhead_malign, h)
            if headnormmemberhigh == 0 and headbenignmemberhigh == 0 and headmalignmemberhigh == 0:
                headbenignmemberhigh = interpmembershipminclause(x_head, fuzzyhead_benign, h)
                if headnormmemberhigh == 0 and headbenignmemberhigh == 0 and headmalignmemberhigh == 0:
                    headnormmemberhigh = interpmembershipminclause(x_head, fuzzyhead_norm, h)

            #Rule Set Declaration
            
            # URGENT RULES
            urgentoutputlow = []
            urgentoutputhigh = []
            rule1low = max(temphypomemberlow, headmalignmemberlow) # IF Temperature is HYPOTHERMIC OR Headache is MALIGN THEN Urgency is URGENT
            rule1high = max(temphypomemberhigh, headmalignmemberhigh)  # IF Temperature is HYPOTHERMIC OR Headache is MALIGN THEN Urgency is URGENT
            rule6low = min(headbenignmemberlow, tempfevmemberlow, max(agechildmemberlow, ageeldermemberlow)) # IF Age is NOT ADULT AND Headache is BENIGN AND Temperature is FEVER THEN Urgency is URGENT
            rule6high = min(headbenignmemberhigh, tempfevmemberhigh, max(agechildmemberhigh, ageeldermemberhigh)) # IF Age is NOT ADULT AND Headache is BENIGN AND Temperature is FEVER THEN Urgency is URGENT
            urgentoutputlow.append(rule1low)
            urgentoutputlow.append(rule6low)
            urgentoutputhigh.append(rule1high)
            urgentoutputhigh.append(rule6high)
            
            #Loop to find the lowest firing strength for URGENT
            urgentusedlow = 0
            urgentoutputmaxlow = 0
            if len(urgentoutputlow) > 0:
                urgentoutputmaxlow = max(urgentoutputlow)
                if urgentoutputmaxlow > 0:
                    urgentusedlow = 1
                    
            #Loop to find the highest firing strength for URGENT        
            urgentusedhigh = 0
            urgentoutputmaxhigh = 0
            if len(urgentoutputhigh) > 0:
                urgentoutputmaxhigh = max(urgentoutputhigh)
                if urgentoutputmaxhigh > 0:
                    urgentusedhigh = 1
            
            # NON-URGENT RULES 
            nonurgentoutputlow = []
            nonurgentoutputhigh = []
            rule2low = min(tempavgmemberlow, headnormmemberlow) # IF Temperature is AVERAGE AND Headache is NORMAL THEN Urgency is NON-URGENT
            rule2high = min(tempavgmemberhigh, headnormmemberhigh) # IF Temperature is AVERAGE AND Headache is NORMAL THEN Urgency is NON-URGENT
            nonurgentoutputlow.append(rule2low)
            nonurgentoutputhigh.append(rule2high)

            rule5low = min(ageadultmemberlow, tempavgmemberlow, headbenignmemberlow) # IF Age is ADULT AND Temperature is AVERAGE and Headache is BENIGN THEN Urgency is NON-URGENT
            rule5high = min(ageadultmemberhigh, tempavgmemberhigh, headbenignmemberhigh) # IF Age is ADULT AND Temperature is AVERAGE and Headache is BENIGN THEN Urgency is NON-URGENT
            nonurgentoutputlow.append(rule5low)
            nonurgentoutputhigh.append(rule5high)
            
            #Loop to find the lowest firing strength for NON-URGENT
            nonurgentusedlow = 0
            nonurgentoutputmaxlow = 0
            if len(nonurgentoutputlow) > 0:
                nonurgentoutputmaxlow = max(nonurgentoutputlow)
                if nonurgentoutputmaxlow > 0:
                    nonurgentusedlow = 1
            
            #Loop to find the highest firing strength for NON-URGENT
            nonurgentusedhigh = 0
            nonurgentoutputmaxhigh = 0
            if len(nonurgentoutputhigh) > 0:
                nonurgentoutputmaxhigh = max(nonurgentoutputhigh)
                if nonurgentoutputmaxhigh > 0:
                    nonurgentusedhigh = 1
    
            # SEMI-URGENT RULES
            semiurgentoutputlow = []
            semiurgentoutputhigh = []
            rule3low = min(tempfevmemberlow, headnormmemberlow) # IF Temperature is FEVER AND Headache is NORMAL THEN Urgency is SEMI-URGENT
            rule3high = min(tempfevmemberhigh, headnormmemberhigh) # IF Temperature is FEVER AND Headache is NORMAL THEN Urgency is SEMI-URGENT
            rule4low = min(max(agechildmemberlow, ageeldermemberlow), tempavgmemberlow, headbenignmemberlow) # IF Age is NOT ADULT AND Temperature is AVERAGE and Headache is BENIGN THEN Urgency is SEMI-URGENT
            rule4high = min(max(agechildmemberhigh, ageeldermemberhigh), tempavgmemberhigh, headbenignmemberhigh) # IF Age is NOT ADULT AND Temperature is AVERAGE and Headache is BENIGN THEN Urgency is SEMI-URGENT
            rule7low = min(ageadultmemberlow, tempfevmemberlow, headbenignmemberlow) # IF Age is ADULT AND Temperature is FEVER AND Headache is BENIGN THEN Urgency is SEMI-URGENT
            rule7high = min(ageadultmemberhigh, tempfevmemberhigh, headbenignmemberhigh) # IF Age is ADULT AND Temperature is FEVER AND Headache is BENIGN THEN Urgency is SEMI-URGENT
            semiurgentoutputlow.append(rule3low)
            semiurgentoutputlow.append(rule4low)
            semiurgentoutputlow.append(rule7low)
            semiurgentoutputhigh.append(rule3high)
            semiurgentoutputhigh.append(rule4high)
            semiurgentoutputhigh.append(rule7high)
            
            #Loop to find the lowest firing strength for NON-URGENT
            semiurgentusedlow = 0
            semiurgentoutputmaxlow = 0
            if len(semiurgentoutputlow) > 0:
                semiurgentoutputmaxlow = max(semiurgentoutputlow)
                if semiurgentoutputmaxlow > 0:
                    semiurgentusedlow = 1
                    
            #Loop to find the highest firing strength for NON-URGENT
            semiurgentusedhigh = 0
            semiurgentoutputmaxhigh = 0
            if len(semiurgentoutputhigh) > 0:
                semiurgentoutputmaxhigh = max(semiurgentoutputhigh)
                if semiurgentoutputmaxhigh > 0:
                    semiurgentusedhigh = 1
            
            
            #Zero Order TSK
            # Urgent rules
            rule1tsklow = rule1low * 90
            rule1tskhigh = rule1high * 90
            rule6tsklow = rule6low * 90
            rule6tskhigh = rule6high * 90
            # Non-Urgent rules
            rule2tsklow = rule2low * 10
            rule2tskhigh = rule2high * 10
            rule5tsklow = rule5low * 10
            rule5tskhigh = rule5high * 10
            # Semi-Urgent rules
            rule3tsklow = rule3low * 50
            rule3tskhigh = rule3high * 50
            rule4tsklow = rule4low * 50
            rule4tskhigh = rule4high * 50
            rule7tsklow = rule7low * 50
            rule7tskhigh = rule7high * 50

            #First Order TSK 
            
            # Define input variables for high and low values
            input_variables_high = {
                'age': y[1],        # Crisp age
                'temperature': t[1], # Crisp temperature
                'headache': h[1]     # Crisp headache level
            }

            input_variables_low = {
                'age': y[0],        # Crisp age
                'temperature': t[0], # Crisp temperature
                'headache': h[0]     # Crisp headache level
            }

            rule_coefficients = {
            # Urgent
            'rule1': {'p_temp': 1, 'p_head': 1, 'r': 90},   # High fever or severe headache indicates high urgency
            'rule6': {'p_head': 1, 'p_temp': 1, 'p_age': 1, 'r': 90},  # Severe symptoms in a child or elderly are very urgent

            # Non-Urgent
            'rule2': {'p_temp': 0.3, 'p_head': 0.2, 'r': 10},    # Mild symptoms suggest low urgency
            'rule5': {'p_age': 0.2, 'p_temp': 0.3, 'p_head': 0.2, 'r': 10},  # Mild symptoms in an adult

            # Semi-Urgent
            'rule3': {'p_temp': 0.5, 'p_head': 0.4, 'r': 30},   # Fever with normal headache, moderately urgent
            'rule4': {'p_age': 0.3, 'p_temp': 0.4, 'p_head': 0.3, 'r': 10},  # Moderate symptoms in a child or elderly
            'rule7': {'p_age': 0.2, 'p_temp': 0.5, 'p_head': 0.3, 'r': 10},   # Fever and headache in an adult
            }

            firing_strengths_high = {
            'rule1': rule1high,  
            'rule2': rule2high,
            'rule3': rule3high,
            'rule4': rule4high,
            'rule5': rule5high,
            'rule6': rule6high,
            'rule7': rule7high,
            }

            firing_strengths_low = {
            'rule1': rule1low,
            'rule2': rule2low,
            'rule3': rule3low,
            'rule4': rule4low,
            'rule5': rule5low,
            'rule6': rule6low,
            'rule7': rule7low
            }

            # TSK FIRST ORDER OUTPUT
            firstorderoutput_low = calculate_tsk_output(firing_strengths_low, input_variables_low, rule_coefficients)
            firstorderoutput_high = calculate_tsk_output(firing_strengths_high, input_variables_high, rule_coefficients)

            #Output Membership/Defuzz methods - What is the maximum and minimum firing strength for each membership function
            outputnonurgentlow = np.fmin(nonurgentoutputmaxlow, fuzzyurg_low)
            outputnonurgenthigh = np.fmin(nonurgentoutputmaxhigh, fuzzyurg_low)
            outputsemiurgentlow = np.fmin(semiurgentoutputmaxlow, fuzzyurg_mid)
            outputsemiurgenthigh = np.fmin(semiurgentoutputmaxhigh, fuzzyurg_mid)
            outputurgentlow = np.fmin(urgentoutputmaxlow, fuzzyurg_high)
            outputurgenthigh = np.fmin(urgentoutputmaxhigh, fuzzyurg_high)
            
            #Create a new set based on the min and max rules we have created, and their firing strength
            aggregatedlow = np.fmax(outputnonurgentlow, np.fmax(outputsemiurgentlow, outputurgentlow))  
            aggregatedhigh = np.fmax(outputnonurgenthigh, np.fmax(outputsemiurgenthigh, outputurgenthigh))  
            
            #Defuzzify our new set into a highest and lowest numeric output based on one of the following methods
            centroidlow = fuzz.defuzz(x_urgency, aggregatedlow, 'centroid')
            centroidhigh = fuzz.defuzz(x_urgency, aggregatedhigh, 'centroid')
            
            bisectorlow = fuzz.defuzz(x_urgency, aggregatedlow, 'bisector')
            bisectorhigh = fuzz.defuzz(x_urgency, aggregatedhigh, 'bisector')
            
            meanofmaximalow = fuzz.defuzz(x_urgency, aggregatedlow, 'mom')
            meanofmaximahigh = fuzz.defuzz(x_urgency, aggregatedhigh, 'mom')
            
            minofmaximalow = fuzz.defuzz(x_urgency, aggregatedlow, 'som')
            minofmaximahigh = fuzz.defuzz(x_urgency, aggregatedhigh, 'som')
            
            maxofmaximalow = fuzz.defuzz(x_urgency, aggregatedlow, 'lom')
            maxofmaximahigh = fuzz.defuzz(x_urgency, aggregatedhigh, 'lom')
            
            zeroorderoutputlow = (rule1tsklow + rule6tsklow + rule2tsklow + rule5tsklow + rule3tsklow + rule4tsklow + rule7tsklow) / (rule1low + rule6low + rule2low + rule5low + rule3low + rule4low + rule7low)
            zeroorderoutputhigh = (rule1tskhigh + rule6tskhigh + rule2tskhigh + rule5tskhigh + rule3tskhigh + rule4tskhigh + rule7tskhigh) / (rule1high + rule6high + rule2high + rule5high + rule3high + rule4high + rule7high)
            
            #Print Patient Data and Input set membership values
            print("\nPatient: "+str(num))
            print("Age = "+str(y)+", Temperature = "+str(t)+", Headache Severity = "+str(h))
            print("\nInput Memberships (Lowest Interval : Highest Interval): \n")
            print('Age memberships:')
            print("Child Membership = "+str(agechildmemberlow)+" : "+str(agechildmemberhigh)+", Adult Membership = "+str(ageadultmemberlow)+" : "+str(ageadultmemberhigh)+", Elderly Membership = "+str(ageeldermemberlow)+" : "+str(ageeldermemberhigh))
            print("\nTemperature Memberships:")
            print("Hypothermic Membership = "+str(temphypomemberlow)+" : "+str(temphypomemberhigh)+", Average Membership = "+str(tempavgmemberlow)+" : "+str(tempavgmemberhigh)+", Fever Membership = "+str(tempfevmemberlow)+" : "+str(tempfevmemberlow))
            print("\nHeadache Memberships:")
            print("Normal Membership = "+str(headnormmemberlow)+" : "+str(headnormmemberhigh)+", Benign Membership = "+str(headbenignmemberlow)+" : "+str(headbenignmemberlow)+", Malign Membership = "+str(headmalignmemberlow)+" : "+str(headmalignmemberhigh))
            
            #Plot Centroid Output and Print data relating to the plot
            defuzz(centroidlow, centroidhigh, 'Centroid', ax3)
            
            #If the user did not select to only show Centroid (The Recommended Defuzzifier), show all possible outputs and their details
            if graphreductor.lower() != "y":
                #Plot Bisector Output and Print data relating to the plot
                defuzz(bisectorlow, bisectorhigh, 'Bisector', ax3)
                
                #Plot Mean of Maxima Output and Print data relating to the plot
                defuzz(meanofmaximalow, meanofmaximahigh, 'Mean of Maxima', ax3)
                
                #Plot Min of Maxima Output and Print data relating to the plot
                defuzz(minofmaximalow, minofmaximahigh, 'Min of Maxima', ax3)
                
                #Plot Max of Maxima Output and Print data relating to the plot
                defuzz(maxofmaximalow, maxofmaximahigh, 'Max of Maxima', ax3)
            
            #Plot Zero Order Output and Print data relating to the plot
            defuzz(zeroorderoutputlow, zeroorderoutputhigh, 'Zero Order TSK', ax4)
            
            #Plot First Order Output and Print data relating to the plot
            defuzz(firstorderoutput_low, firstorderoutput_high, 'First Order TSK', ax4)
            
            print("\n")    
            
            #Continue Looping for all remaining inputs (if any)
            headtmp.remove(h)
            num+=1
            break
        temperaturetmp.remove(t)
        break
    
#Plot all input sets and output sets onto their respective graphs
plotting(ax0, x_age, [fuzzyage_child, fuzzyage_adult, fuzzyage_elderly], ['Child', 'Adult', 'Elderly'], ['r', 'g', 'b'], 'Age')

plotting(ax1, x_temp,[fuzzytemp_hypo, fuzzytemp_average, fuzzytemp_fever],['Hypothermic', 'Average', 'Fever'],['r', 'g', 'b'],'Temperature')

plotting(ax2, x_head,[fuzzyhead_norm, fuzzyhead_benign, fuzzyhead_malign],['Normal', 'Benign', 'Malign'],['r', 'g', 'b'],'Headache')

plotting(ax3, x_urgency,[fuzzyurg_low, fuzzyurg_mid, fuzzyurg_high],['Non-Urgent', 'Semi-Urgent', 'Urgent'],['r', 'g', 'b'],'Mamdani Inference - Urgency')

plotting(ax4, x_urgency,[fuzzyurg_low, fuzzyurg_mid, fuzzyurg_high],['Non-Urgent', 'Semi-Urgent', 'Urgent'],['r', 'g', 'b'],'TSK Inference - Urgency')

plt.tight_layout()
plt.show()