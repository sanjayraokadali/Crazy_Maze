from django.shortcuts import render
import pyautogui, sys
from time import sleep
import ctypes
import mouseinfo
from mazeApp.get_pixel_info import *
# Create your views here.
def BasePage(request):

    cond = True

    while cond:

        (x,y) = pyautogui.position()


        colorRef = ctypes.windll.gdi32.GetPixel(dc, x, y)  # A COLORREF value as 0x00bbggrr. See https://docs.microsoft.com/en-us/windows/win32/gdi/colorref
        red = colorRef % 256
        colorRef //= 256
        green = colorRef % 256
        colorRef //= 256
        blue = colorRef

        li = [red,green,blue]

        print('rgb' + str(li))

        if li == [0,0,0]:
            cond = False
            break


    return render(request, 'mazeApp/BasePage.html',{'cond':cond})

def HomePage(request):



    return render(request, 'mazeApp/HomePage.html')
