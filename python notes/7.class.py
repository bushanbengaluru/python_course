#Conditional based : some cases showing and some cases hiding
#now go to Main.js
remove
 <Counter />
 
 import EmpCard from "./EmpCard";
import Counter from "./Counter";
import './Main.css';
function Main(){
    //let names=['rama','sita','hanuma']  
    return(
        <div className="maincomp">
   <button>show/hide</button>
        </div>
    );
}
export default Main;
# create Main.css in src

.maincomp button{
    height: 70px;
    width: 120px;
    margin-top: 40px;
    background-color: blue;
    color: white;
    font-size: x-large;
    border: none;
    margin: 20px;
}
# create ShowHide.js

function ShowHode()
{
    return(
        <div>
            <h1>We are good student</h1>
        </div>
    )
}
export default ShowHode;
# render to Main.js
import ShowHode from "./ShowHide";
  <button>show/hide</button>
<ShowHode />
#now in Main.js
we can take one variable isshow
once we can take isshow=false -- we dint show the value
 let isshow=false;
    return(
        <div className="maincomp">
   <button>show/hide</button>
      {isshow? <ShowHide/>:''}
        </div>

    );
}
export default Main;
# now we can take isshow=true we can see the value
#in Main.js
 let isshow=true;
    return(
        <div className="maincomp">
   <button>show/hide</button>
      {isshow? <ShowHide/>:''}
        </div>

    );
}
export default Main;
# now onClick button
#Main.js and see the result in console
function Main(){
    //let names=['rama','sita','hanuma'];
     let isshow=true;
     let changeshow=()=>{
        isshow=!isshow;
        console.log(isshow)
     }
    return(
        <div className="maincomp">
   <button on onClick={changeshow}>show/hide</button>
      {isshow? <ShowHide/>:''}
        </div>

    );
}
export default Main;
# its change the value but this norma variable
# now we can take the state variable
import { useState } from "react";
function Main(){
    #//let names=['rama','sita','hanuma'];
    # //let isshow=true;
     let [isshow,setIsShow]=useState(false);
     let changeshow=()=>{
      # // isshow=!isshow;
       setIsShow(!isshow)
        console.log(isshow)
     }
    return(
        <div className="maincomp">
   <button on onClick={changeshow}>show/hide</button>
      {isshow? <ShowHide/>:''}
        </div>
    );
}
export default Main;









