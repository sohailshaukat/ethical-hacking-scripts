[[Threat-Modelling]]

##### Steps in Threat Modeling
![[19437_Generic_Steps.jpeg]]
The threat modeling process comprises the generic steps illustrated in the picture above.

The process of researching the search space is iterative and constantly refined by analyzing the feedback from previous iterations.

##### Identify Assets
![[19438_Identify_Assests.jpeg]]
The first step is to understand what's at stake.

-   Identifying tangible assets, like databases or sensitive files is usually easy.
    
-   Understanding the capabilities of an application and valuing them is challenging.
    
-   Less concrete things, such as reputation and goodwill are the most difficult to measure but are often the most critical.
    

##### Create an Architectural Overview
![[19439_Architecture_Overview.jpeg]]
The purpose of this process is to explicate the functions of the application, its architecture, deployment configurations, and the technologies that are part of the solution.

##### In Architectural Overview

The key focus in creating the architectural overview is to find potential vulnerabilities in the design and implementation of the application.

The following are key factors to be considered:

-   Identify the functionality of the application.
-   Draft an architecture diagram.
-   Identify the technologies.

##### Decompose the Application
![[19441_Decompose_Application_2.jpeg]]
The application is broken down with respect to the processes, including all the sub-processes that make up the application.

Drafting a Data Flow Diagram (DFD) simplifies the procedure.

The image above illustrates a simple DFD of a News Feed Service.

> _The more you understand about the mechanics of your application, the easier it is to uncover threats._

##### Decomposing the Application
![[19442_Decompose_Application_1.jpeg]]
_The image above lists the basic steps that help in decomposing the application_

##### Identify the Threats
[Youtube](https://youtu.be/l-CWYwxtHDg)
In this step, the threats that might compromise the integrity of the assets are identified.

The members of the development and test teams are gathered to conduct an informed brainstorming session.

The following tasks are performed in this step.

-   Identifying network threats.
-   Identifying host threats.
-   Identifying application threats.

> Ideally, the team consists of application architects, security professionals, developers, testers, and system administrators.

##### Document the Threats

The anticipated attack technique and countermeasure required needs to be listed for each of the identified threats.

_A template similar to the example below is used in which several target attributes are clearly described._

Threat Description | Attacker obtains authentication credentials by monitoring the network
---|---
Threat target |Web application user authentication process
Risk | **`High`**
Attack techniques | Use of network monitoring software
Countermeasures | Use SSL to provide encrypted channel

##### Rating threats

Threats can be rated using a standard method called **DREAD**.

It takes into account the following items:

-   **Damage potential** (How much are the assets affected?)
-   **Reproducibility** (How easily the attack can be reproduced?)
-   **Exploitability** (How easily the attack can be launched?)
-   **Affected users** (What’s the number of affected users?)
-   **Discoverability** (How easily the vulnerability can be found?)

The threats are rated by answering the above questions and assigning values for every item (high, medium, low).

[Click here](https://resources.infosecinstitute.com/qualitative-risk-analysis-dread-model/#gref) to learn more about DREAD.

##### Rate the Threats

In the final step of the process, the threats are rated based on the risks they pose.

This aids in addressing the threats that present higher risks first, and then resolve the other threats.

> It may not be economically viable to address all of the identified threats, some of them may even be ignored because the chance of them occurring is small and the damage that would result if they did is minimal.

```
Risk = Probability * Damage Potential
```

The formula above helps in determining risk which in turn indicates the consequences to a system if an attack were to occur.

##### Generating a Work Item Report

A more formalized work item report can be created from the initial threat model that can include additional attributes.

In this step, each of the threats that were rated is prioritized and fixed. Then the threat modeling process is restarted.

Threat Description | Attacker obtains authentication credentials by monitoring the network
---|---
Attack Techniques | Use of network monitoring software
Counter Measures | Use SSL to provide encrypted channel
Status | **`SSL Implemented`**

##### The Output
![[19449_output.jpeg]]

The output of the threat modeling process is a document that may be used by the different members of a project team.

It helps to gain a clear picture of the threats that need to be addressed and how to address them.

Threat models consist of a definition of the architecture of the application and a list of threats for the application scenario.