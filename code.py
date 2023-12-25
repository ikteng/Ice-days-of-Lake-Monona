import csv
import sys
import matplotlib.pyplot as plt
import numpy as np

# help extract the data from the downloaded csv
# def create_csv():
#     #sys.argv[1] #first argument as string
#     #opening the csv file to write
#     with open('downloaded_data.csv','r', encoding='utf-8-sig') as read, open('data.csv','w',newline='') as write:
#         #read file
#         reader = csv.DictReader(read, delimiter=',')
#         #create writer object
#         writer=csv.writer(write)

#         headers=reader.fieldnames
#         print(headers)

#         #write the header
#         writer.writerow(['year','days'])

#         #spliting into 2 columns
#         for row in reader:
#             #print(row)
#             x=row['Category'].split('-')[0]
#             y=row['Annual number of days']
       
#             writer.writerow([x, y])

def visualize_data(filename):
    with open(filename) as f:
        xpoints=[]
        ypoints=[]
        #convert csv to reader
        reader = csv.reader(f,delimiter=',')
        headers = next(reader)
        #print(headers)
        data = [row for row in reader]
        #print(data)

        for d in data:
            xpoints.append(int(d[0]))
            ypoints.append(int(d[1]))

        #labels
        plt.xlabel("Year")
        plt.ylabel("Number of Frozen Days")

        #plt.xticks(xpoints)

        #plot points
        plt.plot(xpoints,ypoints)

        #save figure into file
        plt.savefig("plot.jpg")

        #plt.show()

    return xpoints,ypoints

def create_feature_vector_X(x):
    vector_X=np.zeros([len(x),2],dtype="int64")
    for i in range(len(x)):
        vector_X[i][0]=1
        vector_X[i][1]=x[i]
    # print(vector_X)

    return vector_X

def create_feature_vector_Y(y):
    vector_Y=np.zeros(len(y),dtype="int64")
    for i in range(len(y)):
        vector_Y[i]=y[i]
    # print(vector_Y)

    return vector_Y

def matrix_product(x):
    #Z=XTX
    Z=np.dot(np.transpose(x),x)
    # print(Z)

    return Z

def inverse_matrix_product(Z):
    #I=(XTX)^-1
    I=np.linalg.inv(Z)
    # print(I)

    return I

def pseudo_inverse_X(I,X):
    #PI+(XTX)^-1 x XT
    PI=np.dot(I,np.transpose(X))
    # print(PI)

    return PI

def calculate_B(PI,Y):
    B=np.dot(PI,Y)
    # print(B)

    return B

def prediction(B):
    #Y_test = B0 + B1_x_test
    x_test=2022
    Y_test=B[0]+B[1]*x_test
    print("Prediction: {:.3f}\n".format(Y_test))

    return B[1],Y_test

def model_interpretation(B1):
    #positive
    if (B1>0):
        symbol=">"
        answer="It is more likely to have Monona ice"
    #negative
    elif(B1<0):
        symbol="<"
        answer="It is lesser likely to have Monona ice"
    #zero
    else:
        symbol="="
        answer="It is equal chance of having and not having Monona ice"
    
    print("Model Interpretation:\n",symbol,"\n",answer,"\n")

def model_limitation(B):
    #B[0]+B[1]x* = 0
    x=(0-B[0])/B[1]
    print("Model Limitation:\nIt is estimated that only during the year {:.3f}, Lake Monona will no longer freeze\n".format(x))

if __name__=="__main__":
    # create_csv()
    filename='data.csv'
    #python3 .\hw5.py .\toy.csv
    # filename=sys.argv[1] #first command line argument passed
    x,y=visualize_data(filename)
    X_vector=create_feature_vector_X(x)
    Y_vector=create_feature_vector_Y(y)
    Z_vector=matrix_product(X_vector)
    I=inverse_matrix_product(Z_vector)
    PI=pseudo_inverse_X(I,X_vector)
    B=calculate_B(PI,Y_vector)
    B1,Y_test=prediction(B)
    model_interpretation(B1)
    model_limitation(B)
