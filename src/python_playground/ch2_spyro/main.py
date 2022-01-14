import turtle
from argparse import ArgumentParser
from datetime import datetime

from PIL import Image

from python_playground.ch2_spyro.animator import SpiroAnimator
from python_playground.ch2_spyro.spyro import Spiro


def saveDrawing():
    turtle.hideturtle()
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = f"spiro-{dateStr}"
    print(f"saving drawing to {fileName}.eps/png")
    canvas = turtle.getcanvas()
    canvas.postscript(file=f"{fileName}.eps")
    img = Image.open(f"{fileName}.eps")
    img.save(f"{fileName}.png", "png")
    turtle.showturtle()


def main():
    print("generating spirograph...")
    descStr = """This program draws Spirographs using the Turtle module. When run wtih no arguments, this
    program draws random Spirographs.

    Terminology:

    R: radius of outer circle
    r: radius of inner circle
    l: ratio of hole distance to r
    """
    parser = ArgumentParser(description=descStr)
    parser.add_argument(
        "--sparams", nargs=3, dest="sparams", required=False, help="The three arguments in sparams: R, r, l"
    )
    args = parser.parse_args()

    turtle.setup(width=0.8)
    turtle.shape("turtle")
    turtle.title("Spirographs!")
    turtle.onkey(saveDrawing, "s")
    turtle.listen()
    turtle.hideturtle()

    if args.sparams:
        params = [float(x) for x in args.sparams]
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        spiroAnim = SpiroAnimator(2)
        turtle.onkey(spiroAnim.toggleTurtles, "t")
        turtle.onkey(spiroAnim.restart, "space")

    turtle.mainloop()


if __name__ == "__main__":
    main()
