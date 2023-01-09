<<<<<<< Updated upstream


class Bin:
    def __init__(self, size, length, width, height, capacity):
        self.size = size 
        self.length = length
        self.width = width
        self.height = height
        self.capacity = capacity
        self.total_items = 0 # number of total items in one bin
        self.items = [] # item in one bin -- a blank list initially
        self.unplaced_items = []
        self.unfitted_items = [] # unfitted item in one bin -- a blank list initially
        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS
    
    def format_numbers(self, number_of_decimals):
        self.length = set_to_decimal(self.length, number_of_decimals)
        self.height = set_to_decimal(self.height, number_of_decimals)
        self.width = set_to_decimal(self.width, number_of_decimals)
        self.capacity = set_to_decimal(self.capacity, number_of_decimals)
        self.number_of_decimals = number_of_decimals
    
    def get_volume(self):
        return set_to_decimal(
            self.length * self.height * self.width, self.number_of_decimals)
     
    def get_total_weight(self):
        total_weight = 0
        
        for item in self.items:
            total_weight += item.weight
        
        return set_to_decimal(total_weight, self.number_of_decimals)
    
    def get_filling_ratio(self):
        total_filling_volume = 0
        total_filling_ratio = 0
        
        for item in self.items:
            total_filling_volume += item.get_volume()
            
        total_filling_ratio = total_filling_volume / self.get_volume()
        return set_to_decimal(total_filling_ratio, self.number_of_decimals)
    
    def can_hold_item_with_rotation(self, item, pivot): 
        """Evaluate whether one item can be placed into bin with all optional orientations.
        Args:
            item: any item in item list.
            pivot: an (x, y, z) coordinate, the back-lower-left corner of the item will be placed at the pivot.
        Returns:
            a list containing all optional orientations. If not, return an empty list.
        """
        
        fit = False 
        valid_item_position = [0, 0, 0]
        item.position = pivot 
        rotation_type_list = [] 
        
        
        for i in range(0, len(RotationType.ALL)): 
            item.rotation_type = i 
            dimension = item.get_dimension() 
            if (
                pivot[0] + dimension[0] <= self.length and  # x-axis
                pivot[1] + dimension[1] <= self.width and  # y-axis
                pivot[2] + dimension[2] <= self.height     # z-axis
            ):
            
                fit = True
                
                for current_item_in_bin in self.items: 
                    if intersect(current_item_in_bin, item): 
                        fit = False
                        item.position = [0, 0, 0]
                        break 
                
                if fit: 
                    if self.get_total_weight() + item.weight > self.capacity: # estimate whether bin reaches its capacity
                        fit = False
                        item.position = [0, 0, 0]
                        continue 
                    
                    else: 
                        rotation_type_list.append(item.rotation_type) 
            
            else:
                continue 
        
        return rotation_type_list 

    def put_item(self, item, pivot, distance_3d): 
        """Evaluate whether an item can be placed into a certain bin with which orientation. If yes, perform put action.
        Args:
            item: any item in item list.
            pivot: an (x, y, z) coordinate, the back-lower-left corner of the item will be placed at the pivot.
            distance_3d: a 3D parameter to determine which orientation should be chosen.
        Returns:
            Boolean variable: False when an item couldn't be placed into the bin; True when an item could be placed and perform put action.
        """
        
        fit = False 
        rotation_type_list = self.can_hold_item_with_rotation(item, pivot)
        margins_3d_list = []
        margins_3d_list_temp = []
        margin_3d = []
        margin_2d = []
        margin_1d = []
        
        n = 0
        m = 0
        p = 0
        
        if not rotation_type_list:
            return fit 
        
        else:
            fit = True 
            
            rotation_type_number = len(rotation_type_list)
            
            if rotation_type_number == 1: 
                item.rotation_type = rotation_type_list[0] 
                self.items.append(item)
                self.total_items += 1
                return fit 
            
            else: 
                for rotation in rotation_type_list: 
                    item.rotation_type = rotation
                    dimension = item.get_dimension()
                    margins_3d = [distance_3d[0] - dimension[0], 
                                 distance_3d[1] - dimension[1], 
                                 distance_3d[2] - dimension[2]]
                    margins_3d_temp = sorted(margins_3d)
                    margins_3d_list.append(margins_3d)
                    margins_3d_list_temp.append(margins_3d_temp)
                
                while p < len(margins_3d_list_temp):
                    margin_3d.append(margins_3d_list_temp[p][0])
                    p += 1
                
                p = 0
                while p < len(margins_3d_list_temp):
                    if margins_3d_list_temp[p][0] == min(margin_3d):
                        n += 1
                        margin_2d.append(margins_3d_list_temp[p][1])
                    
                    p += 1
                
                if n == 1:
                    p = 0
                    while p < len(margins_3d_list_temp):
                        if margins_3d_list_temp[p][0] == min(margin_3d):
                            item.rotation_type = rotation_type_list[p]
                            self.items.append(item)
                            self.total_items += 1
                            return fit 
                        
                        p += 1
                
                else:
                    p = 0
                    while p < len(margins_3d_list_temp):
                        if (
                            margins_3d_list_temp[p][0] == min(margin_3d) and
                            margins_3d_list_temp[p][1] == min(margin_2d)
                        ):
                            m += 1
                            margin_1d.append(margins_3d_list_temp[p][2])
                        
                        p += 1
                
                if m == 1:
                    p = 0
                    while p < len(margins_3d_list_temp):
                        if (
                            margins_3d_list_temp[p][0] == min(margin_3d) and
                            margins_3d_list_temp[p][1] == min(margin_2d)
                        ):
                            item.rotation_type = rotation_type_list[p]
                            self.items.append(item)
                            self.total_items += 1
                            return fit 
                        
                        p += 1
                
                else:
                    p = 0
                    while p < len(margins_3d_list_temp):
                        if (
                            margins_3d_list_temp[p][0] == min(margin_3d) and
                            margins_3d_list_temp[p][1] == min(margin_2d) and
                            margins_3d_list_temp[p][2] == min(margin_1d)
                        ):
                            item.rotation_type = rotation_type_list[p]
                            self.items.append(item)
                            self.total_items += 1
                            return fit 
                        
                        p += 1
        
    def string(self):
        return "%s(%sx%sx%s, max_weight:%s) vol(%s) item_number(%s) filling_ratio(%s)" % (
            self.size, self.length, self.width, self.height, self.capacity,
            self.get_volume(), self.total_items, self.get_filling_ratio())
