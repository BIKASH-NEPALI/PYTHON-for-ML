numbers=(1,2,3,4,5,6,7,8,9,10)
found=int(input("Enter elements to found"))
index=0
for numbers in numbers:
    if(found==numbers):
        print("elements if found at index", index)
    index+=1