from classes.Associacao import Pen, Writer, Typewriter

if __name__ == "__main__":
    writer = Writer("victor")
    pen = Pen("Bic")
    typeWriter = Typewriter()

    writer.tool = pen
    writer.tool.writing()


