# Why File Upload Forms are a Major Security Threat

Allowing file uploads by end users, especially if done without a full understanding of the risks associated with it, is akin to opening the floodgates for server compromise. Naturally, despite the security concerns surrounding the ability for end-users to upload files, it is an increasingly common requirement in modern web applications.

File uploads carry a significant risk that not many are aware of, or how to mitigate against abuses. Worst still, several web applications contain insecure, unrestricted file upload mechanisms. This article will present eight common flawed methods of securing upload forms, and how easily an attacker could bypass such defenses.

## No Validation

A simple file upload form typically consists of an HTML form which is presented to the client and a server-side script that processes the file being uploaded. The following example contains such an HTML form and a server-side script written in PHP.

```
<form enctype="multipart/form-data" action="uploader.php" method="POST">
  <input type="hidden" name="MAX_FILE_SIZE" value="100000" />
  Choose a file to upload:
  <input name="uploadedfile" type="file" />
  <input type="submit" value="Upload File" /> 
</form>
<?php 
  $target_path = "uploads/";
  $target_path = $target_path . basename($_FILES['uploadedfile']['name']);
  if (move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
    echo "The file " . basename($_FILES['uploadedfile']['name']) . " has been uploaded"; 
  } else {
    echo "There was an error uploading the file, please try again"; 
  }
?>
```

When the PHP interpreter receives an `HTTP POST` method request of the `multipart/form-data` encoding type, the script will create a temporary file with a random name in a temporary directory on the server, for example, _/var/tmp/php6yXOVs_. The PHP interpreter will also populate the global array `$_FILES` with the information about the uploaded file as follows.

-   `$_FILES['uploadedfile']['name']`: The original name of the file on the client machine
-   `$_FILES['uploadedfile']['type']`: The mime type of the file
-   `$_FILES['uploadedfile']['size']`: The size of the file in bytes
-   `$_FILES['uploadedfile']['tmp_name']`: The temporary filename in which the uploaded file was stored on the server

The `move_uploaded_file()` PHP function will move the temporary file to a location provided by the user. In this case, the destination is below the server root. Therefore the files can be accessed using a URL such as _http://www.example.com/uploads/uploadedfile.txt_.

In this simple example, no restrictions are imposed by the server-side script on what file types are allowed to be uploaded to the server. To such an extent, an attacker could easily upload a malicious PHP that could lead to server compromise.

## MIME-type Validation

A common mistake made when securing file upload forms is to only check the MIME-type returned by the application runtime. For example, with PHP, when a file is uploaded to the server, PHP will set the variable `$_FILES['uploadedfile']['type']` to the MIME-type provided by the web client.

Since an attacker could easily control the MIME-type by sending the server a crafted `HTTP POST` request, such validation is trivial for an attacker to bypass. To such an extent, an attacker could easily upload a malicious PHP file with an allowed MIME-type that could lead to server compromise.

## Blacklisting File Extensions

Another weak validation method that is widely used in file upload forms is to use a blacklist of types of files that have dangerous extensions. Upload forms using this mechanism would check the extension of the file that is being uploaded and compare its file extension to a list of extensions that the application considers harmful.

While this could be somewhat effective against some file types, the choice of employing a blacklist is a poor one since practically impossible to compile a list of all possible file extensions that an attacker could abuse use, especially if the application is running within an environment that allows a large number of scripting languages, such as Perl, Python, Ruby, and others – the list is endless. For example, the attacker may change the letters in the extension to their capital forms (_.phP_, _.PhP_, _.pHP_). A whitelisting approach in this use case is by far more effective.

One possible way an attacker could bypass a file extension blacklist on an Apache HTTP Server is to first upload an _.htaccess_ file with the following contents.

```
AddType application/x-httpd-php .jpg
```

The above configuration would instruct the Apache HTTP Server to execute JPEG images as though they were PHP scripts. An attacker would then proceed to upload a file with a _.jpg_ extension (a file extension that is presumably allowed), which would contain PHP code instead of an image and this would allow for code execution.

The screenshot below shows an HTTP request to a JPEG file that contains PHP code that invokes the `phpinfo()` function.

