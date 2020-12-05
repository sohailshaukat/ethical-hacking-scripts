Proxy tab in Burp Suite is

    Mainly used to intercept the request via Burp Suite proxy tool
    Configure the proxy
    Store all the request and response in "HTTP History"
    Manipulating requests


E2E - Workflow of Proxy Tab (Option)

![[Pasted image 20201204183742.png]]

## Step 1:

Once Burp Suite is installed in your machine, the first step towards testing your application is configuring the proxy setup in the tool so that the requests on your web application (to be tested) can be intercepted by Burp Suite.

To do so, open Burp Suite tool and navigate to **Proxy Tab** and check the **SubTab "Option".**

Here, you have to configure the proxy details as same as the browser proxy so that you can capture the request and response. Ex - 127.0.0.1:8080 as shown.

![[Pasted image 20201204183858.png]]

## Step 2:

Let's get into Proxy Tab and look into the SubTab "HTTP history". It captures all the call made via the browser, which was configured with Burp Suite.

You can also look into the request and response of each call by clicking it.

![[Pasted image 20201204184140.png]]

## Step 3:

Let's get into **Proxy Tab** and look into the **SubTab Intercept**. It has an **On** and **Off** feature, that helps to enable / disable interception of the requests.

Please note, when intercept is On, **Forward button** gets enabled, else Forward button is always disabled.

When intercept is **On** a request gets captured in the intercept tab allowing us to intercept / change the request body. It will not hit the server until you click the forward button.

When the intercept is **Off**, the request will not be captured in intercept tab, thus not allowing any request modification. In this case, the request will go to the server directly.


