from django.shortcuts import render
import pyautogui, sys
from time import sleep
import time
import ctypes
import mouseinfo
from django.http import HttpResponseRedirect
from mazeApp.get_pixel_info import *
from django.urls import reverse
# Create your views here.
def BasePage(request):

    return render(request, 'mazeApp/BasePage.html',)

def HomePage(request):

    t_start = 0
    t_stop = 0

    cond = True

    while cond:

        t_start = time.time()

        ## RECEIVING CURRENT CURSOR POSITION ON THE INTERFACE
        (x,y) = pyautogui.position()

        ## FINDING THE RGB REFERENCES USING THE X AND Y LOCATIONS OF THE CURSOR
        colorRef = ctypes.windll.gdi32.GetPixel(dc, x, y)  # A COLORREF value as 0x00bbggrr. See https://docs.microsoft.com/en-us/windows/win32/gdi/colorref
        red = colorRef % 256
        colorRef //= 256
        green = colorRef % 256
        colorRef //= 256
        blue = colorRef

        li = [red,green,blue]

        ## PRINTING OUT THE COORDINATES AND RGB BAND
        print('X: COORDINATE: ' + str(x) + '   Y COORDINATE ' +  str(y) + ' ')

        print('RGB' + str(li))

        # pyautogui.moveTo(1920 - (x+w), 1080 - (y+h))

        ## LOOP BREAK CONDITION ///// WHEN USER TOUCHED THE BOUNDARY
        if li == [0,0,0]:
            cond = False
            message = "You touched the boundary! try again!!"
            t_stop = time.time()
            counter = t_stop - t_start
            break



    return render(request,'mazeApp/HomePage.html', {'time':counter * 100,'message':message})
    # return HttpResponseRedirect(reverse('basepage'),{'message':message})
