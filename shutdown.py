def shutdown_program():
    shutdown = input("Type 'shutdown' to close the program: ")
    if shutdown.lower() == "shutdown":
        print("Shut Down")
        exit()
    else:
        print("Program continues running.")

shutdown_program()
