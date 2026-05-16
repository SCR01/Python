def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Superman", power="Flight")
print_kwargs(power="Invisibility")
print_kwargs(name="Batman",power="Intelligence",enemy="Joker") # This will raise an error because 'enemy' is not defined in the function parameters.