![Upload Form files](https://www.acunetix.com/wp-content/uploads/2012/10/image2-1.png)

## Double Extensions

Another concept for bypassing file upload validation is for an attacker to abuse double extensions where an application extracts file extensions by looking for the `.` character in the filename, and extracting the string after the dot character. The method used to bypass this approach is similar to the method used to bypass a file extension blacklist.

It’s important to first understand how the target web server handles files with multiple extensions. In this example, it shall be assumed that the target server is the Apache HTTP Server. The following is a quotation of the Apache HTTP Server documentation regarding files with multiple extensions.

> Files can have more than one extension, and the order of the extensions is normally irrelevant. For example, if the file _welcome.html.fr_ maps onto content type `text/html` and language French then the file _welcome.fr.html_ will map onto exactly the same information. If more than one extension is given which maps onto the same type of meta-information, then the one to the right will be used, except for languages and content encodings. For example, if _.gif_ maps to the MIME-type `image/gif` and _.html_ maps to the MIME-type `text/html`, then the file _welcome.gif.html_ will be associated with the MIME-type `text/html`.

Therefore, a file named _index.php.123_ will be interpreted as a PHP file by the Apache HTTP Server and it will be executed. This, of course, will only work if the last extension (in this case _.123_) is not specified in the list of MIME-types known to the web server. This lesser-known feature of the Apache HTTP Server could be very dangerous for a number of reasons. Knowing this, an attacker could upload a file containing malicious code (such as a web shell) and bypass the file upload form validation.

A far better approach to securing file upload forms is to employ a whitelisting approach. With this approach, only files that match a known and accepted file extension are allowed. However, in some cases, this approach will not work as expected. For example, when the Apache HTTP Server is configured to execute PHP code, there are two ways one can specify this: using the `AddHandler` directive or using the `AddType` directive. If the `AddHandler` directive is used, all filenames containing the _.php_ extension (_.php_, _.php.jpg_) will be executed as PHP scripts. Therefore, if an Apache HTTP Server configuration file contains the following, it may be vulnerable:

```
AddHandler php5-script .php
```

On an Apache HTTP Server with the above configuration, an attacker can upload a file named _filename.php.jpg_, bypass the validation, and execute code.

## Checking the Image Header

When image upload only is allowed, most web applications usually validate the image header by using a server-side function such as `getimagesize()` in PHP. When called, this function will return the size of an image. If the file is not a valid image, meaning that the file header is not that of an image, the function will return `FALSE`. Therefore, several web applications typically check if the function returns `TRUE` or `FALSE` and validate the uploaded file using this information.

If an attacker attempts to upload a simple PHP shell embedded in a JPEG file, the function will return false, effectively stopping the attack. However, even this approach can be easily bypassed if the Apache HTTP Server is using the `AddHandler` directive described above. If an image file is opened in an image editor, such as GIMP, one can edit the image metadata to include a comment. An attacker would insert some PHP code here as shown below.

![](https://www.acunetix.com/wp-content/uploads/2012/10/image1-1.png)

The image will still have a valid header; therefore it bypasses the `getimagesize()` check. As seen in the screenshot below, the PHP code inserted in the image comments still gets executed when the image is requested by a browser.

![](https://www.acunetix.com/wp-content/uploads/2012/10/image3.png)

## Protecting the Upload Folder with .htaccess

Another common method used to secure file upload forms is to restrict execution of scripts in an upload directory using _.htaccess_ configuration that would typically contain the following:

```
AddHandler cgi-script .php .php3 .php4 .phtml .pl .py .jsp .asp .htm .shtml .sh .cgi Options –ExecCGI
```

The above is another type of blacklist approach, which in itself is not very secure. Furthermore, as warned in the PHP documentation, the `move_uploaded_file()` function will overwrite any file if the destination file already exists. Because uploaded files can and will overwrite the existing ones, an attacker could easily replace an existing _.htaccess_ file with a modified one. This will allows execution of specific scripts which can help compromise a server.

## Client-Side Validation

Another common security measure in file upload forms is client-side validation of files to be uploaded. Typically, such an approach is more common in ASP.NET applications, since ASP.NET offers easy-to-use validation controls.

These types of validation controls allow an application to do regular-expression checks upon the file that is being uploaded, to check that the extension of the file being uploaded is specified in the list of allowed extensions. Below is a sample code taken from Microsoft’s website.

```
<asp:FileUpload ID="FileUpload1" runat="server" /><br /> 
<br /> 
<asp:Button ID="Button1" runat="server" OnClick="Button1_Click" 
Text="Upload File" /> <br /> 
<br /> 
<asp:Label ID="Label1" runat="server"></asp:Label> 
<asp:RegularExpressionValidator 
id="RegularExpressionValidator1" runat="server" 
ErrorMessage="Only mp3, m3u or mpeg files are allowed!" 
ValidationExpression="^(([a-zA-Z]:)|(\\{2}\w+)\$?)(\\(\w[\w].*)) 
+(.mp3|.MP3|.mpeg|.MPEG|.m3u|.M3U)$" 
ControlToValidate="FileUpload1"></asp:RegularExpressionValidator> 
<br /> 
<asp:RequiredFieldValidator 
id="RequiredFieldValidator1" runat="server"
ErrorMessage="This is a required field!" 
ControlToValidate="FileUpload1"></asp:RequiredFieldValidator>
```

This ASP.NET code uses validation controls, so the end-user is only allowed to upload _.mp3_, _.mpeg_ or _.m3u_ files to the web server. If the file type does not match any of the specified extensions, the validation control throws an exception and the file won’t be uploaded.

Since this type of validation is done on the client side, a malicious user can easily bypass it. It is possible to write a short client-side script that will do the validation instead of the script provided by the web application. Without using a web browser, the attacker can send `HTTP POST` requests to the application in order to bypass the client side validation and upload a malicious file.

## Suggested Solution

The following is a list of best practices that should be enforced when file uploads are allowed on websites and web applications. These practices will help avoid file upload vulnerabilities in web applications that are served using Apache HTTP Server, however similar rules could easily be applied to other servers both on Linux and Windows.

-   Define an _.htaccess_ file that will only allow access to files with allowed extensions.
-   Do not place the _.htaccess_ file in the same directory where the uploaded files will be stored, instead, place it in the parent directory. This way the _.htaccess_ file can never be overwritten by an attacker.
-   A typical _.htaccess_ which allows only GIF, JPG, JPEG, and PNG files should include the following (this should be adapted as necessary for specific requirements). The following will also prevent double extension attacks:
    
    ```
    deny from all <
    files ~ “^w+.(gif|jpe?g|png)$”> 
    order deny,allow
    allow from all 
    </files>
    ```
    
-   If possible, upload the files in a directory outside the server root.
-   Prevent overwriting of existing files (to prevent the _.htaccess_ overwrite attack).
-   Create a whitelist of accepted MIME-types (map extensions from these MIME-types).
-   Generate a random file name and add the previously generated extension.
-   Don’t rely on client-side validation only, since it is not enough. Ideally, both server-side and client-side validation should be implemented.