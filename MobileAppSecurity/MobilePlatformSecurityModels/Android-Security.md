[[Mobile-Platforms]]
[Youtube](https://youtu.be/HAYk7fVaMGM)
# Android Security
![[Pasted image 20201222010337.png]]

To address security issues, the Android platform implements a **permission-based security model.**

The model is based on **application isolation** in a **sandbox environment.**

- This means that each application executes in its environment and is unable to influence or modify execution of any other application.

	**Application sandboxing** is performed at the **Linux kernel level.**

Android exploits the standard Linux access control mechanisms to achieve isolation.

Moreover, **SQLCipher**, an SQLite extension that provides transparent 256-bit AES encryption of database files can be used for full database encryption.

Though the isolation model facilitates a secure environment for executing the applications, the restrictions enforced by the model could also degrade the overall application functionality.

To lift the restrictions imposed by the isolation model, two mechanisms were introduced by Android: **Shared user Id** and **permissions**