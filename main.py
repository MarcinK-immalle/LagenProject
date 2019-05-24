import BI
import UI

while True:
    a, b = UI.vraag_2_getallen()
    deling, rest = BI.deling_en_rest(a, b)
    print(f"De gehele deling van {a} door {b} is {deling} en heeft als rest {rest}.")
