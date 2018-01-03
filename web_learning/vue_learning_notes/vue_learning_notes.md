# { vue : learning notes } 
#### ( started : 20171020 )
————————————


### Resources
---------


#### jsFiddle 
————————————

https://jsfiddle.net/user/miska/fiddles/


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

// Each Vue component is a Vue instance

// Data is bound to the vue instance, so : 
   // - when the Vue or externally bound data is updated, 
      the Vue data, or exteral data, is updated

   // - when the data is updated, the dom elements ( as needed ) are updated
      too


###### Vue lifecycle 

https://alligator.io/vuejs/component-lifecycle/




###### Instance properties and methods : 
  // note that one can access instantiated methods and properties through 
  //  the properaties and methods, prefaced by a $
  //   - such that one can access the referenced element or data, 
  //      - as well as create watcher methods, that are triggered once 
  //      particular variables are changed

    var data = { a: 1 }
    var vm = new Vue({
      el: '#example',
      data: data
    })
    vm.$data === data // => true
    vm.$el === document.getElementById('example') // => true
    // $watch is an instance method
    vm.$watch('a', function (newValue, oldValue) {
      // This callback will be called when `vm.a` changes
    })

// a more complex example   
  

###### computed values : 
A method that caches a result based on its dependencies, so it's not recalculated every time. 
NOTE : these can also act as watched variables, but with the difference they dont' get re-calculted every time.

Eg: (below) : generating the "reversedMessage" property/data/variable
NOTE : That the "function name" is in fact the name of the 
variable that the computed method calculates. The variable name doesn't need to exist in the data part of the component or Vue instance… 

    // computed property, doesn't update unless one of its dependencies change
    computed: {
      reversedMessage: function () {
        return this.message.split('').reverse().join('')
      }
    }


###### Watched values : 
###### # - as soon as the variable changes, the value is updated… 
https://vuejs.org/v2/guide/computed.html#Watchers

###### # html
    <div id="demo_watched_generated_value">{{ " try changing first/lastName and see this update : "+fullName }}</div>
###### # js
      //  comp
      var vm_watched_computed = new Vue({
        //
        el: "#demo_watched_generated_value",
        data: {
          firstName : "Foo",
          lastName : "Bar",
          fullName : "Foo Bar"
        },
        watch:{
          firstName: function(val){
            this.fullName = val+" "+this.lastName;
          },
          lastName: function(val){
            this.fullName = this.firstName+" "+val;
          }
        }
      });


###### Filters : 
###### # - apply text transformations in the html and code ( v-whatever statements in the DOM tag definitions ). Can be defined in components or globally
https://vuejs.org/v2/guide/filters.html

Methods, within the Vue app, which allow one to apply text trasnformations - such as capitalisation, etc - to text.   
Can also be chained like unix pipes. 
Can also be placed in the DOM tag definitions .

** USAGE : **
eg. 

    <!-- in mustaches -->
    {{ message | capitalize }}
    <!-- in v-bind -->
    <div v-bind:id="rawId | formatId"></div>

can be chained : 

    {{ message | filterA | filterB }}


** IN CODE : **
defined in components :

    filters: {
      capitalize: function (value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
      }
    }

defined globally : 

    Vue.filter('capitalize', function (value) {
      if (!value) return ''
      value = value.toString()
      return value.charAt(0).toUpperCase() + value.slice(1)
    })




###### Computed values : ( lookup )
###### # the variable value is only calculated once ( eg at construction )

###### # html
    <div id="demo_computed_generated_value">{{ "computed fullname : "+fullName }}</div>
###### # js
      //  comp
      var vm_watched_computed = new Vue({
        //
        el: "#demo_computed_generated_value",
        data: {
          firstName : "Foo",
          lastName : "Bar",
          fullName : "Foo Bar"
        },
        computed:{
          fullname: function(){
            return this.first+" "+this.lastName;
          }
        }
      });


###### Computed values : getters & setters
###### # 





###### Constructor : "Created"

    new Vue({
      data: {
        a: 1
      },
      created: function () {
        // `this` points to the vm instance
        console.log('a is: ' + this.a)
      }
    })
    // => "a is: 1"

###### other livecycle hooks :  mounted, updated, and destroyed
related : lifecycle diagram : https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram



###### Render functions : for when templates are too rigid 
_ Allows one to write functions that produce desired dom, rather than producing the DOM using templates infused with Vue code…
 
eg. for variable sized headings 

        // 
        Vue.component('anchored-heading', {
          render: function (createElement) {
            return createElement(
              'h' + this.level,   // tag name
              this.$slots.default // array of children
            )
          },
          props: {
            level: {
              type: Number,
              required: true
            }
          }
        })




### Demos 
----------

