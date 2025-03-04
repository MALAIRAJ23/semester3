data=[
      ['sunny','hot','high','false','no'],['sunny','hot','high','true','no'],['overcast','hot','high','false','yes'],
      ['rainy','mild','high','false','yes'],['rainy','cool','normal','false','yes'],['rainy','cool','normal','true','no'],
      ['overcast','cool','normal','true','yes'],['sunny','mild','high','false','no'],['sunny','cool','normal','false','yes'],
      ['rainy','mild','normal','false','yes'],['sunny','mild','normal','true','yes'],['overcast','mild','high','true','yes'],
      ['overcast','hot','normal','false','yes'],['rainy','mild','high','true','no'] 
 ]  #given data 
ip_eg=['sunny','cool','normal','true'] #input data 
op_eg="no" #output data 
ycount=sum(1 for record in data if record[4]=="yes") #count of yes for getting probability
ncount=sum(1 for record in data if record[4]=="no") #countof no for getting probability
tot=len(data) #total number of the rows 
prob_y=ycount/tot  #probability of yes
prob_n=ncount/tot  #probability of no
def likelihood(index_f,value_f,class_d): #function to calculate likelihood
 class_count=sum(1 for record in data if record[index_f]==value_f and record[4]==class_d) #basic for likelihood it takes the index of the input data and checks for yes and no counts
 t_class_count=ycount if class_d=="yes" else ncount #to get total class count
 return class_count/t_class_count if t_class_count>0 else 0 #only if total count is greater than 0 take into account
prob_class_y=1 #assign prob of class y as 1
prob_class_n=1 #assign prob of class n as 1
for i in range(len(ip_eg)): 
 prob_class_y*=likelihood(i,ip_eg[i],"yes") #calculating likelihood for yes in input
 prob_class_n*=likelihood(i,ip_eg[i],"no") #calculating likelihood for no in input
prediction="yes" if prob_class_y>prob_class_n else "no" #predicting output based on the greatest value
print("prediction:",prediction) 
if prediction!=op_eg: 
 print("risk:",max(prob_class_y,prob_class_n)) #if prediction not equal to output take the maximum of prior as risk
else: 
 print("risk:",0) #else there is no risk