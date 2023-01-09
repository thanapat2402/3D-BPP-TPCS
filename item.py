<<<<<<< Updated upstream
from constants import *
from extensions import Extensions

class Item:
    def __init__(self, name, length, width, height, weight):
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.weight = weight
        self.rotation_type = 0 # initial rotation type: (x, y, z) --> (l, w, h)
        self.position = START_POSITION # initial position: (0, 0, 0)
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS
    
    def format_numbers(self, number_of_decimals):
        self.length = set_to_decimal(self.length, number_of_decimals)
        self.height = set_to_decimal(self.height, number_of_decimals)
        self.width = set_to_decimal(self.width, number_of_decimals)
        self.weight = set_to_decimal(self.weight, number_of_decimals)
        self.number_of_decimals = number_of_decimals
        
    def get_volume(self):
        return set_to_decimal(
            self.length * self.height * self.width, self.number_of_decimals)
    
    def get_dimension(self): # 6 orientation types -- (x-axis, y-axis, z-axis)
        if self.rotation_type == RotationType.RT_LWH:
            dimension = [self.length, self.width, self.height]
        elif self.rotation_type == RotationType.RT_HLW:
            dimension = [self.height, self.length, self.width]
        elif self.rotation_type == RotationType.RT_HWL:
            dimension = [self.height, self.width, self.length]
        elif self.rotation_type == RotationType.RT_WHL:
            dimension = [self.width, self.height, self.length]
        elif self.rotation_type == RotationType.RT_WLH:
            dimension = [self.width, self.length, self.height]
        elif self.rotation_type == RotationType.RT_LHW:
            dimension = [self.length, self.height, self.width]
        else:
            dimension = []
        
        return dimension
        
    def string(self):
        rotation_list = ["LWH","HLW","HLW","WHL","WLH","LHW"]
        return "%s(%sx%sx%s, weight: %s) pos(%s) rt(%s) vol(%s)" % (
            self.name, self.length, self.width, self.height, self.weight,
            self.position, rotation_list[self.rotation_type], self.get_volume()
        )
=======
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "%run ./constants.ipynb\n",
    "%run ./auxiliary_methods.ipynb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Item:\n",
    "    def __init__(self, name, length, width, height, weight):\n",
    "        self.name = name\n",
    "        self.length = length\n",
    "        self.width = width\n",
    "        self.height = height\n",
    "        self.weight = weight\n",
    "        self.rotation_type = 0 # initial rotation type: (x, y, z) --> (l, w, h)\n",
    "        self.position = START_POSITION # initial position: (0, 0, 0)\n",
    "        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS\n",
    "    \n",
    "    def format_numbers(self, number_of_decimals):\n",
    "        self.length = set_to_decimal(self.length, number_of_decimals)\n",
    "        self.height = set_to_decimal(self.height, number_of_decimals)\n",
    "        self.width = set_to_decimal(self.width, number_of_decimals)\n",
    "        self.weight = set_to_decimal(self.weight, number_of_decimals)\n",
    "        self.number_of_decimals = number_of_decimals\n",
    "        \n",
    "    def get_volume(self):\n",
    "        return set_to_decimal(\n",
    "            self.length * self.height * self.width, self.number_of_decimals)\n",
    "    \n",
    "    def get_dimension(self): # 6 orientation types -- (x-axis, y-axis, z-axis)\n",
    "        if self.rotation_type == RotationType.RT_LWH:\n",
    "            dimension = [self.length, self.width, self.height]\n",
    "        elif self.rotation_type == RotationType.RT_HLW:\n",
    "            dimension = [self.height, self.length, self.width]\n",
    "        elif self.rotation_type == RotationType.RT_HWL:\n",
    "            dimension = [self.height, self.width, self.length]\n",
    "        elif self.rotation_type == RotationType.RT_WHL:\n",
    "            dimension = [self.width, self.height, self.length]\n",
    "        elif self.rotation_type == RotationType.RT_WLH:\n",
    "            dimension = [self.width, self.length, self.height]\n",
    "        elif self.rotation_type == RotationType.RT_LHW:\n",
    "            dimension = [self.length, self.height, self.width]\n",
    "        else:\n",
    "            dimension = []\n",
    "        \n",
    "        return dimension\n",
    "        \n",
    "    def string(self):\n",
    "        rotation_list = [\"LWH\",\"HLW\",\"HLW\",\"WHL\",\"WLH\",\"LHW\"]\n",
    "        return \"%s(%sx%sx%s, weight: %s) pos(%s) rt(%s) vol(%s)\" % (\n",
    "            self.name, self.length, self.width, self.height, self.weight,\n",
    "            self.position, rotation_list[self.rotation_type], self.get_volume()\n",
    "        )"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.0 64-bit",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.0"
  },
  "vscode": {
   "interpreter": {
    "hash": "afb734500600fd355917ca529030176ea0ca205570884b88f2f6f7d791fd3fbe"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
>>>>>>> Stashed changes
