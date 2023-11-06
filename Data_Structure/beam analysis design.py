def Dbeam(fy, fck, b, d, dt, As, Asp, dp):



   #assumption: fck<=40 MPa
  #  if fck <= 40:
   n = 1.00
   ecu = 0.003
   beta1 = 0.80

   #equivalent stress block
   a = ((As - Asp) * fy) / ((0.85 * fck * b))
   c = a/ beta1
  #  Mn= As * fy * (d-a / 2) * 1E-6 #kN.m
   es = 0.003 * (c - dp) / c
   et = ecu * (dt-c) / c

   discriminant = ((660 * Asp - As * fy) ** 2 )+ (4 * n * 0.85 * fck * b * 660 * Asp * beta1 * dp)

   if es > 0.002:
      a = ((As - Asp) * fy) / ((0.85 * fck * b))
      print("1번조건")
      print("1번dscriminant", discriminant)

      Mn = (Asp * fy * (d-dp) + (As- Asp) * fy * (d - a/2)) * 1E-6 #kN.m
      c = a / beta1
      esp = 0.003 * (c - dp) / c
      fsp =  200000 * esp
     
   else:
      if discriminant >= 0:
         print("2번조건")
         print("번dscriminant", discriminant)
         a = (-(660 * Asp - As * fy) + discriminant ** 0.5) / (2 * n * 0.85 * fck * b)
         c = a / beta1
         esp = 0.003 * (c - dp) / c
         fsp =  200000 * esp
         Mn = 0.85 * fck * a * b *(d - a / 2) + Asp * fsp * (d - dp)

      else:
         print("3번조건")
         print("dscriminant", discriminant)
         a = (-(660 * Asp - As * fy) + (- discriminant) ** 0.5) / (2 * n * 0.85 * fck * b)
         c = a / beta1
         esp = 0.003 * (c - dp) / c
         fsp =  200000 * esp
         Mn = 0.85 * fck * a * b *(d - a / 2) + Asp * fsp * (d - dp)




   #check maximum reinforcement
   if et<0.004:
      print("Error: The given section is not a beam")
      phi = 0.0
   elif et<0.005:
      phi = 0.65 + (0.85-0.65)*(et-0.002)/0.003
   else:
      phi = 0.85

   #check minimum reinforcement
   fr = 0.63 * (fck ** 0.5)
   h = d + 60
   Mcr = fr * b * h * h / 6 * 1E-6 #kN.m
   pMn = phi * Mn

   print("mcr" , Mcr)
   print('pMn', pMn)

  #  pMn = pMn.real
   
   if pMn < 1.2 * Mcr:
      print("Error: Too little reinforcement")
      phi = 0.0


   pMn = phi * Mn


   return a, c, et, Mn , phi, pMn, Mcr




# D22 = 387.1
# D25 = 506.7
# D29 = 642.6



#Dbeam 예제 1
fy, fck, b, d, dt, As, Asp, dp = 400, 24, 400, 515, 540, 8 * 506.7, 2 * 387.1, 60
a, c, et, Mn, phi, pMn, Mcr = Dbeam(fy, fck, b, d, dt, As, Asp, dp)
print(f'[Dbeam] a={a:6.1f}mm, c={c:6.1f}mm, et={et:7.4f}, Mn={Mn:6.1f}kN.m, phi={phi:6.3f}, pMn={pMn:6.1f}kN.m, Mcr={Mcr:6.1f}kN.m')

#Dbeam 예제 2
fy, fck, b, d, dt, As, Asp, dp = 400, 27, 400, 710, 740, 8*387.1, 2*387.1, 60
a, c, et, Mn, phi, pMn, Mcr = Dbeam(fy, fck, b, d, dt, As, Asp, dp)
print(f'[Dbeam] a={a:6.1f}mm, c={c:6.1f}mm, et={et:7.4f}, Mn={Mn:6.1f}kN.m, phi={phi:6.3f}, pMn={pMn:6.1f}kN.m, Mcr={Mcr:6.1f}kN.m')

#Dbeam 예제 3
fy, fck, b, d, dt, As, Asp, dp = 300, 21, 400, 515, 540, 8*387.1, 2*387.1, 60
a, c, et, Mn, phi, pMn, Mcr = Dbeam(fy, fck, b, d, dt, As, Asp, dp)
print(f'[Dbeam] a={a:6.1f}mm, c={c:6.1f}mm, et={et:7.4f}, Mn={Mn:6.1f}kN.m, phi={phi:6.3f}, pMn={pMn:6.1f}kN.m, Mcr={Mcr:6.1f}kN.m')

#Dbeam 예제 4-2
fy, fck, b, d, dt, As, Asp, dp = 400, 21, 300, 515, 540, 8*387.1, 2*387.1, 60
a, c, et, Mn, phi, pMn, Mcr = Dbeam(fy, fck, b, d, dt, As, Asp, dp)
print(f'[Dbeam] a={a:6.1f}mm, c={c:6.1f}mm, et={et:7.4f}, Mn={Mn:6.1f}kN.m, phi={phi:6.3f}, pMn={pMn:6.1f}kN.m, Mcr={Mcr:6.1f}kN.m')

#Dbeam 예제 4-3
fy, fck, b, d, dt, As, Asp, dp = 400, 21, 300, 515, 540, 8*387.1, 4*387.1, 60
a, c, et, Mn, phi, pMn, Mcr = Dbeam(fy, fck, b, d, dt, As, Asp, dp)
print(f'[Dbeam] a={a:6.1f}mm, c={c:6.1f}mm, et={et:7.4f}, Mn={Mn:6.1f}kN.m, phi={phi:6.3f}, pMn={pMn:6.1f}kN.m, Mcr={Mcr:6.1f}kN.m')


