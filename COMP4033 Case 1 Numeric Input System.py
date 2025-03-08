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
             ageinput = float(input("Please enter the patient's Age: "))
             tempinput = float(input("Please enter the patient's temperature: "))
             headinput = float(input("Please enter the patient's headache severity: "))
         except ValueError:
             print("Please Provide a Numerical Input!")
             continue
         if ageinput < 0 or ageinput > 130:
             print("Please Enter a Valid Age! (0-130)")
             continue
         if tempinput < 0 or tempinput > 100:
             print("Please Enter a Valid Temperature! (0-100)")
             continue
         if headinput < 0 or headinput > 10:
             print("Please Enter a Valid Headache Severity! (0-10)")
             continue
         age.append(ageinput)
         temperature.append(tempinput)
         headache.append(headinput)
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


# Function to print all membership variables for a specified defuzzified output
def printoutput(label, linguistic, singleton):
    print("\n"+label+" Defuzzification:")
    print("Output = "+str(singleton))
    print("Linguistic Output = "+str(linguistic))
    print("Non-Urgent Membership = "+str(fuzz.interp_membership(x_urgency, fuzzyurg_low, singleton)))
    print("Semi-Urgent Membership = "+str(fuzz.interp_membership(x_urgency, fuzzyurg_mid, singleton)))
    print("Urgent Membership = "+str(fuzz.interp_membership(x_urgency, fuzzyurg_high, singleton)))

