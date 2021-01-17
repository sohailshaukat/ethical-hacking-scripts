[[Brute-Force-Attack]]
**Passwords - Cornerstone of Computer Security**

Strong, secure passwords are a cornerstone of an effective security strategy. Passwords ensure that only authorized personnel will be able to gain access to a system or network. Unfortunately this is not always the case. Passwords are usually invented and implemented by the individuals who are utilizing the computer or the network. The words, symbols, dates that make up the password usually have some personal meaning to the user so that the he or she can easily remember it. Herein lies the problem. Many users will place priority on convenience over security. As a result, they choose passwords that are relatively simple. While this helps them to recall the password when it comes time to logon - it also makes the password much easier for hackers to crack. Potential hackers will probe your network looking for the weak link that will give them entry. The most notorious and the easiest to exploit is a weak password. The first line of security defence thus becomes one of the weakest.

Part of the responsibility of the system administrator is to ensure that users are aware of the necessity of maintaining viable secure passwords. This entails two aspects: first, to educate users about to the importance of strong passwords and how to implement them; and, secondly, to implement measures that will ensure that users' passwords are adequately effective. To achieve the first objective, user-education is the key. To fulfil the second objective, it is imperative that the system administrator stay one step ahead, discovering weak passwords before the hacker. To do this he/she may use the same tool as a hacker - a password-cracker.

**Password Crackers**

**Word-lists**

As the name implies, a password cracker is a tool that is used to 'crack' or figure out a password. Originating from the "Dark Side," these delightful little tools were developed to give a hacker access to a computer on a network by discovering the user's password. Password crackers use different methods to achieve their objective. Some password crackers use 'word lists', lists of words, phrases or other combinations or letters, numbers and symbols that computer users often use as passwords. They enter word after word, at high speed, until they find the word or combination of symbols that matches the password. Password crackers operate on the theory that eventually, given a sufficient number of combinations and permutations, they will come across the word, phrase or combination of characters that makes up the password. If an entry from the word list matches the password, it is considered cracked.

Once the password is cracked, it could allow the hacker to assume the legitimate users' identity, thereby allowing access to all data that the legitimate user is authorized to view. If this isn't bad enough the hacker may be able to escalate those illegally gained privileges sufficiently to take control of the whole network.

If passwords were stored in plain text, reading them would be easy; as a result, they are encrypted. In order to counter the securing effects of encryption, the password cracker will run the wordlists through the same cryptographic algorithm as the original passwords before comparative analysis until a match is established. In other words, the password-cracker adopts the same cryptographic configuration as the password, and then runs the word lists in comparison to the password.

**Brute-Forcing**

Whereas wordlists rely on speed and guile, a second method of password cracking relies purely on power and repetition, it is called 'brute forcing.' Brute-forcing is a form of password cracking that attempts to crack the password by simply comparing every possible combination and permutation of characters available until it finds a match for the password. As the name implies brute forcing is very powerful and will eventually crack any password; however, is extremely slow because it uses every conceivable character combination. For example, 3-letter password submitted to an alpha-numeric test would change like this:

 aaa, aab, aac... aaA, aaB, aaC... aa0, aa1, aa2, aa3... aba, aca, ada... 

each of the combinations of characters and symbols is fed through the appropriate cryptographic algorithm and compared to the stored password until a match is found.

As you can imagine, brute-forcing is rather ungainly and slow in comparison to using wordlists. However, what it lacks in speed, it makes up for in thoroughness. Brute-forcing ultimately effective because it tries every combination and permutation of characters, even nonsensical combinations that may otherwise evade the order, logic or pragmatic basis of a wordlist. On the other hand, password crackers compare the password against only known combinations of symbols and characters.

**Brute-Force and Wordlist Hybrids**

