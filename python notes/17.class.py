# now react router dom:
now till now we are rendering one by one component
now i dont want like this
i want one menu in that menu
1 get component
2 post component
3 put component
4 delete component
# now click get component i want get component
# now click post component i want post component
# now click put component i want put component
# now click delete component i want delete component
that is react router dom
now we can create the router --router means urls -in django we are creating url
 the same way in react we creating router

 #now create the react router dom this is a another package
 npm install react-router-dom
 #now that package is install or not go to package.json and check
 # now go to Main.js
 import { Routes,Route } from "react-router-dom";
 # Route is a component and Routers is nothing but collection od Route
 import EmpCard from "./EmpCard";
import Counter from "./Counter";
import ShowHide from "./ShowHide";
import './Main.css';
import { useState } from "react";
import ToDoList from "./ToDoList";
import GetEmployees from "./GetEmployees";
import Test from "./Test";
import PostEmployees from "./PostEmployees";
import UpdateEmployess from "./UpdateEmployess";
import { Routes,Route } from "react-router-dom";
function Main(){
    return(
        <div className="maincomp">
         <Routes>
            <Route path="/GET" element={<GetEmployees />} />
            <Route path="/POST" element={<PostEmployees/>} />
            <Route path="/Update" element={<UpdateEmployess/>} />
         </Routes>
        </div>

    );
}
export default Main;
# now go to SideBar.js

import './SideBar.css';
import { Link } from 'react-router-dom';
function SideBar(){
    return(
        <div className="sidebarcomp">
            <div className='menu'>
            <ul>
                <li><Link to="/GET">GET</Link></li>
                <li><Link to="/POST">POST</Link></li>
                <li><Link to="Update">Update</Link>USer</li>
               
            </ul>
            </div>
        </div>

    );
}
export default SideBar;
# now go to index.js
import { BrowserRouter } from 'react-router-dom';
root.render(
  #<React.StrictMode>
  <BrowserRouter>
    <App />
    </BrowserRouter>
#</React.StrictMode>
);



 
