


"""


Python Forensics - Indicators of Compromise
Advertisements
 Previous Page Next Page  
Indicators of Compromise (IOC) is defined as "pieces of forensic data, which includes data found in system log entries or files, that identify potentially malicious activity on a system or network."

By monitoring for IOC, organizations can detect attacks and act quickly to prevent such breaches from occurring or limit damages by stopping attacks in earlier stages.

There are some use-cases, which allow querying the forensic artifacts such as −

Looking for a specific file by MD5
Searching for a specific entity, which is actually stored in the memory
Specific entry or set of entries, which is stored in Windows registry
The combination of all the above provides better results in searching artifacts. As mentioned above, Windows registry gives a perfect platform in generating and maintaining IOC, which directly helps in computational forensics.

Methodology
Look for the locations in the file system and specifically for now into Windows registry.

Search for the set of artifacts, which have been designed by forensic tools.

Look for the signs of any adverse activities.

Investigative Life Cycle
Investigative Life Cycle follows IOC and it searches for specific entries in a registry.

Stage 1: Initial Evidence − Evidence of the compromise is detected either on a host or on the network. The responders will investigate and identify the exact solution, which is a concrete forensic indicator.

Stage 2: Create IOCs for Host & Network − Following the data collected, the IOC is created, which is easily possible with Windows registry. The flexibility of OpenIOC gives limitless number of permutations on how an Indicator can be crafted.

Stage 3: Deploy IOCs in the Enterprise − Once the specified IOC has been created, the investigator will deploy these technologies with the help of API in Windows registers.

Stage 4: Identification of Suspects − The deployment of IOC helps in the identification of suspects in a normal way. Even additional systems will be identified.

Stage 5: Collect and Analyze Evidence − Evidences against the suspects are gathered and analyzed accordingly.

Stage 6: Refine & Create New IOCs − The investigative team can create new IOCs based of their evidences and data found in the enterprise and additional intelligence, and continue to refine their cycle.

The following illustration shows the phases of Investigative Life Cycle −

"""
