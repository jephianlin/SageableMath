## -*- encoding: utf-8 -*-

# This file was *autogenerated* from the file SageableMath-2019SMath316.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3 = Integer(3); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0); _sage_const_7 = Integer(7); _sage_const_6 = Integer(6); _sage_const_5 = Integer(5); _sage_const_4 = Integer(4); _sage_const_116 = Integer(116); _sage_const_105 = Integer(105); _sage_const_107 = Integer(107); _sage_const_89 = Integer(89); _sage_const_47 = Integer(47); _sage_const_113 = Integer(113); _sage_const_112 = Integer(112); _sage_const_86 = Integer(86); _sage_const_1p5 = RealNumber('1.5'); _sage_const_114 = Integer(114); _sage_const_0p1 = RealNumber('0.1'); _sage_const_0p2 = RealNumber('0.2'); _sage_const_2p5 = RealNumber('2.5'); _sage_const_30 = Integer(30); _sage_const_50 = Integer(50); _sage_const_98 = Integer(98); _sage_const_126 = Integer(126); _sage_const_124 = Integer(124); _sage_const_125 = Integer(125); _sage_const_103 = Integer(103); _sage_const_104 = Integer(104); _sage_const_96 = Integer(96); _sage_const_95 = Integer(95); _sage_const_94 = Integer(94)## This file (SageableMath-2019SMath316.sagetex.sage) was *autogenerated* from SageableMath-2019SMath316.tex with sagetex.sty version 2015/08/26 v3.0-92d9f7a.
import sagetex
_st_ = sagetex.SageTeXProcessor('SageableMath-2019SMath316', version='2015/08/26 v3.0-92d9f7a', version_check=True)
_st_.current_tex_line = _sage_const_47 
_st_.blockbegin()
try:
 def linear_regression(data, draw=False):
     """
     Input:
         data: a list of pairs [(x1,y1), ..., (xN,yN)]
     Output:
         Output [a,b] so that the line y = ax + b
         is the best fitting line for the data.
         When draw == True,
         create a graphical illustration p and return [a,b,p].
     """
     NN = len(data)
     ### x_list = [x1, x2, ..., xN]
     x_list = [p[_sage_const_0 ] for p in data]
     ### one_list = [1,1, ..., 1]
     one_list = [_sage_const_1 ] * NN
     ### y_list = [y1, y2, ..., yN]
     y_list = [p[_sage_const_1 ] for p in data]
     ### define A and v as described in the algorithm
     A = matrix([x_list, one_list]).transpose()
     v = matrix([y_list]).transpose()
     AT = A.transpose()
     ATA = AT * A
     ATAinv = ATA.pseudoinverse()
     ans = ATAinv * AT * v
     a, b = ans.transpose()[_sage_const_0 ]
 
     if draw:
         x_min = min(x_list)
         x_max = max(x_list)
         x_range = x_max - x_min
         x = var('x')
         pic = (a*x + b).plot(xmin=x_min-_sage_const_0p1 *x_range,
                              xmax=x_max+_sage_const_0p1 *x_range)
         pic += point(data, rgbcolor='red', size=_sage_const_30 )
 
         return [a,b,pic]
 
     return [a,b]
except:
 _st_.goboom(_sage_const_86 )
_st_.blockend()
_st_.current_tex_line = _sage_const_89 
_st_.blockbegin()
try:
 ### horizontal data
 data = [(_sage_const_1 ,_sage_const_1 ),(_sage_const_2 ,_sage_const_1 ),(_sage_const_3 ,_sage_const_1 ),(_sage_const_4 ,_sage_const_1 ),(_sage_const_5 ,_sage_const_1 )]
 
 a,b,p = linear_regression(data,True)
except:
 _st_.goboom(_sage_const_94 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_0 , latex(a))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_95 
 _st_.inline(_sage_const_1 , latex(b))
except:
 _st_.goboom(_sage_const_95 )
try:
 _st_.current_tex_line = _sage_const_96 
 _st_.plot(_sage_const_0 , format='notprovided', _p_=p)
except:
 _st_.goboom(_sage_const_96 )
_st_.current_tex_line = _sage_const_98 
_st_.blockbegin()
try:
 ### linear data
 data = [(_sage_const_1 ,_sage_const_1 ),(_sage_const_2 ,_sage_const_1p5 ),(_sage_const_3 ,_sage_const_2 ),(_sage_const_4 ,_sage_const_2p5 ),(_sage_const_5 ,_sage_const_3 )]
 
 a,b,p = linear_regression(data,True)
except:
 _st_.goboom(_sage_const_103 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_2 , latex(a))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_104 
 _st_.inline(_sage_const_3 , latex(b))
except:
 _st_.goboom(_sage_const_104 )
try:
 _st_.current_tex_line = _sage_const_105 
 _st_.plot(_sage_const_1 , format='notprovided', _p_=p)
except:
 _st_.goboom(_sage_const_105 )
_st_.current_tex_line = _sage_const_107 
_st_.blockbegin()
try:
 ### non-linear data
 data = [(_sage_const_1 ,_sage_const_1 ),(_sage_const_2 ,_sage_const_1 ),(_sage_const_3 ,_sage_const_2 ),(_sage_const_4 ,_sage_const_2 ),(_sage_const_5 ,_sage_const_3 )]
 
 a,b,p = linear_regression(data,True)
except:
 _st_.goboom(_sage_const_112 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_4 , latex(a))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_113 
 _st_.inline(_sage_const_5 , latex(b))
except:
 _st_.goboom(_sage_const_113 )
try:
 _st_.current_tex_line = _sage_const_114 
 _st_.plot(_sage_const_2 , format='notprovided', _p_=p)
except:
 _st_.goboom(_sage_const_114 )
_st_.current_tex_line = _sage_const_116 
_st_.blockbegin()
try:
 ### almost-linear data
 import numpy as np
 x = np.linspace(_sage_const_1 ,_sage_const_5 ,_sage_const_50 )
 y = x*_sage_const_0p2  + _sage_const_1  + _sage_const_0p1 *np.random.randn(_sage_const_50 )
 data = list(zip(x,y))
 
 a,b,p = linear_regression(data,True)
except:
 _st_.goboom(_sage_const_124 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_6 , latex(a))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_125 
 _st_.inline(_sage_const_7 , latex(b))
except:
 _st_.goboom(_sage_const_125 )
try:
 _st_.current_tex_line = _sage_const_126 
 _st_.plot(_sage_const_3 , format='notprovided', _p_=p)
except:
 _st_.goboom(_sage_const_126 )
_st_.endofdoc()