Some password crackers, such as the [l0pht password cracker](http://www.l0pht.com/l0phtcrack/), also use a hybrid check which mixes the two techniques. This combines the best of both methods and is considered to be highly effective against password where a little imagination has been used in the passwords creation.

**The Importance of Strong Passwords**

A network is only as secure as it's weakest link. With this in mind, easily guessed passwords need to be weeded out before they unlock the door for the wrong person. This is particularly true since the advent of password crackers have made it so much easier for hackers to "guess" passwords. Unfortunately the average user is more inclined to make the password easy to remember than difficult to guess. Education is the key to effective password use. A system administrator must instil the importance of effective passwords in the minds of the system's users. How can he or she accomplish this? Enter the password cracker.

This discussion may have led readers to believe that password crackers could only be used by hackers for criminal purposes. Not true. They can be also be used to ensure that users are implementing secure passwords. Systems administrators can use password crackers to test the strength of user's passwords. The system administrator can then notify users whose passwords are insecure. Some password crackers can also issue an e-mail advising users to change their password immediately if it was too easily or too quickly cracked.

**Systems Administrators and Password Protection**

It should be noted that users are not the only parties guilty of jeopardizing the integrity of password security. Systems administrators may have different standards of password behaviour for themselves than for other users. Because they have a number of passwords to remember, administrators often pick a single, simple password for many applications. This obviously creates a serious weakness in the security chain. Sys-admins also may have the ability to bypass password-enhancing tools, which they may choose to do for the sake of convenience. Couple this with the fact that they can remove reminders to change passwords from their own passwords and you have a serious problem. Finally, sys-admins may often take shortcuts in the installation of software or equipment that will often leave applications with their default passwords. This is such a common occurrence that there are repositories on the Internet with all these default passwords, something initially put in place to assist the administrator, but more likely to help the hacker.

**Improving password quality**

We have referred several times to weak passwords and the threat that they may pose to network security, but what do we mean by weak passwords? Characteristically, they are anything that might occur in a dictionary, which is to say simple, proper words utilizing only letters and no other type of character. For instance, proper names are poor choices for passwords.

Another flawed password is one that relies on personal information about the user, such as birthdays, anniversaries, spouse's names etc., that will make the password easier to remember. As discomfiting as it may seem, hackers often have access to users' personal information. By using a technique known as social engineering, hackers will use a legitimate user's personal information to make educated guesses of the user's password. By incorporating this information into the password, the hacker has a much better chance of cracking the password. A good hacker will socially engineer the target account, carrying out a little research into your hobbies, interests, date of birth even family members and pets. Selecting obscure words, phrases and symbols should prevent this.

While it is important to create a password that does not consist of orthodox everyday words, but that can be reasonably easily remembered, it is also important to use different characters in the password. Users should try to incorporate letters (both upper and lower case,) numbers and symbols. They can achieve this by mingling characters from the various character sets, which include:

-   uppercase letters such as A, B, C;
-   lowercase letters such as a, b,c;
-   numerals such as 1, 2, 3;
-   special characters such as $, ?, &; and
-   alt characters such as µ, £, Æ.

Strong passwords replace simple letters with other characters so that they form memorable words but don't necessarily form dictionary words. For example, 'Password' may become 'Pa55w0rd'. Unfortunately, this step is already outdated; dictionaries have been already been created to combat this technique. As a result, users have been forced use combinations of 2 or more unrelated words, each of which should consist of characters from each of the five character sets.

**Random Password Generators**

Much faith is put into random password generators that give users a ready-made password. However, due to the random nature of these passwords, they are difficult to remember. Often the first thing a user will do is to write the password down on a sticky note that they then put on their monitor, allowing any and all passers-by to see their 'secret' password. This creates potential problems because it allows unauthorized people to see it. Again, the solution is to create a password that is memorable, but which is not so simple that it can be cracked by a word list. This is somewhat difficult - it challenges both the imagination and the memory - but it is a vital step in computer security.

**Update Passwords Regularly**

In addition to creating passwords that are difficult to crack, it is important to change passwords intermittently. This is necessary in case somebody has cracked your password or is in the process of trying to crack your password, it becomes necessary to change your password. Most users will not remember to do this on their own. As a result, it should be the responsibility of the system administrator to issue reminders to users on a regular basis.

Another option is password-update prompts, these are pop-up boxes that come up on a user's monitor that remind the user to change his or her password. Generally speaking, operating systems that offer password prompts remind the user to change passwords every thirty days. One OS that offers this service is Windows 2000 Professional.

Windows NT4.0 goes one step further than simply offering an update prompt. For this OS, Microsoft offers an easy-to-install tool free of charge (service pack 2+) called passfilt.dll that forces users to use at least 3 of the above character sets in each password, thereby forcing users to choose a secure password. This can be an effective tactic; however, it is important that systems administrators ensure that each and every user is given advance notice of the introduction of this tool and how to use it to generate passwords, otherwise your helpdesk will be inundated with complaints and passfilt will be ineffective.

Sys-admins should also be warned that there is often resistance to its introduction - users often complain that they couldn't possibly remember a complex password. As a compromise, the sys-admin could allow a complex password to be used for a longer period of time before the user receives an update reminder.

**Potential Implications of Password Cracking**

System administrators should be careful how they conduct password cracking. For instance, it may be worth considering carrying out any password cracking offline to avoid any chance of the password cracking session being view by unauthorized parties. Furthermore, password cracking should not be undertaken without the proper authorization of employers. Unless the appropriate notification is given and the required authorization received from the employer, questions could be raised about the credibility and trust of the person conducting the password cracking. Furthermore, fellow employees may interpret password cracking as a violation of their privacy. This could obviously cause serious problems within the workplace.

As well, systems administrators should check to make sure that they are not contravening any local laws when they are conducting password cracking. In cases in which the security of the organization's computers and networks are concerned, it is better to err on the side of caution and obtain the proper clearance prior to engaging in password cracking.

**Passwords and Security Policy**

An undiscovered weak password could make everyone's data vulnerable to compromise. It is imperative that all aspects of password assurance is included in the Security Policy of the organization. The policy should not only stress the absolute importance of strong, secure passwords, and the role of all individual users in maintaining the strength and security of their own passwords, it should also outline the steps that the system administrator is expected to follow in ensuring the security of the system through passwords.

**A Final Word of Password Wisdom**

I remember seeing a great phrase on the Mexican Hackers Emergency Response Team page, which went something like "Passwords are like underwear: don't share them, hide them under your keyboard, or hang them from your monitor. Above all, change them frequently"

A. Cliff has worked with electronic security for nearly 20 years on everything on the transmission side from HF to SHF, both systems work and repair down to component level. He has worked at nearly every level, from mainframes to PCs to networks.He has also worked on various secure telephone exchanges, fibre optic repair, cryptography, etc. In his spare time, he also maintains a list of network security tools, which is available at [http://www.networkintrusion.co.uk](http://www.networkintrusion.co.uk/)