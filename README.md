# 3D-Bin-Packing_Problem
This project created to solving 3D-Bin-Packing-Problem by find the minimun size of shipping box that can contained all items in one box (without weight).
This project imprementation based on :
* Janet-19/3d-bin-packing-problem. https://github.com/Janet-19/3d-bin-packing-problem

## Download and Usage
Download the whole code then open the [main.ipynb](https://github.com/thanapat2402/genetic_sriracha/blob/main/main.ipynb) to run the program

**Basic parameter**

There are basic parameter that need to set up:
* Bin (size, legth, width, height)
  * For each bin, you need to enter its size (name), length, width, and height.
* Item(name, length, width, height)
  * For each item, you need to enter its name, length, width, and height.
  
**Basic usage**

* At [main.ipynb](https://github.com/thanapat2402/genetic_sriracha/blob/main/main.ipynb) use packer.add_bin() and packer.add_item() 
to add items that needed packing and optional box types. Then, use packer.pack() to perform the whole packing process.
* After packing, the prgram will show the order of box that can hold all items from the smallest to the biggest one and also show how to place the item to the box.