#### Hellow world - simplest Vue : 

    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
        <head>
            <script src="https://unpkg.com/vue"></script>
        </head>
        <body>
            <!-- app dom --> 
            <div id="app">
                <div id="app">
                    {{ message }}
                </div>
            </div>
            
            <!-- js --> 
            <script type="text/javascript">
                //
                var app = new Vue({
                    el: '#app',
                    data: {
                        message: "hellow world!"
                    }
                })
                //
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
** Mustaches cannot be used inside HTML attributes, instead use a v-bind directive: **
It also works for boolean attributes - the attribute will be removed if the condition evaluates to a falsy value:

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


###### # various directives : 
/ / / /

// v-text : sets the tetual content of a component : 
// eg : 

    <span v-text='text_var'></span>



##### // Conditionals and Loops
————————————

** v-if ** and ** v-for ** can be used for conditionals and loops. 
(the same applies for v-else v-show )
If the value/function/method attached to v-if/v-else/v-show is true, the relevant element is visible. If the value is false, then the dom element disappears.

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

###### html
    <div id="app-4">
      <ol>
        <li v-for="todo in todos">
          {{ todo.text }}
        </li>
      </ol>
    </div>
###### js
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


##### // Handling User Input  ( v-on & v-bind & v-model )
————————————

// eg use a button and attach a method
// - press button, trigger method, which updates data, which is then updated 
//      in the dom objects

###### html
    <div id="app-5">
      <p>{{ message }}</p>
      <button v-on:click="reverseMessage">Reverse Message</button>
    </div>
###### js
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


// interaction can also be two-way … with ** v-model **
//  ( importantly : v-model allows two way binding of data )

###### html
    <div id="app-6">
      <p>{{ message }}</p>
      <input v-model="message">
    </div>
###### js
    var app6 = new Vue({
      el: '#app-6',
      data: {
        message: 'Hello Vue!'
      }
    })


##### // v-shorthands for v-bind and v-on 

    <!-- full syntax -->
    <a v-bind:href="url"> ... </a>
    <!-- shorthand -->
    <a :href="url"> ... </a>
    v-on Shorthand


    <!-- full syntax -->
    <a v-on:click="doSomething"> ... </a>
    <!-- shorthand -->
    <a @click="doSomething"> ... </a>

##### // Raw HTML : 
————————————

https://vuejs.org/v2/guide/syntax.html#Raw-HTML

The double mustaches interprets the data as plain text, not HTML. In order to output real HTML, you will need to use the v-html directive:

    <div v-html="rawHtml"></div>

The contents of this div will be replaced with the value of the rawHtml property, interpreted as plain HTML - data bindings are ignored.



##### // Using JavaScript Expressions
————————————

https://vuejs.org/v2/guide/syntax.html#Using-JavaScript-Expressions

So far we’ve only been binding to simple property keys in our templates. But Vue.js actually supports the full power of JavaScript expressions inside all data bindings:

    {{ number + 1 }}
    {{ ok ? 'YES' : 'NO' }}
    {{ message.split('').reverse().join('') }}
    <div v-bind:id="'list-' + id"></div>



####  // composing with components - making components 
———————————— <br> 
————————————


##### # RANDOM NOTES 
————————————

##### Note : Component names
Component names should be : all lowercase and with a dash… 


##### # Variables and scope within Vue Apps : 
————————————

  . when calling variables from html : 
  just use the variablename straight up&down, like so : 
        <div v-bind:html="variablename"></div>

  . within App methods ( and other bits ? ) use:
         this.variable_name

  . vue app example of the above ( calling variables from App methods ):

      var app8 = new Vue({
        el: "#app-8",
        data: {
          /* definition suggesting which dataclasses to have on/off */
          class_defintions : { button: true },
          /* another in/active class definiton */
          class_defintions__button_false : { button: false, button_red: true },
          class_switch: true,
        },
        methods: {
          switch_classes: function(){
            console.log("class_switch : "+this.class_switch );
            console.log("current_class : "+this.current_class );
            if( this.class_switch === true ){
              this.current_class = this.class_defintions;
            }else{
              this.current_class = this.class_defintions__button_false;
            }
            //
            // reverse the class switch… 
            this.class_switch = !this.class_switch;
          }
        }
      })



##### # Note : v-bind conventions 
————————————
eg. in this component in the HTML :

    <test_component_htlm_with_prop_02 v-bind:message='random_test_text' v-bind:data_general='random_test_text__data_general__array_of_variables' ></test_component_htlm_with_prop_02>

note : 

    v-bind:message='random_test_text'

  here : 
  - 'message' refers to a property of the component eg:
        Vue.component("test_component_htlm_with_prop_02",{
         props: ['message'],
        template: '<div>Im a hmtl+PROP : ||{{ message}}  </div>'
      })
  - make sure to use '=' for indicating which component prop goes with which vue app variable,  (in the conponent declartion in the html ).
  i.e. in the component declaration v-bind, ":" is for component props and such, while '=' is for external things, like variables being attached to the props



