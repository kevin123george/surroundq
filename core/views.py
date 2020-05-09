from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
import matplotlib.patches as patches
# Create your views here.
from django.template import loader


def index(request):
    return render(request, 'index.html')


def example(request):
    lookup = request.GET.get('q')
    print(lookup)
    if lookup:
        print("\n The machine has learned to draw a line from (-x,-y) tp (x,y)")
        # val = int(input("\nEnter the value of x(y=x): "));
        # val = int(10)
        val = int(lookup)
        plt.plot(range(val), '-r')
        plt.title('Graph of y-x=0')
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.grid()
        # plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')
        plt.show()
        return render(request, 'example.html')
    if request.GET.get('x') and request.GET.get('y'):
        print("The machine has learned to identify if the points specified is inside or outside the circle")
        # xval = int(input("\nEnter the value of x: "));
        # yval = int(input("\nEnter the value of y: "));
        xval = int(request.GET.get('x'))
        yval = int(request.GET.get('y'))
        if (xval * xval) + (yval * yval) > 25:
            print("Outside circle")
            xlimt = xval + 1
            ylimt = yval + 1
        else:
            print("Inside circle")
            xlimt = ylimt = 6
        circle1 = plt.Circle((0, 0), 5, color='r')

        fig, ax = plt.subplots(1)
        ax.set_aspect(1)
        plt.xlim(-xlimt, xlimt)
        plt.ylim(-ylimt, ylimt)
        ax.add_artist(circle1)
        ax.plot((xval), (yval), 'o', color='y')
        plt.plot(xval, yval)
        plt.grid(linestyle='--')
        plt.title('Circle with radius 5', fontsize=8)
        # plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')
        plt.show()
        return render(request, 'example.html')

    if request.GET.get('a') and request.GET.get('b'):
        print("The machine has learned to identify if the points specified is inside or outside the square")
        xval = int(request.GET.get('a'))
        yval = int(request.GET.get('b'))
        if xval >= -4 and xval <= 4 and yval >= -4 and yval <= 4:
            print("Inside")
            xlimt = ylimt = 6
        else:
            print("Outside")
            xlimt = xval + 1
            ylimt = yval + 1

        fig, ax = plt.subplots(1)
        ax.set_aspect(1)
        plt.xlim(-xlimt, xlimt)
        plt.ylim(-ylimt, ylimt)
        ax.add_patch(
            patches.Rectangle(
                xy=(-4, -4),  # point of origin.
                width=8,
                height=8,
                linewidth=1,
                color='red',
                fill=True
            )
        )
        ax.plot((xval), (yval), 'o', color='y')
        plt.plot(xval, yval)
        plt.grid(linestyle='--')
        plt.title('Square with width 5', fontsize=8)
        # plt.savefig("plot_circle_matplotlib_01.png", bbox_inches='tight')
        plt.show()
        return render(request, 'example.html')

    print("=============")
    return render(request, 'example.html')


def aiconcept(request):
    return render(request, 'aiconcepts.html')


def theory(request):
    return render(request, 'theory.html')


def aipipeline(request):
    return render(request, 'aipipeline.html')
