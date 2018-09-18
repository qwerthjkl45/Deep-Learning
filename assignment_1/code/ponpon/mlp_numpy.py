"""
This module implements a multi-layer perceptron (MLP) in NumPy.
You should fill in code into indicated sections.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from modules import * 

class MLP(object):
  """
  This class implements a Multi-layer Perceptron in NumPy.
  It handles the different layers and parameters of the model.
  Once initialized an MLP object can perform forward and backward.
  """

  def __init__(self, n_inputs, n_hidden, n_classes):
    """
    Initializes MLP object. 
    
    Args:
      n_inputs: number of inputs.
      n_hidden: list of ints, specifies the number of units
                in each linear layer. If the list is empty, the MLP
                will not have any linear layers, and the model
                will simply perform a multinomial logistic regression.
      n_classes: number of classes of the classification problem.
                 This number is required in order to specify the
                 output dimensions of the MLP
    
    TODO:
    Implement initialization of the network.
    """

    ########################
    # PUT YOUR CODE HERE  #
    #######################
    
    self.layers = []    
    for idx, n_node in enumerate(n_hidden):

        if idx == 0:
            dim_in = n_inputs
        else:
            dim_in = dim_out
            
        dim_out = n_node
        
        self.layers += [LinearModule(dim_in, dim_out)]
        
        self.layers += [ReLUModule()]
    
    dim_in = dim_out
    dim_out = n_classes
    self.layers += [LinearModule(dim_in, dim_out)]
    self.layers += [SoftMaxModule()]
    
    self.loss = CrossEntropyModule()

    ########################
    # END OF YOUR CODE    #
    #######################

  def forward(self, x):
    """
    Performs forward pass of the input. Here an input tensor x is transformed through 
    several layer transformations.
    
    Args:
      x: input to the network
    Returns:
      out: outputs of the network
    
    TODO:
    Implement forward pass of the network.
    """

    ########################
    # PUT YOUR CODE HERE  #
    #######################
    out = x

    #x = x.reshape(x.shape[0], -1)
    for layer in self.layers:        
    #    if not isinstance(layer, CrossEntropyModule):
        out = layer.forward(out)
    
    ########################
    # END OF YOUR CODE    #
    #######################

    return out

  def backward(self, dout):
    """
    Performs backward pass given the gradients of the loss. 

    Args:
      dout: gradients of the loss
    
    TODO:
    Implement backward pass of the network.
    """
    
    ########################
    # PUT YOUR CODE HERE  #
    #######################    

    for layer in reversed(self.layers):
        #if not isinstance(layer, CrossEntropyModule):
        dout = layer.backward(dout)
        if isinstance(layer, LinearModule):
            layer.params['weight'] = layer.params['weight'] - 0.01 * layer.grads['weight']
            layer.params['bias'] = layer.params['bias'] - 0.01 * layer.grads['bias']

            print(layer.grads['weight'])
    ########################
    # END OF YOUR CODE    #
    #######################

    return