# Function to defuzzify an output, plot it on its respective graph, and print the output result details 
def defuzz(defuzztype, defuzzname, graph):
    outputmember = fuzz.interp_membership(x_urgency, fuzzyurg_high, defuzztype)
    defuzzlinguistic = 'Urgent'
    if fuzz.interp_membership(x_urgency, fuzzyurg_mid, defuzztype) > outputmember:
        outputmember = fuzz.interp_membership(x_urgency, fuzzyurg_mid, defuzztype)
        defuzzlinguistic = 'Semi-Urgent'
    if fuzz.interp_membership(x_urgency, fuzzyurg_low, defuzztype) > outputmember:
        outputmember = fuzz.interp_membership(x_urgency, fuzzyurg_low, defuzztype)
        defuzzlinguistic = 'Non-Urgent'
    outputlabel = defuzzname+": "+inputnumber
    graph.plot(defuzztype, outputmember, 'ro', linewidth=1.5, alpha=0.9)
    graph.text(defuzztype, outputmember, outputlabel, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    printoutput(defuzzname, defuzzlinguistic, defuzztype)

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

# For each input, plot the age input onto the Age graph and the relevant membership set
num = 1
for x in age:
    xmember = fuzz.interp_membership(x_age, fuzzyage_child, x)
    if fuzz.interp_membership(x_age, fuzzyage_adult, x) > fuzz.interp_membership(x_age, fuzzyage_child, x):
        xmember = fuzz.interp_membership(x_age, fuzzyage_adult, x)
    if fuzz.interp_membership(x_age, fuzzyage_elderly, x) > xmember:
        xmember = fuzz.interp_membership(x_age, fuzzyage_elderly, x)

    inputnumber = "Patient No. "+str(num)
    ax0.plot(x, xmember, "ro")
    ax0.text(x, xmember, inputnumber, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    num +=1

# For each input, plot the age input onto the Temperature graph and the relevant membership set
num = 1
for x in temperature:
    xmember = fuzz.interp_membership(x_temp, fuzzytemp_hypo, x)
    if fuzz.interp_membership(x_temp, fuzzytemp_average, x) > fuzz.interp_membership(x_temp, fuzzytemp_hypo, x):
        xmember = fuzz.interp_membership(x_temp, fuzzytemp_average, x)
    if fuzz.interp_membership(x_temp, fuzzytemp_fever, x) > xmember:
        xmember = fuzz.interp_membership(x_temp, fuzzytemp_fever, x)
    inputnumber = "Patient No. "+str(num)
    ax1.plot(x, xmember, "ro")
    ax1.text(x, xmember, inputnumber, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    num +=1

# For each input, plot the age input onto the Headache graph and the relevant membership set
num = 1
for x in headache:
    xmember = fuzz.interp_membership(x_head, fuzzyhead_norm, x)
    if fuzz.interp_membership(x_head, fuzzyhead_benign, x) > fuzz.interp_membership(x_head, fuzzyhead_norm, x):
        xmember = fuzz.interp_membership(x_head, fuzzyhead_benign, x)
    if fuzz.interp_membership(x_head, fuzzyhead_malign, x) > xmember:
        xmember = fuzz.interp_membership(x_head, fuzzyhead_malign, x)
    inputnumber = "Patient No. "+str(num)
    ax2.plot(x, xmember, "ro")
    ax2.text(x, xmember, inputnumber, horizontalalignment="left", verticalalignment = "bottom", fontsize = 8)
    num +=1  

# Loop to iterate through all inputs, and determine what the defuzzified output should be
num = 1
for y in age:
    temperaturetmp = temperature
    for t in temperaturetmp:
        headtmp = headache
        for h in headtmp:
            inputnumbe = "Patient "+str(num)
            
            #Establish the Inputs Membership value into all input sets
            agechildmember = fuzz.interp_membership(x_age, fuzzyage_child, y)
            ageadultmember = fuzz.interp_membership(x_age, fuzzyage_adult, y)
            ageeldermember = fuzz.interp_membership(x_age, fuzzyage_elderly, y)
            
            temphypomember = fuzz.interp_membership(x_temp, fuzzytemp_hypo, t)
            tempavgmember = fuzz.interp_membership(x_temp, fuzzytemp_average, t)
            tempfevmember = fuzz.interp_membership(x_temp, fuzzytemp_fever, t)
            
            headnormmember = fuzz.interp_membership(x_head, fuzzyhead_norm, h)
            headbenignmember = fuzz.interp_membership(x_head, fuzzyhead_benign, h)
            headmalignmember = fuzz.interp_membership(x_head, fuzzyhead_malign, h)

            #Rule Set Declaration
    
            # URGENT RULES
            urgentoutput = []  
            rule1 = max(temphypomember, headmalignmember) # IF Temperature is HYPOTHERMIC OR Headache is MALIGN THEN Urgency is URGENT
            rule6 = min(headbenignmember, tempfevmember, max(agechildmember, ageeldermember)) # IF Age is NOT ADULT AND Headache is BENIGN AND Temperature is FEVER THEN Urgency is URGENT
            urgentoutput.append(rule1)
            urgentoutput.append(rule6)
            
            #Loop to find the highest firing strength for URGENT
            urgentused = 0
            urgentoutputmax = 0
            if len(urgentoutput) > 0:
                urgentoutputmax = max(urgentoutput)
                if urgentoutputmax > 0:
                    urgentused = 1
            
            # NON-URGENT RULES
            nonurgentoutput = []
            rule2 = min(tempavgmember, headnormmember) # IF Temperature is AVERAGE AND Headache is NORMAL THEN Urgency is NON-URGENT
            nonurgentoutput.append(rule2)

            rule5 = min(ageadultmember, tempavgmember, headbenignmember) # IF Age is ADULT AND Temperature is AVERAGE and Headache is BENIGN THEN Urgency is NON-URGENT
            nonurgentoutput.append(rule5)
            
            #Loop to find the highest firing strength for NON-URGENT
            nonurgentused = 0
            nonurgentoutputmax = 0
            if len(nonurgentoutput) > 0:
                nonurgentoutputmax = max(nonurgentoutput)
                if nonurgentoutputmax > 0:
                    nonurgentused = 1
    
            # SEMI-URGENT RULES
            semiurgentoutput = []
            rule3 = min(tempfevmember, headnormmember) # IF Temperature is FEVER AND Headache is NORMAL THEN Urgency is SEMI-URGENT
            rule4 = min(max(agechildmember, ageeldermember), tempavgmember, headbenignmember) # IF Age is NOT ADULT AND Temperature is AVERAGE and Headache is BENIGN THEN Urgency is SEMI-URGENT
            rule7 = min(ageadultmember, tempfevmember, headbenignmember) # IF Age is ADULT AND Temperature is FEVER AND Headache is BENIGN THEN Urgency is SEMI-URGENT
            semiurgentoutput.append(rule3)
            semiurgentoutput.append(rule4)
            semiurgentoutput.append(rule7)
            
            #Loop to find the highest firing strength for NON-URGENT
            semiurgentused = 0
            semiurgentoutputmax = 0
            if len(semiurgentoutput) > 0:
                semiurgentoutputmax = max(semiurgentoutput)
                if semiurgentoutputmax > 0:
                    semiurgentused = 1
            
            
            #Zero Order TSK 
            # Urgent Rules
            rule1tsk = rule1 * 90
            rule6tsk = rule6 * 90
            # Non-urgent Rules
            rule2tsk = rule2 * 10
            rule5tsk = rule5 * 10
            # Semi-urgent Rules
            rule3tsk = rule3 * 50
            rule4tsk = rule4 * 50
            rule7tsk = rule7 * 50

            #First Order TSK 
            input_variables = {
                'age': y,        # Crisp age
                'temperature': t, # Crisp temperature
                'headache': h    # Crisp headache level
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

            firing_strengths = {
            'rule1': rule1,  
            'rule2': rule2,
            'rule3': rule3,
            'rule4': rule4,
            'rule5': rule5,
            'rule6': rule6,
            'rule7': rule7,
            }

            # TSK FIRST ORDER OUTPUT
            firstorderoutput= calculate_tsk_output(firing_strengths, input_variables, rule_coefficients)
                
            #Output Membership/Defuzz methods - What is the maximum firing strength for each membership function
            outputnonurgent = np.fmin(nonurgentoutputmax, fuzzyurg_low)
            outputsemiurgent = np.fmin(semiurgentoutputmax, fuzzyurg_mid)
            outputurgent = np.fmin(urgentoutputmax, fuzzyurg_high)
            
            #Create a new set based on the rules we have created, and their firing strength
            aggregated = np.fmax(outputnonurgent, np.fmax(outputsemiurgent, outputurgent))  
            
            #Defuzzify our new set into a numeric output based on one of the following methods
            centroid = fuzz.defuzz(x_urgency, aggregated, 'centroid')
            
            bisector = fuzz.defuzz(x_urgency, aggregated, 'bisector')
            
            meanofmaxima = fuzz.defuzz(x_urgency, aggregated, 'mom')
            
            minofmaxima = fuzz.defuzz(x_urgency, aggregated, 'som')
            
            maxofmaxima = fuzz.defuzz(x_urgency, aggregated, 'lom')
            
            zeroorderoutput = (rule1tsk + rule6tsk + rule2tsk + rule5tsk + rule3tsk + rule4tsk + rule7tsk) / (rule1 + rule6 + rule2 + rule5 + rule3 + rule4 + rule7)     
            
            #Print Patient Data and Input set membership values
            print("\nPatient: "+str(num))
            print("Age = "+str(y)+", Temperature = "+str(t)+", Headache Severity = "+str(h))
            print("\nInput Memberships: \n")
            print('Age memberships:')
            print("Child Membership = "+str(agechildmember)+", Adult Membership = "+str(ageadultmember)+", Elderly Membership = "+str(ageeldermember))
            print("\nTemperature Memberships:")
            print("Hypothermic Membership = "+str(temphypomember)+", Average Membership = "+str(tempavgmember)+", Fever Membership = "+str(tempfevmember))
            print("\nHeadache Memberships:")
            print("Normal Membership = "+str(headnormmember)+", Benign Membership = "+str(headbenignmember)+", Malign Membership = "+str(headmalignmember))
            print("\nOutput Memberships:")
            
            #Plot Centroid Output and Print data relating to the plot
            defuzz(centroid, 'Centroid', ax3)
            
            #If the user did not select to only show Centroid (The Recommended Defuzzifier), show all possible outputs and their details
            if graphreductor.lower() != "y":
                #Plot Bisector Output and Print data relating to the plot
                defuzz(bisector, 'Bisector', ax3)
                
                #Plot Mean of Maxima Output and Print data relating to the plot
                defuzz(meanofmaxima, 'Mean of Maxima', ax3)
                
                #Plot Min of Maxima Output and Print data relating to the plot
                defuzz(minofmaxima, 'Min of Maxima', ax3)
                
                #Plot Max of Maxima Output and Print data relating to the plot
                defuzz(maxofmaxima, 'Max of Maxima', ax3)
                
            #Plot Zero Order TSK Output and Print data relating to the plot
            defuzz(zeroorderoutput, 'Zero Order TSK', ax4)
                
            #Plot First Order TSK Output and Print data relating to the plot
            defuzz(firstorderoutput, 'First Order TSK', ax4)
            
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