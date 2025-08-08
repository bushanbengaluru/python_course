# now go to App.js we can commend to all the components
# now im create one component that is ComponentA.js
function ComponentA(props){
      
    return(
        <div>
            <h1>Component A</h1>
        <p>name:{props.aname}</p>
        </div>
    );
}
export default ComponentA;
# now  to App.js
import ComponentA from './ComponentA';
function App() {
      # now i want name
      let name='rama';
  /*<First />
   <SideBar />
   <Main />
   <Footer />*/
  return (
    <div className="App">
   <ComponentA aname={name}/>
    </div>
  );
}

export default App;

# now again i want another sub compoment that is ComponentB.js

function ComponentB(){
    return(
        <div>

            <h1>ComponentB</h1>
        </div>
    );
}
export default ComponentB;

# now ComponentB rendering to ComponentA.js

import ComponentB from "./ComponentB";
function ComponentA(props){
    return(
        <div>
            <h1>Component A</h1>
            <p>name:{props.aname}</p>
            <ComponentB />
        </div>
    );
}
export default ComponentA;
# now componentA.js parent and componentB.js is child component
# now i want name:rama in componentB so we can use props right
and now we can take the parent to child again sub child and sub child we can
takke the value that s props drilling
#now go to ComponentA.js

import ComponentB from "./ComponentB";
function ComponentA(props){
    return(
        <div>
            <h1>Component A</h1>
            <p>name:{props.aname}</p>
            <ComponentB bname={props.aname}/> # add thid
        </div>
    );
}
export default ComponentA;
#now go to ComponentB.js

function ComponentB(props){ # add proprs
    
    return(
        <div>

            <h1>ComponentB</h1>
            <p>name:{props.bname}</p> # add this
        </div>
    );
}
export default ComponentB;
# but hear we can take the A component to B component adn i have another component
# my be we can use props we call like this we can confuse so we can avoid this holding
# we can use useContext(that is statemanagement)
# now they are given one is context hook
# context hook : it is create a variable in the global scope

# now go to App.js
import ComponentA from './ComponentA';
import { createContext } from 'react';
export const myContext=createContext();
function App() {
  let name='rama';
  /*<First />
   <SideBar />
   <Main />
   <Footer />*/
  return (
    <div className="App">
      <myContext.Provider value={name} >
    <ComponentA />
      </myContext.Provider>
  
    </div>
  );
}

export default App;
# now go to ComponentA.js

import ComponentB from "./ComponentB";
import { myContext } from "./App";
import { useContext } from "react";
function ComponentA(props){
    let name=useContext(myContext)
    return(
        <div>
            <h1>Component A</h1>
            <p>name:{name}</p>
            <ComponentB />
        </div>
    );
}
export default ComponentA;
# now go to ComponentB.js

import { myContext } from "./App";
import { useContext } from "react";
function ComponentB(){
    let name=useContext(myContext)
    
    return(
        <div>

            <h1>ComponentB</h1>
            <p>name:{name}</p>
        </div>
    );
}
export default ComponentB;
# now based on useState get the value
# go to App.js
import ComponentA from './ComponentA';
import { createContext, useState } from 'react';
export const myContext=createContext();

function App() {
  //let name='rama';
  let [name,setName]=useState(''); # add this
  /*<First />
   <SideBar />
   <Main />
   <Footer />*/
  return (
    <div className="App">
      <myContext.Provider value={[name,setName]} > # hear also
    <ComponentA />
      </myContext.Provider>
  
    </div>
  );
}

export default App;
# now go to ComponentA.js

import ComponentB from "./ComponentB";
import { myContext } from "./App";
import { useContext } from "react";
function ComponentA(props){
    let [name,setName]=useContext(myContext)
    return(
        <div>
            <h1>Component A</h1>
            <p>name:{name}</p>
            <ComponentB />
        </div>
    );
}
export default ComponentA;
# now go to ComponentB.js

import { myContext } from "./App";
import { useContext } from "react";
function ComponentB(){
    let [name,setName]=useContext(myContext)
    
    return(
        <div>

            <h1>ComponentB</h1>
            <p>name:{name}</p>
            <input type="text" onChange={(e)=>setName(e.target.value)} />
        # in case change the name autometically change both component name value
        </div>
    );
}
export default ComponentB;




















