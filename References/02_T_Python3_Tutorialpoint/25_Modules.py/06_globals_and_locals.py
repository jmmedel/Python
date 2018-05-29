


"""

he globals() and locals() Functions
The globals() and locals() functions can be used to return the names in the global and local namespaces depending on the location from where they are called.

If locals() is called from within a function, it will return all the names that can be accessed locally from that function.

If globals() is called from within a function, it will return all the names that can be accessed globally from that function.

The return type of both these functions is dictionary. Therefore, names can be extracted using the keys() function.

The reload() Function
When a module is imported into a script, the code in the top-level portion of a module is executed only once.

Therefore, if you want to reexecute the top-level code in a module, you can use the reload() function. The reload() function imports a previously imported module again. The syntax of the reload() function is this −

reload(module_name)
Here, module_name is the name of the module you want to reload and not the string containing the module name. For example, to reload hello module, do the following −

reload(hello)


Packages in Python
A package is a hierarchical file directory structure that defines a single Python application environment that consists of modules and subpackages and sub-subpackages, and so on.

Consider a file Pots.py available in Phone directory. This file has the following line of source code −

"""

def Pots():
    print ("I'm Pots Phone") 



