##### Threat Modeling Processes

Usually, threat modeling processes start with creating a visual representation of the application and infrastructure being analyzed.

The application/infrastructure is broken down into various components to enhance the analysis.

Once completed, the visual representation can be used to identify and enumerate potential threats efficiently.

Threat modeling methodologies usually use two types of diagrams for visualization:

-   **Data Flow Diagrams (DFDs)**
-   **Process Flow Diagrams (PFDs)**

##### Data Flow Diagrams

Data Flow Diagrams (DFD) is the **visual representation technique** used by threat modeling methodologies like STRIDE, PASTA, and Trike.

DFDs were developed in the 1970s as a tool to illustrate the **details of the** **data flow process** in an application, data storage, and manipulation by the infrastructure upon which the application runs.

Traditionally, DFDs utilize only four symbols:

-   **Data flows**
-   **Data stores**
-   **Processes**
-   **External entities**

At the beginning of the 2000s, an extra symbol, **trust boundaries**, was added to allow DFDs to be exploited for threat modeling.

##### DFD Example

![[19465_dfd_example.jpeg]]

The image above illustrates a simple DFD drawn for a College Library application.

DFDs can be expressed at different levels. Level 0, also known as **context diagram** gives an overview of the application and the higher levels detail out the processes of the application.

##### DFD in Threat Modeling

Once the application-infrastructure system is expressed concerning the five elements, security experts analyze each identified threat entry point against all known threat categories.

Once the potential threats are enumerated, further steps for mitigation and analysis may be carried out.

##### Shortcomings of DFDs

DFD based threat modeling practices face the following shortcomings:

-   DFDs cannot represent the design and flow of an application accurately.
-   DFDs are not efficient in illustrating how users interact and traverse through the features of an application.
-   Data flow diagrams are found to be vague, complex, and harder to comprehend.
-   There is no standard approach to DFD based threat modeling - different threat models with contradicting outputs can be generated for the same application.
-   DFD based threat models are more effective in the analysis of high-level system issues.

##### Process Flow Diagrams (PFDs)

The VAST methodology creates a distinction between Application Threat Models (ATM) and Operational or Infrastructure Threat Models (OTM).

Application Threat Models are built with **Process Flow Diagrams**.

PFD was developed in 2011 as a tool to let Agile software development teams to develop threat models on the basis of application design process.

-   Applications are decomposed on the basis of the **component features or use cases**.
-   Each feature is enumerated in terms of the **core building blocks** required to construct that feature.
-   Features are then linked by **communication protocols**.

> The resulting visualization known as a map of how a user navigates through the various features of an application.

##### Process Flow Diagram: ATM

![[19469_PFD_ATM.jpeg]]

##### Threat Modeling Using PFDs

Process Flow Diagrams provide visualization in the **viewpoint of an attacker**.

Generally, attackers are more concerned with sorting out ways to move through the application use-cases rather than on data flows.

> _The prime intention is to exploit simple use cases to gain access to assets._

---

Hence the tool used to analyze such threats must help in recreating a similar thought process.

Such a design helps in deriving a more practical abuse-case analysis as well as makes the outcomes more appealing and viable to the development team.

##### Threat Model Diagram: OTM

![[19471_PFD_OTM.jpeg]]

OTMs are made up of end-to-end data flow diagrams that resemble traditional DFDs.

End to end data flow diagrams break down an application into its different independent, grouped, and shared components.

Each component is explained in terms of specific attributes.

Components are then connected by communication pathways and protocols.