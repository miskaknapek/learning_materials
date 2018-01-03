# { notes javascript & notes }
#####( started 20171020 )
--------------


### resources
---------




### General javascript
————————————

#### Datatypes
————————————

##### self. vs this.

**Self** really refers to **Window.self** .
If one's variables function in a global context, they're in fact in the context of .self . 

eg. invoked in a global context : 

    function foo() {
        console.log(
            window.self === window, // is self window?
            window.self === this,   // is self this?
            this === window         // is this window?
        );
    }
    foo(); // true true true

but… if one invokes things in a local context … this won't be the same as window.self

    // invoke foo with context {}
    foo.call({}); // true false false




### ES6
----------

#### Modules
————————————

##### // Overview - extensive
https://medium.freecodecamp.org/javascript-modules-a-beginner-s-guide-783f7d7a5fcc
###### short description : 
https://spring.io/understanding/javascript-modules
###### also : 
http://exploringjs.com/es6/ch_modules.html
###### node js modules 
https://www.w3schools.com/nodejs/nodejs_modules.asp

Modules are holders of javascript components. 
One file per module/component. 
    Claimed this helps maintainability ( < lols, hence the need for webpack :-) 
Also helps with namespacing, and reuse.
    Guess the modules can be namespaced easier.


#### Import
————————————

###### //  Mozilla documentation 
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import

###### //  other developer overview : more extensive than mozilla info 
http://2ality.com/2014/09/es6-modules-final.html

The import statement is used to **import bindings** which are exported by another module.
The bindings can be files or other code module holders ( eg in loaded libraries ).

> note : 
"This feature is only just beginning to be implemented in browsers natively at this time. It is implemented in many transpilers, such as TypeScript and Babel, and bundlers such as Rollup and Webpack."
- What's it about? 
>


#### Prototypical inheritence 
————————————

###### //  Mozilla documentation - short
https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/Inheritance
###### //  Mozilla documentation - long
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain






#### HTTP Methods - GET & POST 
----------

Client server messaging btw Web client and Server : - GET & POST 
// HTTP was designed to enable communications between clients and servers; 

##### - GET : Requests data from specific resoruce
##### - POST : Submits **data** to be processed, to a specific resource 

##### Other HTTP Request Methods : 
HEAD : Same as GET but only returns HTTP headers and no body data
PUT : Uploads a represneation of a specific URI
DELTE : Deletes specific resource
OPTIONS : Returns the HTTP methods the server supports
CONNECT : Converst the requested connection to a transparent TCP/IP Tunnel



#### [ GET]  : Requests data from specific resoruce
————————————

eg : 

         /test/demo_form.php?name1=value1&name2=value2


¿ What can one do with GET requests? 
- GET results are cached!
- GET requests are possible to bookmark. 
- DON'T use GET requests with sensitive data.
- GET requests are limited in length. 
- GET requests should only really be used to retrieve data.


#### [ POSTS]  : Submits **data** to be processed, to a specific resource 
||      - eg input form values
————————————

eg. input form values can be sent using POST : 

        POST /test/demo_form.php HTTP/1.1
        Host: w3schools.com
        name1=value1&name2=value2


¿ What can one do with POST requests ? 
- POST requests don't cache
- POST requests can't be bookmarked! 
- POST requests don't have a restriction on length
- BINARY data can also be used in POST requests

#### - - jQuery.POST method! 
( for some POST stuff to a server! )

##### resource : 
        https://www.w3schools.com/jquery/ajax_post.asp

Syntax : 

    $( selector ).post( URL, data, function( data, status, xhr ), dataType )

//      and in this, the DataTypes : 
    - XML 
    - html
    - text
    - script - runs a response as JS and returns it as plain txt
    - json
    - jsonp - loads a JSON block using JSONP, will add a "?callback=?" to the URL to spcify the callback