###### # Setting classes with v-bind:class
————————————
- One can pass a {} / associative array to indicate which classes should be on/off
  eg. this would turn on the "button_red" class

      <div v-bind:class="{button_red : true}" >

  eg. one can also pass a variable name which holds a simiar json array

    html :
      <div v-bind:class="class_defintions__button_false" >
    js - vue app : 
      data : {
          class_defintions__button_false : { button: false, button_red: true }
        }

  eg. alternatively, one can pass a variable that points at the current class definition variable : 
    - BUT BUT BUT : you might need to set the current_class variable 
    from code! - looks like it's difficult to initialise it from the Vue app

    hmtl : 
        <div v-bind:class="current_class" >
    js - vue app : 
      data : {
          /* class defintion */*
          class_defintions : { button: true },
          /* variable suggesting which class is in use */
          current_class: this.class_defintions,
    }



###### # Vue instances vs components 
————————————
- Typically you need one Vue app, to hold it all together. 
    - eg : 
      var our_Vue_app = new Vue({
                  el: "body",
                  data: 
                    { ourdata: window.ourdata }
                  construct: … 
                  computed: … 
                  methods: … 
                  et… 
                })
- Once you have a Vue app, you can register components 
    - eg : 
        our_Vue_app.component("component-name", {
          props: ['prop_one', 'prop_two' ],
          template: "<div> prop one : {{prop_one}}, prop_two: {{prop_two}}</div>"
      });



###### # Declaring a new component … with a prop
————————————

###### # Note the name of the prop… regardless of the original variable name sent to the component, inside the component, as below, the prop/variable name listed here, in the "props", is the one that's valid and usable. 
Note 2 : the ".text" 'subdomain' of the variable ( todo.text ) relates to the subdomain in the main data, in the main Vue app ( app7 ).

    Vue.component('todo-item', {
      // The todo-item component now accepts a
      // "prop", which is like a custom attribute.
      // This prop is called todo.
      props: ['todo'],
      template: '<li>{{ todo.text }}</li>'
    })

// Vue app with data … 
    - note data

    var app7 = new Vue({
      el: '#app-7',
      data: {
        groceryList: [
          { id: 0, text: 'Vegetables' },
          { id: 1, text: 'Cheese' },
          { id: 2, text: 'Whatever else humans are supposed to eat' }
        ]
      }
    })


###### # Passing a property to a component, in html 
————————————

Note : the "v-bind" text binds/connects the data from the app7 ( main Vue app just above ), to the component, specifying the variable name in the compmonent to attach to, and the data name in the "super" the data originally 'came from.'
Note2 : one can also pass literal aparameters, or more general/indiviudal data parameters.

    <div id="app-7">
      <ol>
        <!--
          Now we provide each todo-item with the todo object
          it's representing, so that its content can be dynamic.
          We also need to provide each component with a "key",
          which will be explained later.
        -->
        <todo-item
          v-for="item in groceryList"
          v-bind:todo="item"
          v-bind:key="item.id">
        </todo-item>
      </ol>
    </div>




##### // Component Computed properties
————————————

Like methods, but the property is computed and cached, for faster retrieval


    <div id="example">
      <p>Original message: "{{ message }}"</p>
      <p>Computed reversed message: "{{ reversedMessage }}"</p>
    </div>

    var vm = new Vue({
      el: '#example',
      data: {
        message: 'Hello'
      },
      computed: {
        // a computed getter
        reversedMessage: function () {
          // `this` points to the vm instance
          return this.message.split('').reverse().join('')
        }
      }
    })


##### // Component communication 
————————————

Data is passed from parent to child via **props**,
Data passed from childr to parent happens via **events**


##### // NOTE : Local values 
  - YOU MIGHT WANT TO COPY THE INITIAL VALUE OF A GLOBAL VALUE, IF YOU WANT A LOCALISED VALUE, RATHER THAN CONSTANTLY SUBSCRIBING TO THE GLOBAL VALUE! EG DO THIS TO MAKE A LOCAL INSTANTIATION OF A VALUE : 

        props: ['initialCounter'],
        data: function () {
          return { counter: this.initialCounter }
        }



##### // Component methods
————————————

###### #

Like methods, but the property is computed and cached, for faster retrieval

###### # html
    <p>Reversed message: "{{ reverseMessage() }}"</p>
###### # js
    // in component
    methods: {
      reverseMessage: function () {
        return this.message.split('').reverse().join('')
      }
    }



##### // References
————————————

… Allows one to reference a DOM element from javascript code. 

eg. this in dom 

    <input ref="photoUpload" @change="handlePhotoUpload" type="file" class="hide">

can be accessed through this in JS

    this.$refs.photoUpload


##### // Handlers
————————————

Vue can listen to events usng the @ prefix - eg. @change @click 

eg. 

    <input ref="photoUpload" @change="handlePhotoUpload" type="file" class="hide">


##### // vm.$emit
————————————

vm.$emit( event, […args] )

Trigger an event on the current instance. Any additional arguments will be passed into the listener’s callback function.




### Various basics
---------


##### Loading and Sending data … via XMLHttpRequest is ok
…?promises?
https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/send

promises documentation : https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise


##### observation : 

having two Vue apps can create a bit of a conflict… 

