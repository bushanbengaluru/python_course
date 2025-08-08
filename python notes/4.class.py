create title,side,main,and footer in one page
#First.js
import './First.css';
function First(){
    return (
     <div className="headercomp">
       <h1> this first components</h1>
        </div>
    );
}
export default First;
# First.css
.headercomp h1{
    
    background-color: blue;
}
# SideBar.js

import './SideBar.css';
function SideBar(){
    return(
        <div className="sidebarcomp">
            <div className='menu'>
            <ul>
                <li>Home</li>
                <li>Admin</li>
                <li>USer</li>
                <li>About Us</li>
            </ul>
            </div>
        </div>

    );
}
export default SideBar;
# SideBar.css

.sidebarcomp{
    background-color:brown;
    color: white;
    height: 500px;
}
.sidebarcomp ul{
    list-style-type: none;    
   
}
.sidebarcomp .menu{
    position: relative;
    top: 100px;
    font-size: large;
}
# Main.js
function Main(){
    return(
        <div className="maincomp">
        <h1>Main components</h1>
        </div>

    );
}
export default Main;
# Footer.js

import './Footer.css';
function Footer(){
    return(
        <div className="footercomp">
            <h1>@Kosmik Technology</h1>
        </div>

    );
}
export default Footer;

# Footer.css
.footercomp{
    background-color: blue;
}
# App.js
import SideBar from './SideBar';
import Main from './Main';
import Footer from './Footer';
function App() {
  return (
    <div className="App">
   <First />
   <SideBar />
   <Main />
   <Footer />
    </div>
  );
}
export default App;
#App.css
.App {
  text-align: center;
  display: grid;
  grid-template-areas: 
  "header header"
  "sidebar main"
  "footer footer ";
 
}
.headercomp{
  grid-area: header;
}
.sidebarcomp{
  grid-area: sidebar;
  height: 500px;
}
.footercomp{
  grid-area: footer;
}
--------------------------------------------------
# now go to Main.js file we can modiy any thing
function Main(){
    return(
        <div className="maincomp">
        <h1>hai nivas</h1>
        </div>

    );
}
export default Main;
# in case we can right through variable like
function Main(){
      let name='rama';
    return(
        <div className="maincomp">
        <h1>hai {name}</h1>
        </div>
    );
}
# in case we can read multiple name
in Main.js
function Main(){
    let names=['rama','sita','hanuma'];
    return(
        <div className="maincomp">
        <h1>hai {names.map((name)=>name)}</h1>
                      # map() function read multiple values
        </div>
    );
}
export default Main;
# now we want one by one name
in Main.js
function Main(){
    let names=['rama','sita','hanuma'];
    return(
        <div className="maincomp">
        <h1>hai {names.map((name)=>{
            return <p>{name}</p> # return multiple values
            })}</h1>
        </div>

    );
}
export default Main;
# In case we have dictionaty way of data
in Mian.js
function Main(){
    //let names=['rama','sita','hanuma'];
    let Person ={
        name:'rama',
        age:30,
        gender:"M"
    }
    return(
        <div className="maincomp">
        <h1>{Person.name} - {Person.age} - {Person.gender}</h1>
        </div>

    );
}
export default Main;
# in case we can take multiple dictionary values

function Main(){
    //let names=['rama','sita','hanuma'];
    let Person ={
        name:'rama',
        age:30,
        gender:"M"
    }
    let Person1 ={
        name:'sita',
        age:30,
        gender:"F"
    }
    let Person2 ={
        name:'Hanuma',
        age:30,
        gender:"M"
    }
    return(
        <div className="maincomp">
        <h1>{Person.name} - {Person.age} - {Person.gender}</h1>
        <h1>{Person1.name} - {Person1.age} - {Person1.gender}</h1>
        <h1>{Person2.name} - {Person2.age} - {Person2.gender}</h1>
        </div>

    );
}
export default Main; # but it is not correct
# now we have multiple dictionary values based on
in Main.js
function Main(){
    //let names=['rama','sita','hanuma'];
    let Person =[{
        name:'rama',
        age:30,
        gender:"M"
    },{
        name:'sita',
        age:30,
        gender:"F"
    },{
        name:'Hanuma',
        age:30,
        gender:"M"
    }]
    return(
        <div className="maincomp">
        {Person.map((obj)=>{
            return <h1>{obj.name}-{obj.age}-{obj.gender}</h1>
        })}
        </div>
    );
}
export default Main;
# now i want each values in box
# now create one js file in src
#EmpCard.js
import './EmpCard.css';
function EmpCard()
{
    return(
        <div className="empcardcomp">
            <p>Name:</p>
            <p>Age:</p>
            <p>Gender:</p>
        </div>
    )
}
export default EmpCard;
#EmpCard.css
.empcardcomp{
    width: 150px;
    height: 150px;
    border: 1px solid black;
    float: left;
}
# then go to Main.js
import EmpCard from "./EmpCard";
function Main(){
    //let names=['rama','sita','hanuma'];
    let Person =[{
        name:'rama',
        age:30,
        gender:"M"
    },{
        name:'sita',
        age:30,
        gender:"F"
    },{
        name:'Hanuma',
        age:30,
        gender:"M"
    }]
    return(
        <div className="maincomp">
        {Person.map((obj)=>{
            return <EmpCard />
        })}
        </div>
    );
}
export default Main;














