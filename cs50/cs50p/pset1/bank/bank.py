Greeting = input ("Greeting: ").strip().lower()
match Greeting :
    case "hello" | "hello, newman" :
        print ("$0", end='')
    case "hey" | "how you doing?" :
        print ("$20", end='')
    case _:
        print ("$100", end='')