=======
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "%run ./constants.ipynb\n",
    "%run ./auxiliary_methods.ipynb"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Bin:\n",
    "    def __init__(self, size, length, width, height, capacity):\n",
    "        self.size = size \n",
    "        self.length = length\n",
    "        self.width = width\n",
    "        self.height = height\n",
    "        self.capacity = capacity\n",
    "        self.total_items = 0 # number of total items in one bin\n",
    "        self.items = [] # item in one bin -- a blank list initially\n",
    "        self.unplaced_items = []\n",
    "        self.unfitted_items = [] # unfitted item in one bin -- a blank list initially\n",
    "        self.number_of_decimals = DEFAULT_NUMBER_OF_DECIMALS\n",
    "    \n",
    "    def format_numbers(self, number_of_decimals):\n",
    "        self.length = set_to_decimal(self.length, number_of_decimals)\n",
    "        self.height = set_to_decimal(self.height, number_of_decimals)\n",
    "        self.width = set_to_decimal(self.width, number_of_decimals)\n",
    "        self.capacity = set_to_decimal(self.capacity, number_of_decimals)\n",
    "        self.number_of_decimals = number_of_decimals\n",
    "    \n",
    "    def get_volume(self):\n",
    "        return set_to_decimal(\n",
    "            self.length * self.height * self.width, self.number_of_decimals)\n",
    "     \n",
    "    def get_total_weight(self):\n",
    "        total_weight = 0\n",
    "        \n",
    "        for item in self.items:\n",
    "            total_weight += item.weight\n",
    "        \n",
    "        return set_to_decimal(total_weight, self.number_of_decimals)\n",
    "    \n",
    "    def get_filling_ratio(self):\n",
    "        total_filling_volume = 0\n",
    "        total_filling_ratio = 0\n",
    "        \n",
    "        for item in self.items:\n",
    "            total_filling_volume += item.get_volume()\n",
    "            \n",
    "        total_filling_ratio = total_filling_volume / self.get_volume()\n",
    "        return set_to_decimal(total_filling_ratio, self.number_of_decimals)\n",
    "    \n",
    "    def can_hold_item_with_rotation(self, item, pivot): \n",
    "        \"\"\"Evaluate whether one item can be placed into bin with all optional orientations.\n",
    "        Args:\n",
    "            item: any item in item list.\n",
    "            pivot: an (x, y, z) coordinate, the back-lower-left corner of the item will be placed at the pivot.\n",
    "        Returns:\n",
    "            a list containing all optional orientations. If not, return an empty list.\n",
    "        \"\"\"\n",
    "        \n",
    "        fit = False \n",
    "        valid_item_position = [0, 0, 0]\n",
    "        item.position = pivot \n",
    "        rotation_type_list = [] \n",
    "        \n",
    "        \n",
    "        for i in range(0, len(RotationType.ALL)): \n",
    "            item.rotation_type = i \n",
    "            dimension = item.get_dimension() \n",
    "            if (\n",
    "                pivot[0] + dimension[0] <= self.length and  # x-axis\n",
    "                pivot[1] + dimension[1] <= self.width and  # y-axis\n",
    "                pivot[2] + dimension[2] <= self.height     # z-axis\n",
    "            ):\n",
    "            \n",
    "                fit = True\n",
    "                \n",
    "                for current_item_in_bin in self.items: \n",
    "                    if intersect(current_item_in_bin, item): \n",
    "                        fit = False\n",
    "                        item.position = [0, 0, 0]\n",
    "                        break \n",
    "                \n",
    "                if fit: \n",
    "                    if self.get_total_weight() + item.weight > self.capacity: # estimate whether bin reaches its capacity\n",
    "                        fit = False\n",
    "                        item.position = [0, 0, 0]\n",
    "                        continue \n",
    "                    \n",
    "                    else: \n",
    "                        rotation_type_list.append(item.rotation_type) \n",
    "            \n",
    "            else:\n",
    "                continue \n",
    "        \n",
    "        return rotation_type_list \n",
    "\n",
    "    def put_item(self, item, pivot, distance_3d): \n",
    "        \"\"\"Evaluate whether an item can be placed into a certain bin with which orientation. If yes, perform put action.\n",
    "        Args:\n",
    "            item: any item in item list.\n",
    "            pivot: an (x, y, z) coordinate, the back-lower-left corner of the item will be placed at the pivot.\n",
    "            distance_3d: a 3D parameter to determine which orientation should be chosen.\n",
    "        Returns:\n",
    "            Boolean variable: False when an item couldn't be placed into the bin; True when an item could be placed and perform put action.\n",
    "        \"\"\"\n",
    "        \n",
    "        fit = False \n",
    "        rotation_type_list = self.can_hold_item_with_rotation(item, pivot)\n",
    "        margins_3d_list = []\n",
    "        margins_3d_list_temp = []\n",
    "        margin_3d = []\n",
    "        margin_2d = []\n",
    "        margin_1d = []\n",
    "        \n",
    "        n = 0\n",
    "        m = 0\n",
    "        p = 0\n",
    "        \n",
    "        if not rotation_type_list:\n",
    "            return fit \n",
    "        \n",
    "        else:\n",
    "            fit = True \n",
    "            \n",
    "            rotation_type_number = len(rotation_type_list)\n",
    "            \n",
    "            if rotation_type_number == 1: \n",
    "                item.rotation_type = rotation_type_list[0] \n",
    "                self.items.append(item)\n",
    "                self.total_items += 1\n",
    "                return fit \n",
    "            \n",
    "            else: \n",
    "                for rotation in rotation_type_list: \n",
    "                    item.rotation_type = rotation\n",
    "                    dimension = item.get_dimension()\n",
    "                    margins_3d = [distance_3d[0] - dimension[0], \n",
    "                                 distance_3d[1] - dimension[1], \n",
    "                                 distance_3d[2] - dimension[2]]\n",
    "                    margins_3d_temp = sorted(margins_3d)\n",
    "                    margins_3d_list.append(margins_3d)\n",
    "                    margins_3d_list_temp.append(margins_3d_temp)\n",
    "                \n",
    "                while p < len(margins_3d_list_temp):\n",
    "                    margin_3d.append(margins_3d_list_temp[p][0])\n",
    "                    p += 1\n",
    "                \n",
    "                p = 0\n",
    "                while p < len(margins_3d_list_temp):\n",
    "                    if margins_3d_list_temp[p][0] == min(margin_3d):\n",
    "                        n += 1\n",
    "                        margin_2d.append(margins_3d_list_temp[p][1])\n",
    "                    \n",
    "                    p += 1\n",
    "                \n",
    "                if n == 1:\n",
    "                    p = 0\n",
    "                    while p < len(margins_3d_list_temp):\n",
    "                        if margins_3d_list_temp[p][0] == min(margin_3d):\n",
    "                            item.rotation_type = rotation_type_list[p]\n",
    "                            self.items.append(item)\n",
    "                            self.total_items += 1\n",
    "                            return fit \n",
    "                        \n",
    "                        p += 1\n",
    "                \n",
    "                else:\n",
    "                    p = 0\n",
    "                    while p < len(margins_3d_list_temp):\n",
    "                        if (\n",
    "                            margins_3d_list_temp[p][0] == min(margin_3d) and\n",
    "                            margins_3d_list_temp[p][1] == min(margin_2d)\n",
    "                        ):\n",
    "                            m += 1\n",
    "                            margin_1d.append(margins_3d_list_temp[p][2])\n",
    "                        \n",
    "                        p += 1\n",
    "                \n",
    "                if m == 1:\n",
    "                    p = 0\n",
    "                    while p < len(margins_3d_list_temp):\n",
    "                        if (\n",
    "                            margins_3d_list_temp[p][0] == min(margin_3d) and\n",
    "                            margins_3d_list_temp[p][1] == min(margin_2d)\n",
    "                        ):\n",
    "                            item.rotation_type = rotation_type_list[p]\n",
    "                            self.items.append(item)\n",
    "                            self.total_items += 1\n",
    "                            return fit \n",
    "                        \n",
    "                        p += 1\n",
    "                \n",
    "                else:\n",
    "                    p = 0\n",
    "                    while p < len(margins_3d_list_temp):\n",
    "                        if (\n",
    "                            margins_3d_list_temp[p][0] == min(margin_3d) and\n",
    "                            margins_3d_list_temp[p][1] == min(margin_2d) and\n",
    "                            margins_3d_list_temp[p][2] == min(margin_1d)\n",
    "                        ):\n",
    "                            item.rotation_type = rotation_type_list[p]\n",
    "                            self.items.append(item)\n",
    "                            self.total_items += 1\n",
    "                            return fit \n",
    "                        \n",
    "                        p += 1\n",
    "        \n",
    "    def string(self):\n",
    "        return \"%s(%sx%sx%s, max_weight:%s) vol(%s) item_number(%s) filling_ratio(%s)\" % (\n",
    "            self.size, self.length, self.width, self.height, self.capacity,\n",
    "            self.get_volume(), self.total_items, self.get_filling_ratio())\n"
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
