# { vue : learning notes } 
#### ( started : 20171020 )
————————————


### Resources
---------

#### official resources
————————————

** intro pages ** official /
https://vuejs.org/v2/guide/installation.html

** resources page ** (official)(excellent) / 
https://github.com/vuejs/awesome-vue


#### other resources
————————————

##### Vue for people who know just enough jQuery to get by (2017-april)
https://medium.freecodecamp.org/vue-js-introduction-for-people-who-know-just-enough-jquery-to-get-by-eab5aa193d77

##### Vue.js 2 Quickstart Tutorial 2017 ( 2017 : january )
Very quick hellow world tutorial 
https://medium.com/codingthesmartway-com-blog/vue-js-2-quickstart-tutorial-2017-246195cfbdd2




### Basics
---------


#### Hellow world - simplest Vue : 

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
        <head>
            <script src="https://unpkg.com/vue"></script>
        </head>
        <body>

            <div id="app">
                <div id="app">
                    {{ message }}
                </div>
            </div>
            
            <script type="text/javascript">

                var app = new Vue({
                    el: '#app',
                    data: {
                        message: "hellow world!"
                    }
                })

            </script>
        </body>
    </html>

** update message : **

    app.message = "something else"

###########




#### Directives
————————————

Provide various reactive behviours to the rendered DOM elements. 
They begin with **v-** something, eg **v-bind** as below.

##### // v-bind
Keeps the relevant attribute bound to the data, such that if the data changes, so does the dom element.

    <!-- change the title, according to the message variable -->
    <div id="app-2">
      <span v-bind:title="message">
        Hover your mouse over me for a few seconds
        to see my dynamically bound title!
      </span>
    </div>

    <!-- as above, though it also works with style -->
    <div id="app_3">
      <span v-bind:style="color_message" >
        lorem ipsum lorem something maybe change with some colour
      </span>
    </div>


##### // Conditionals and Loops
————————————

** v-if ** and ** v-for ** can be used for conditionals and loops. 

eg. 

##### // v-if 

    // if : html
    <div id="app_if">
        <span v-if="seen"> Now you see me</span>
    </div>
    
    // if : js
    var app_if = new Vue({
        el="#app_if"
        data: {
            seen: true
        }
    })


** LOOPS! ! **

##### // v-for

# html
    <div id="app-4">
      <ol>
        <li v-for="todo in todos">
          {{ todo.text }}
        </li>
      </ol>
    </div>
# js
    var app4 = new Vue({
      el: '#app-4',
      data: {
        todos: [
          { text: 'Learn JavaScript' },
          { text: 'Learn Vue' },
          { text: 'Build something awesome' }
        ]
      }
    })


##### // Handling User Input 
————————————

// eg use a button and attach a method
// - press button, trigger method, which updates data, which is then updated 
//      in the dom objects

# html
    <div id="app-5">
      <p>{{ message }}</p>
      <button v-on:click="reverseMessage">Reverse Message</button>
    </div>
# js
    var app5 = new Vue({
      el: '#app-5',
      data: {
        message: 'Hello Vue.js!'
      },
      methods: {
        reverseMessage: function () {
          this.message = this.message.split('').reverse().join('')
        }
      }
    })


// interaction can also be two-way … 
// 

# html
    <div id="app-6">
      <p>{{ message }}</p>
      <input v-model="message">
    </div>
# js
    var app6 = new Vue({
      el: '#app-6',
      data: {
        message: 'Hello Vue!'
      }
    })



##### // Composing with Components - making components 
————————————

// eg use a button and attach a method
// - press button, trigger method, which updates data, which is then updated 
//      in the dom objects





### Various basics
---------


##### observation : 

having two Vue apps can create a bit of a conflict… 

