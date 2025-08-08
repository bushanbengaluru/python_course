# now update the component
# now create the UpdateEmployess.js
function UpdateEmployess(){
    return(
        <div className="updateempcomp">
          <label>
            Employee No:
            <input type="text" />
          </label><br/>
          <button>Get Data</button>
        </div>
    );
}
export default UpdateEmployess;
# now go to Main.js
import UpdateEmployess from "./UpdateEmployess";
function Main(){
    return(
        <div className="maincomp">
         <UpdateEmployess />
        </div>

    );
}
export default Main;
#now once we can give the eid in text field i want that particular data
# so we can use useState
# now go to UpdateEmployess.js
import axios from "axios";
import { useState } from "react";
function UpdateEmployess(){
    let [eid,setEid]=useState(0);
    let getdata=()=>{
        let fetch_url='http://127.0.0.1:8000/api/modify/'+eid+'/';
        axios.get(fetch_url).then((resp)=>{
            console.log(resp);
            console.log(resp.data);
        })   
        }
    return(
        <div className="updateempcomp">
          <label>
            Employee No:
            <input type="text" onChange={(event)=>setEid(event.target.value)}/>
          </label><br/>
          <button onClick={getdata}>Get Data</button>
        </div>
    );
}
export default UpdateEmployess;







