from django.shortcuts import render
import pyautogui, sys
from time import sleep
import ctypes
import mouseinfo
from django.http import HttpResponseRedirect
from mazeApp.get_pixel_info import *
from django.urls import reverse
# Create your views here.
def BasePage(request):

    return render(request, 'mazeApp/BasePage.html',)

def HomePage(request):

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

        print('X: COORDINATE: ' + str(x) + '   Y COORDINATE ' +  str(y) + ' ')



        print('RGB' + str(li))

        # pyautogui.moveTo(1920 - (x+w), 1080 - (y+h))


        if li == [0,0,0]:
            cond = False
            message = "You Touched the boundary! try again!!"
            break


    return render(request,'mazeApp/HomePage.html')
    # return HttpResponseRedirect(reverse('basepage'),{'message':message})
