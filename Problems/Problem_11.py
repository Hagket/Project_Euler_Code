#Problem 11#
grid=[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8, 49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0, 81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65, 52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91, 22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80, 24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50, 32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70, 67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21, 24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72, 21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95, 78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92, 16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57, 86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58, 19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40, 4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66, 88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69, 4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36, 20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16, 20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54, 1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
horigrid1=[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
horigrid2=[49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
horigrid3=[81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
horigrid4=[52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
horigrid5=[22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
horigrid6=[24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
horigrid7=[32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
horigrid8=[67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
horigrid9=[24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
horigrid10=[21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
horigrid11=[78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
horigrid12=[16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
horigrid13=[86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
horigrid14=[19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
horigrid15=[4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
horigrid16=[88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
horigrid17=[4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
horigrid18=[20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
horigrid19=[20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
horigrid20=[1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]
products=[]

def horizontal4():
  for i in range(1,18):
    hori4=horigrid1[i-1]*horigrid1[i]*horigrid1[i+1]*horigrid1[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid2[i-1]*horigrid2[i]*horigrid2[i+1]*horigrid2[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid3[i-1]*horigrid3[i]*horigrid3[i+1]*horigrid3[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid4[i-1]*horigrid4[i]*horigrid4[i+1]*horigrid4[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid5[i-1]*horigrid5[i]*horigrid5[i+1]*horigrid5[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid6[i-1]*horigrid6[i]*horigrid6[i+1]*horigrid6[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid7[i-1]*horigrid7[i]*horigrid7[i+1]*horigrid7[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid8[i-1]*horigrid8[i]*horigrid8[i+1]*horigrid8[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid9[i-1]*horigrid9[i]*horigrid9[i+1]*horigrid9[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid10[i-1]*horigrid10[i]*horigrid10[i+1]*horigrid10[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid11[i-1]*horigrid11[i]*horigrid11[i+1]*horigrid11[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid12[i-1]*horigrid12[i]*horigrid12[i+1]*horigrid12[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid13[i-1]*horigrid13[i]*horigrid13[i+1]*horigrid13[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid14[i-1]*horigrid14[i]*horigrid14[i+1]*horigrid14[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid15[i-1]*horigrid15[i]*horigrid15[i+1]*horigrid15[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid16[i-1]*horigrid16[i]*horigrid16[i+1]*horigrid16[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid17[i-1]*horigrid17[i]*horigrid17[i+1]*horigrid17[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid18[i-1]*horigrid18[i]*horigrid18[i+1]*horigrid18[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid19[i-1]*horigrid19[i]*horigrid19[i+1]*horigrid19[i+2]
    products.append(hori4)
  for i in range(1,18):
    hori4=horigrid20[i-1]*horigrid20[i]*horigrid20[i+1]*horigrid20[i+2]
    products.append(hori4)

def vertical4():
  for i in range(1,341):
    verti4=grid[i-1]*grid[i+19]*grid[i+39]*grid[i+59]
    products.append(verti4)

def forwarddiagonal4():
  for i in range(1,18):
    diag4=horigrid1[i-1]*horigrid2[i]*horigrid3[i+1]*horigrid4[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid2[i-1]*horigrid3[i]*horigrid4[i+1]*horigrid5[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid3[i-1]*horigrid4[i]*horigrid5[i+1]*horigrid6[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid4[i-1]*horigrid5[i]*horigrid6[i+1]*horigrid7[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid5[i-1]*horigrid6[i]*horigrid7[i+1]*horigrid8[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid6[i-1]*horigrid7[i]*horigrid8[i+1]*horigrid9[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid7[i-1]*horigrid8[i]*horigrid9[i+1]*horigrid10[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid8[i-1]*horigrid9[i]*horigrid10[i+1]*horigrid11[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid9[i-1]*horigrid10[i]*horigrid11[i+1]*horigrid12[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid10[i-1]*horigrid11[i]*horigrid12[i+1]*horigrid13[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid11[i-1]*horigrid12[i]*horigrid13[i+1]*horigrid14[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid12[i-1]*horigrid13[i]*horigrid14[i+1]*horigrid15[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid13[i-1]*horigrid14[i]*horigrid15[i+1]*horigrid16[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid14[i-1]*horigrid15[i]*horigrid16[i+1]*horigrid17[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid15[i-1]*horigrid16[i]*horigrid17[i+1]*horigrid18[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid16[i-1]*horigrid17[i]*horigrid18[i+1]*horigrid19[i+2]
    products.append(diag4)
  for i in range(1,18):
    diag4=horigrid17[i-1]*horigrid18[i]*horigrid19[i+1]*horigrid20[i+2]
    products.append(diag4)

def backwarddiagonal4():
  for i in range(4,21):
    diag4=horigrid1[i-1]*horigrid2[i-2]*horigrid3[i-3]*horigrid4[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid2[i-1]*horigrid3[i-2]*horigrid4[i-3]*horigrid5[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid3[i-1]*horigrid4[i-2]*horigrid5[i-3]*horigrid6[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid4[i-1]*horigrid5[i-2]*horigrid6[i-3]*horigrid7[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid5[i-1]*horigrid6[i-2]*horigrid7[i-3]*horigrid8[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid6[i-1]*horigrid7[i-2]*horigrid8[i-3]*horigrid9[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid7[i-1]*horigrid8[i-2]*horigrid9[i-3]*horigrid10[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid8[i-1]*horigrid9[i-2]*horigrid10[i-3]*horigrid11[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid9[i-1]*horigrid10[i-2]*horigrid11[i-3]*horigrid12[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid10[i-1]*horigrid11[i-2]*horigrid12[i-3]*horigrid13[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid11[i-1]*horigrid12[i-2]*horigrid13[i-3]*horigrid14[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid12[i-1]*horigrid13[i-2]*horigrid14[i-3]*horigrid15[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid13[i-1]*horigrid14[i-2]*horigrid15[i-3]*horigrid16[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid14[i-1]*horigrid15[i-2]*horigrid16[i-3]*horigrid17[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid15[i-1]*horigrid16[i-2]*horigrid17[i-3]*horigrid18[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid16[i-1]*horigrid17[i-2]*horigrid18[i-3]*horigrid19[i-4]
    products.append(diag4)
  for i in range(4,21):
    diag4=horigrid17[i-1]*horigrid18[i-2]*horigrid19[i-3]*horigrid20[i-4]
    products.append(diag4)

horizontal4()
vertical4()
forwarddiagonal4()
backwarddiagonal4()

products.sort()
print("The greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid is: " + str(products[len(products)-1]))