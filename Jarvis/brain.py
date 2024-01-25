import torch.nn as nn   #provides tool for building neural networks

class NeuralNet(nn.Module):   #class inherited from nn.Module class
    def __init__(self,input_size,hidden_size,num_classes):  #initialize Neuralnet class
        super(NeuralNet,self).__init__()   #calls the initialization of parent class
        self.l1 =nn.Linear(input_size,hidden_size)  #create instance of nn.Linear class as l1
        self.l2=nn.Linear(hidden_size,hidden_size)
        self.l3=nn.Linear(hidden_size,num_classes)
        self.relu=nn.ReLU()   #Introduces non-linearity to network by outputting the maximum of zero & input
    
    def forward(self,x):
        out=self.l1(x)   #first linear transformation(l1) to input tensor 'x' 
        out=self.relu(out)
        out=self.l2(out)
        out=self.relu(out)
        out=self.l3(out)
        return out       #returns output of tensor meaning the "prediction of neural network"  



