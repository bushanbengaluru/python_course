# Hooks : adding some extra behaviours to the components
#hooks introduce after 16.0
# whithout hooks we have only class based components
# after hooks all are writing function based components they are writing
now go to main.js we can revome all the the record
we want just this
function Main(){
    //let names=['rama','sita','hanuma'];
  
    return(
        <div className="maincomp">
   
        </div>

    );
}
export default Main;
#now requerment is i want to opetion one is + and -
# click + increment and - decriment
# Now create Counter.js
import './Couter.css';
function Counter(){
    return(
        <div>
            <button>Click Me</button>
        </div>
    );
}
export default Counter;
#Now create Couter.css
.coutercomp button{ 
    height: 70px;
    width: 120px;
    margin-top: 40px;
    background-color: blue;
    color: white;
    font-size: x-large;
    border:none;
}
# then go to Main.js
import EmpCard from "./EmpCard";
import Counter from "./Counter";
function Main(){
    //let names=['rama','sita','hanuma'];  
    return(
        <div className="maincomp">
   <Counter />
        </div>
    );
}
export default Main;

# now we want eventhandler
#now event means click the button that is event and do some thing the logic
# now again go to Couter.js file
function Counter(){
    let handleclick=()=>{
        alert('button click');
    }
    return(
        <div className="coutercomp">
            <button onClick={handleclick}>Click Me</button>
        # handleclick is a function
        </div>
    );
}
export default Counter;
# and now create two buttons like in Counter.js
function Counter(){
    let handleclick=()=>{
        alert('button click');
    }
    return(
        <div className="coutercomp">
            <button onClick={handleclick}>+</button>
         <button onClick={handleclick}>+</button>
        # handleclick is a function
        </div>
    );
}
# now saperate the button
go to Couter.css
# we ca add
      margin: 20px;
# and then go Counter.js we want two functions increment and decrement

import './Counter.css';
function Counter(){
    let count=0
    let increment=()=>{
        count=count+1
    }
    let decrement=()=>{
        count=count-1
    }
    return(
        <div className="coutercomp">
            <button onClick={increment}>+</button> 
            <button onClick={decrement}>-</button> 
            <p>Counter:{count}</p>
        </div>
    );
}
export default Counter;
# and go to Couter.css
#increse the couter size
.coutercomp p{
    font-size: xx-large;
}
# now once click + but we dint see the value but once we click on + or - event
# is going on how means
got o Counter.js Files
go to
let increment=()=>{
        count=count+1
        console.log(count) # once add this
# let decrement=()=>{
        count=count+1
        console.log(count) # add this
# and once run the project and go to inspect then click and increse the value
        and decrese the value
# value change but in that page not showing
# so we can do the re-render
# that is we can use -- useState
# we have different hooks
# now we are taking useState Hook
# what is useState: wich is used to re-render the component whener the particular
        # value changed
#now Counter.js file import userState
import './Counter.css';
import { useState } from 'react'; # useState we are importing to react packages
# when we use the useState we want [variable and method] that methods are
                                   # setter and getter method
function Counter(){
    let [count,setCount]=useState(0) # count is variable
                                     # setCount is a method
                                    # by using setCount we can modify the value
    let increment=()=>{
        setCount(count+1) # add this 
        console.log(count)
    }
    let decrement=()=>{
        setCount(count-1) # add this
        console.log(count)
    }
#now we dont want to nagetive values we want only 0 value in decrement
in Counter.js

    let decrement=()=>{
          if(count!=0)
              setCount(count-1) # add this
        console.log(count)
    }

# why hook useState use : whenever the value of changed in fronted 



    
















