<<<<<<< Updated upstream
class RotationType :
    RT_LWH = 0
    RT_HLW = 1
    RT_HWL = 2
    RT_WHL = 3
    RT_WLH = 4
    RT_LHW = 5
    
    ALL = [RT_LWH, RT_HLW, RT_HWL, RT_WHL, RT_WLH, RT_LHW]

class Axis:
    LENGTH = 0
    WIDTH = 1
    HEIGHT = 2
    
    ALL = [LENGTH, WIDTH, HEIGHT]

=======
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# length in x-axis; width in y-axis; height in z-axis\n",
    "\n",
    "\n",
    "class RotationType :\n",
    "    RT_LWH = 0\n",
    "    RT_HLW = 1\n",
    "    RT_HWL = 2\n",
    "    RT_WHL = 3\n",
    "    RT_WLH = 4\n",
    "    RT_LHW = 5\n",
    "    \n",
    "    ALL = [RT_LWH, RT_HLW, RT_HWL, RT_WHL, RT_WLH, RT_LHW]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# (x, y, z) --> (length, width, height)\n",
    "class Axis:\n",
    "    LENGTH = 0\n",
    "    WIDTH = 1\n",
    "    HEIGHT = 2\n",
    "    \n",
    "    ALL = [LENGTH, WIDTH, HEIGHT]"
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
