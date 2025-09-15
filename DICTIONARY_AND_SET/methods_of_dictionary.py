list1={#duplicate keys are not allowded
    "fruit":"mango",
    "human":"Bikash",
    "planet":"Earth",
    "branch":{"civil":"engineering","bbs":"management", "mbbs":"doctor"}

}
print(list1.keys())
print(list1.values())
print(list1.items())
print(tuple(list1.keys()))
newtupple=tuple(list1.keys())
print(newtupple[0])
print(list1["planet"])
print(list1.get("planet7")) #if does not match error shows
list1.update({"city":"mahendranagar",
              "village":"gulariya"})
print(list1)