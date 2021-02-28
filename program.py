input_file = open("sample_input.txt","r") # Reading the Input File
output_File=open("sample_output.txt","w+") # Creating/Writing the Output File

lines=input_file.readlines() # Reading all lines

noOfEmployees=0
count=1 #Count of line number read

d=dict()
for line in lines:
    if(count==1):
        noOfEmployees=int(line[len(line)-2]) # Storing  the no. of employees
    if(count>=5):
        d.update({line.split(":")[0]: (int)(line.split(":")[1])}) #Updating the dictionary
    count+=1

d={k: v for k, v in sorted(d.items(), key=lambda item: item[1])} #Sorting the dictionary based on values
vals=list(d.values()) # Values if Dictionary
keys=list(d.keys())# Keys if Dictionary

index=0 # Assuming first index to by min Index 
myMin=vals[noOfEmployees-1]-vals[0] # Assuming first index to (first index + noOFEmployees) as min difference

for i in range(1,len(vals)-noOfEmployees):
    if(vals[i+noOfEmployees-1]-vals[i]<myMin):
        index=i # Actual index
        myMin=vals[i+noOfEmployees-1]-vals[i] # Actual min difference

initStr="The goodies selected for distribution are:\n\n"
output_File.write(initStr)

for j in range(index,index+noOfEmployees):
    output_File.write(str(keys[j])+": "+str(vals[j])+"\n") # Output of each item into the output file

output_File.write("\n")
output_File.write("And the difference between the chosen goodie with highest price and the lowest price is "+str(myMin))

output_File.close() #Closing output file
input_file.close() #Closing input file