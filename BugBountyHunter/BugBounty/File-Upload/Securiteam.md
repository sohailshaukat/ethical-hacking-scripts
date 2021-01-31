# File upload security recommendations

In my security career, I have always found file upload module to be one of the most favorite playground for hackers. There are many detailed documents mentioning the guidelines for following secure upload mechanism. Going through them will surely give you a sense of high level of insecurity in file upload module.

So jotted down points which I would take care or recommend for secure uploads.

**Proper file type checks:** Check for atleast basic parameters like filesize, mime-type etc and allow only a selected MIME type wherever possible. Make a white-list of file extensions to be allowed for upload. Try to keep away from executable files and scripts where possible. Set minimum and maximum file size for upload. This will prevent Dosing the webserver by uploading huge files and exhaust the storage space.  
**Random filenames and folder**: Do not allow user input to specify the destination directory or file name of uploaded documents. Good practice is to rename the document to some random value and track them in your Database. In short guessing the name of the uploaded file should be made difficult for the attacker.

**Upload Directory Security:** Upload all files outside your web directory. Possibly separate the upload directory from application and system directories/drive. This can help mitigate issues related to resource exhaustion & directory traversal. Set proper folder permissions (chroot() ). Do not allow user to choose the upload folder. Avoid giving writable permissions to users. Instead webserver like apache can be given writable permissions while preventing users from RWX access on the upload folder.

Prevent users from directly accessing the files in the upload directory. Files can directly be stored on the server or other alternative would be to store the files as blobs in database instead. However blobbing for very large files can affect DB performance and also the malicious data if uploaded will be directly saved in database without validating.

Neutering the file like renaming it to some random value or XORing or compressing the file in some way so that the OS doesn’t interpret it as executable etc. will help increase the security barrier.

**Anti Virus Scan:** Scan the upload files for any virus or malicious content. You can even try out ModSecurity which has a feature for inspecting files on upload, which you can combine with some antivirus. The advantage is that you get to block the HTTP request before the file even gets into your system. Alternatively files can also be scanned immediately just after it is uploaded. Both are affective in their own way and can be adapted accordingly depending on their implementation challenges. Other content filtering techniques include icap or CVP which are worth a thought.

**File name Validation:** While allowing users to upload the files, we allow them to specify the name the files should be referred to. Application should validate these file names for any XSS attacks.

**Uploading and saving uploaded sensitive documents in encrypted form:** Sensitive data needs to be uploaded via SSL and saved on the server in encrypted form to protect against eavesdropping. The file can also be encrypted while uploading instead of doing so while saving on the server. There are different products which can help you do this like AspEncrypt etc.

**Page tokens:** Use unique tokens for upload forms. This can help mitigate the less known Cross-site File Upload Attacks. Thus the attacker cannot upload malicious or illegal content on victim’s account. And if the victim is a web-admin, attacker can help himself upload any malicious file to the directories which is otherwise restricted to other users.

**Error page:** Do not reveal too much info in the error page like the directory path etc which can help attacker in further attack. Use customized error page.

**Proper verb:** HTTP POST verb is preferred over HTTP PUT or GET verb as it is comparatively more secure.

**ACL:** Limit “upload module” access to required users or groups wherever possible.

**Logging user activities:** Log all activities of the user like in this case, IP of user, size of the file, directory to which file was uploaded etc. This is help us know if any attacks were made against your server and if they were successful.