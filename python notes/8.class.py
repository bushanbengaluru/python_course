# now i have text in text we can text i want that text in bellow
# now remove all the ShowHide code in Main.js and implement text file code
Main.js
function Main(){

    return(
        <div className="maincomp">
       <input type="text" />
        </div>
    );
}
export default Main;
#now text by using onChange
import { useState } from "react";
function Main(){
    
     let data='';
     let readdata=(event)=>{
        data=event.target.value;
        console.log(data);
     }
    return(
        <div className="maincomp">
       <input type="text" onChange={readdata}/>
        </div>

    );
}
#no live text Main.js
import { useState } from "react";
function Main(){
    let [data,setData]=useState('') # we are taken string data
   # // let data='';
     let readdata=(event)=>{
        setData(event.target.value);
        console.log(data);
     }
    return(
        <div className="maincomp">
       <input type="text" onChange={readdata}/>
       <p>{data}</p>
        </div>

    );
}
export default Main;




export default Main;
